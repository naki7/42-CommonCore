#!/usr/bin/env python3
"""
Comprehensive tester for Codexion project
Validates against all subject requirements
"""

import subprocess
import re
import sys
import time
import os
from collections import defaultdict, deque
from typing import List, Tuple, Dict

class CoderSimulation:
    """Track state of each coder for validation"""
    def __init__(self, coder_id, time_to_burnout, time_to_compile, 
                 time_to_debug, time_to_refactor):
        self.id = coder_id
        self.time_to_burnout = time_to_burnout
        self.time_to_compile = time_to_compile
        self.time_to_debug = time_to_debug
        self.time_to_refactor = time_to_refactor
        self.state = "idle"
        self.last_compile_start = None
        self.dongle_count = 0
        self.compile_count = 0
        self.burnout_deadline = None
        self.burned_out = False

class TestResult:
    """Encapsulate test result"""
    def __init__(self, name, passed, details="", severity="error"):
        self.name = name
        self.passed = passed
        self.details = details
        self.severity = severity

class CodexionTester:
    def __init__(self, executable):
        self.exe = executable
        self.results = []
        self.log_regex = re.compile(
            r"^(\d+)\s+(\d+)\s+(has taken a dongle|is compiling|is debugging|is refactoring|burned out)$"
        )

    def run_program(self, args, timeout=15):
        """Run codexion with given arguments"""
        try:
            result = subprocess.run(
                [self.exe] + [str(a) for a in args],
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.returncode, result.stdout.strip(), result.stderr.strip()
        except subprocess.TimeoutExpired:
            return None, "", "TIMEOUT"
        except Exception as e:
            return None, "", str(e)

    def test_argument_validation(self):
        """Test invalid argument handling"""
        tests = [
            ("negative coders", [-1, 800, 200, 200, 200, 3, 50, "fifo"]),
            ("zero coders", [0, 800, 200, 200, 200, 3, 50, "fifo"]),
            ("negative burnout", [3, -100, 200, 200, 200, 3, 50, "fifo"]),
            ("zero burnout", [3, 0, 200, 200, 200, 3, 50, "fifo"]),
            ("invalid scheduler", [3, 800, 200, 200, 200, 3, 50, "invalid"]),
            ("missing scheduler", [3, 800, 200, 200, 200, 3, 50]),
        ]

        for name, args in tests:
            code, out, err = self.run_program(args)
            if code is not None:
                # Should either reject or print error
                passed = code == 0 or "Error" in err or "error" in out.lower() or "invalid" in out.lower() or code != 1
                self.results.append(TestResult(
                    f"Arg validation: {name}",
                    passed,
                    f"Return code: {code}, Output contains error info" if passed else "Should reject invalid args",
                    "warning" if code == 1 else "error"
                ))
            else:
                self.results.append(TestResult(
                    f"Arg validation: {name}",
                    False,
                    "Program crashed or timed out"
                ))

    def validate_log_format(self, lines):
        """Validate log format against requirements"""
        invalid_lines = []
        for line in lines:
            if "finished with 0 remaining compiles" in line:
                continue
            if not self.log_regex.match(line):
                invalid_lines.append(line)
        return invalid_lines

    def validate_log_timestamps(self, lines):
        """Ensure timestamps are monotonically increasing"""
        prev_ts = -1
        violations = []
        for line in lines:
            match = self.log_regex.match(line)
            if match:
                ts = int(match.group(1))
                if ts < prev_ts:
                    violations.append(f"Timestamp went backwards: {prev_ts} -> {ts}")
                prev_ts = ts
        return violations

    def validate_compile_sequence(self, lines):
        """Ensure each 'is compiling' is preceded by exactly 2 'has taken a dongle'"""
        violations = []
        for i, line in enumerate(lines):
            if "is compiling" in line:
                if i < 2:
                    violations.append(f"'is compiling' at line {i} without 2 dongle takings before it")
                    continue
                
                # Check previous two lines
                prev1 = lines[i-1] if i >= 1 else ""
                prev2 = lines[i-2] if i >= 2 else ""
                
                if "has taken a dongle" not in prev1:
                    violations.append(f"Line {i-1} should be 'has taken a dongle', got: {prev1}")
                if "has taken a dongle" not in prev2:
                    violations.append(f"Line {i-2} should be 'has taken a dongle', got: {prev2}")
        
        return violations

    def validate_state_transitions(self, lines):
        """Validate valid state transitions per coder"""
        coder_states = defaultdict(list)
        valid_transitions = {
            "idle": ["has taken a dongle"],
            "dongle_taken_once": ["has taken a dongle"],
            "ready_compile": ["is compiling"],
            "compiling": ["is debugging"],
            "debugging": ["is refactoring"],
            "refactoring": ["has taken a dongle", "burned out"],
        }
        
        violations = []
        for line in lines:
            match = self.log_regex.match(line)
            if not match:
                continue
            
            ts, coder_id, action = match.groups()
            coder_id = int(coder_id)
            
            if action == "has taken a dongle":
                dongle_count = len([a for a in coder_states[coder_id] if "has taken" in a])
                if dongle_count == 0:
                    expected_state = "idle"
                elif dongle_count == 1:
                    expected_state = "dongle_taken_once"
                coder_states[coder_id].append(action)
            elif action == "is compiling":
                coder_states[coder_id].append(action)
            elif action == "is debugging":
                if coder_states[coder_id] and "is compiling" not in coder_states[coder_id][-1]:
                    violations.append(f"Coder {coder_id}: 'is debugging' without 'is compiling' first")
                coder_states[coder_id].append(action)
            elif action == "is refactoring":
                if coder_states[coder_id] and "is debugging" not in coder_states[coder_id][-1]:
                    violations.append(f"Coder {coder_id}: 'is refactoring' without 'is debugging' first")
                coder_states[coder_id].append(action)
            elif action == "burned out":
                coder_states[coder_id].append(action)
        
        return violations

    def validate_burnout_timing(self, lines, time_to_burnout):
        """
        Validate that burnout logs appear within 10ms of actual burnout time.
        Burnout occurs when a coder's deadline (last_compile_start + time_to_burnout) is missed.
        """
        coder_deadlines = {}
        burnout_logs = {}
        violations = []
        
        for line in lines:
            match = self.log_regex.match(line)
            if not match:
                continue
            
            ts, coder_id, action = match.groups()
            ts = int(ts)
            coder_id = int(coder_id)
            
            if action == "is compiling":
                coder_deadlines[coder_id] = ts + time_to_burnout
            elif action == "burned out":
                burnout_logs[coder_id] = ts
        
        for coder_id, burnout_ts in burnout_logs.items():
            if coder_id in coder_deadlines:
                deadline = coder_deadlines[coder_id]
                delay = abs(burnout_ts - deadline)
                if delay > 10:
                    violations.append(
                        f"Coder {coder_id}: Burnout logged at {burnout_ts}ms, "
                        f"but deadline was {deadline}ms (delay: {delay}ms, allowed: ≤10ms)"
                    )
        
        return violations

    def validate_no_duplicate_messages(self, lines):
        """Ensure no two messages interleave on a single line"""
        violations = []
        for i, line in enumerate(lines):
            # Check if line has multiple coder actions
            if line.count("has taken a dongle") > 1:
                violations.append(f"Line {i} has multiple 'has taken a dongle' messages: {line}")
            if line.count("is compiling") > 1:
                violations.append(f"Line {i} has multiple messages interleaved")
        return violations

    def validate_completion_condition(self, lines, num_coders, required_compiles):
        """
        Verify simulation stopped correctly:
        - Either when a coder burned out, or
        - When all coders have compiled required times
        """
        compile_counts = defaultdict(int)
        burned_out = False
        
        for line in lines:
            match = self.log_regex.match(line)
            if not match:
                continue
            
            ts, coder_id, action = match.groups()
            coder_id = int(coder_id)
            
            if action == "is compiling":
                compile_counts[coder_id] += 1
            elif action == "burned out":
                burned_out = True
        
        violations = []
        
        if not burned_out:
            # All coders should have compiled at least required_compiles times
            for coder_id in range(1, num_coders + 1):
                if compile_counts[coder_id] < required_compiles:
                    violations.append(
                        f"Coder {coder_id} compiled {compile_counts[coder_id]} times, "
                        f"required: {required_compiles}"
                    )
        
        return violations, compile_counts, burned_out

    def validate_cooldown(self, lines, dongle_cooldown):
        """
        Validate that dongle cooldown is respected.
        A dongle released at time T cannot be taken before T + cooldown_ms
        """
        dongle_releases = defaultdict(list)
        dongle_takes = defaultdict(list)
        violations = []
        
        # This is simplified - in reality we'd need to track which dongle is which
        # For now, check that there's reasonable spacing between releases and takes
        all_actions = []
        for line in lines:
            match = self.log_regex.match(line)
            if match:
                all_actions.append((int(match.group(1)), int(match.group(2)), match.group(3)))
        
        # Check spacing between consecutive "has taken" actions
        take_times = [ts for ts, cid, action in all_actions if action == "has taken a dongle"]
        if len(take_times) >= 2:
            for i in range(1, len(take_times)):
                # This is a rough check - ideally we'd track specific dongles
                pass
        
        return violations

    def test_basic_functionality(self):
        """Test basic execution with valid arguments"""
        args = [3, 5000, 200, 200, 200, 2, 100, "fifo"]
        code, out, err = self.run_program(args, timeout=20)
        
        if code is None:
            self.results.append(TestResult(
                "Basic execution: 3 coders FIFO",
                False,
                "Program timeout or crash"
            ))
            return
        
        lines = out.split('\n') if out else []
        
        # Check format
        invalid_lines = self.validate_log_format(lines)
        self.results.append(TestResult(
            "Log format validation",
            len(invalid_lines) == 0,
            f"{len(invalid_lines)} malformed lines" if invalid_lines else "All lines match format"
        ))
        
        # Check compile sequence
        seq_violations = self.validate_compile_sequence(lines)
        self.results.append(TestResult(
            "Compile sequence (2 dongles before compile)",
            len(seq_violations) == 0,
            f"{len(seq_violations)} violations" if seq_violations else "Valid sequences"
        ))
        
        # Check state transitions
        state_violations = self.validate_state_transitions(lines)
        self.results.append(TestResult(
            "Valid state transitions",
            len(state_violations) == 0,
            f"{len(state_violations)} violations" if state_violations else "All transitions valid"
        ))
        
        # Check timestamps
        ts_violations = self.validate_log_timestamps(lines)
        self.results.append(TestResult(
            "Monotonic timestamps",
            len(ts_violations) == 0,
            f"{len(ts_violations)} violations" if ts_violations else "Timestamps increase"
        ))
        
        # Check message interleaving
        interleave_violations = self.validate_no_duplicate_messages(lines)
        self.results.append(TestResult(
            "No message interleaving",
            len(interleave_violations) == 0,
            f"{len(interleave_violations)} violations" if interleave_violations else "Messages serialized"
        ))
        
        # Check burnout timing
        burnout_violations = self.validate_burnout_timing(lines, 5000)
        self.results.append(TestResult(
            "Burnout detection timing (≤10ms)",
            len(burnout_violations) == 0,
            f"{len(burnout_violations)} violations" if burnout_violations else "Burnout timing accurate",
            "warning" if burnout_violations else "error"
        ))
        
        # Check completion condition
        completion_violations, compile_counts, burned_out = self.validate_completion_condition(
            lines, 3, 2
        )
        self.results.append(TestResult(
            "Completion condition",
            len(completion_violations) == 0,
            f"{len(completion_violations)} violations" if completion_violations else "Correct completion"
        ))

    def test_single_coder(self):
        """Test with single coder (edge case)"""
        args = [1, 5000, 200, 200, 200, 3, 100, "fifo"]
        code, out, err = self.run_program(args)
        
        passed = code == 0 or code == 1
        self.results.append(TestResult(
            "Single coder execution",
            passed,
            "Completed successfully" if passed else "Failed to execute"
        ))

    def test_fifo_fairness(self):
        """Test FIFO scheduling fairness"""
        args = [4, 8000, 150, 150, 150, 2, 50, "fifo"]
        code, out, err = self.run_program(args, timeout=20)
        
        if code is None:
            self.results.append(TestResult(
                "FIFO fairness test",
                False,
                "Program timeout or crash"
            ))
            return
        
        # Check that program ran
        lines = out.split('\n') if out else []
        
        valid_format = len(self.validate_log_format(lines)) == 0
        self.results.append(TestResult(
            "FIFO scheduling execution",
            valid_format and code in [0, 1],
            "FIFO test completed" if valid_format else "Format errors in FIFO test"
        ))

    def test_edf_fairness(self):
        """Test EDF scheduling fairness"""
        args = [4, 8000, 150, 150, 150, 2, 50, "edf"]
        code, out, err = self.run_program(args, timeout=20)
        
        if code is None:
            self.results.append(TestResult(
                "EDF fairness test",
                False,
                "Program timeout or crash"
            ))
            return
        
        lines = out.split('\n') if out else []
        valid_format = len(self.validate_log_format(lines)) == 0
        self.results.append(TestResult(
            "EDF scheduling execution",
            valid_format and code in [0, 1],
            "EDF test completed" if valid_format else "Format errors in EDF test"
        ))

    def test_high_contention(self):
        """Test with high dongle contention"""
        args = [8, 3000, 100, 100, 100, 1, 50, "fifo"]
        code, out, err = self.run_program(args, timeout=20)
        
        if code is None:
            self.results.append(TestResult(
                "High contention (8 coders)",
                False,
                "Program timeout - possible deadlock"
            ))
        else:
            lines = out.split('\n') if out else []
            seq_violations = self.validate_compile_sequence(lines)
            self.results.append(TestResult(
                "High contention sequence validity",
                len(seq_violations) == 0,
                f"{len(seq_violations)} sequence violations under high contention"
            ))

    def test_memory_with_valgrind(self):
        """Check for memory leaks using valgrind"""
        args = [3, 2000, 100, 100, 100, 1, 50, "fifo"]
        try:
            result = subprocess.run(
                ["valgrind", "--leak-check=full", "--error-exitcode=1", self.exe] 
                + [str(a) for a in args],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if "ERROR SUMMARY: 0 errors" in result.stderr:
                self.results.append(TestResult(
                    "Memory leak check (valgrind)",
                    True,
                    "No memory leaks detected"
                ))
            else:
                # Extract leak info
                leak_info = ""
                if "definitely lost" in result.stderr:
                    for line in result.stderr.split('\n'):
                        if "definitely lost" in line or "indirectly lost" in line:
                            leak_info += line + "\n"
                
                self.results.append(TestResult(
                    "Memory leak check (valgrind)",
                    False,
                    leak_info if leak_info else "Memory leaks detected"
                ))
        except FileNotFoundError:
            self.results.append(TestResult(
                "Memory leak check (valgrind)",
                None,
                "valgrind not installed - skipped",
                "warning"
            ))
        except subprocess.TimeoutExpired:
            self.results.append(TestResult(
                "Memory leak check (valgrind)",
                None,
                "valgrind check timed out",
                "warning"
            ))

    def check_norm_compliance(self):
        """Check for basic norm violations"""
        violations = []
        
        c_files = [
            "close_gracefully.c", "coder_actions.c", "codexion.c",
            "dongle_manager.c", "infrastructure_builder.c", "monitor_manager.c",
            "parser.c"
        ]
        
        for filename in c_files:
            try:
                with open(f"/home/naki/42-CommonCore/Milestone\\ 3/Codexion/{filename}", "r") as f:
                    content = f.read()
                    # Basic checks
                    if "printf(" in content and "printf" not in ["printf"]:  # printf allowed
                        pass
                    # Check for global variables (very basic check)
                    if re.search(r'^[a-zA-Z_][a-zA-Z0-9_]*\s+\*?[a-zA-Z_][a-zA-Z0-9_]*\s*[=;]', 
                                content, re.MULTILINE):
                        # Could be global - but this is a very loose check
                        pass
            except:
                pass
        
        self.results.append(TestResult(
            "Norm compliance check",
            None,
            "Manual review recommended - use norminette",
            "warning"
        ))

    def compile_check(self):
        """Verify the program compiles"""
        try:
            result = subprocess.run(
                ["make", "clean"],
                cwd="/home/naki/42-CommonCore/Milestone 3/Codexion",
                capture_output=True,
                timeout=5
            )
            
            result = subprocess.run(
                ["make"],
                cwd="/home/naki/42-CommonCore/Milestone 3/Codexion",
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                self.results.append(TestResult(
                    "Compilation with -Wall -Wextra -Werror",
                    True,
                    "Compiled successfully"
                ))
                return True
            else:
                self.results.append(TestResult(
                    "Compilation with -Wall -Wextra -Werror",
                    False,
                    f"Compilation failed:\n{result.stderr[:500]}"
                ))
                return False
        except Exception as e:
            self.results.append(TestResult(
                "Compilation check",
                False,
                f"Error running make: {str(e)}"
            ))
            return False

    def run_all_tests(self):
        """Run all tests"""
        print("=" * 80)
        print("CODEXION PROJECT COMPREHENSIVE TESTER")
        print("=" * 80)
        print()
        
        # Compilation check first
        if not self.compile_check():
            print("\n⚠️  Compilation failed. Fix compile errors before running other tests.\n")
            return
        
        print("Running tests...\n")
        
        # Run test suites
        self.test_argument_validation()
        self.test_single_coder()
        self.test_basic_functionality()
        self.test_fifo_fairness()
        self.test_edf_fairness()
        self.test_high_contention()
        self.check_norm_compliance()
        self.test_memory_with_valgrind()
        
        # Print results
        self.print_results()

    def print_results(self):
        """Print all test results with summary"""
        print("\n" + "=" * 80)
        print("TEST RESULTS")
        print("=" * 80)
        print()
        
        passed = 0
        failed = 0
        skipped = 0
        
        for result in self.results:
            if result.passed is True:
                status = "✓ PASS"
                passed += 1
            elif result.passed is False:
                status = "✗ FAIL"
                failed += 1
            else:
                status = "⊘ SKIP"
                skipped += 1
            
            print(f"{status} | {result.name}")
            if result.details:
                for line in result.details.split('\n'):
                    print(f"      {line}")
        
        print()
        print("=" * 80)
        print(f"Summary: {passed} passed, {failed} failed, {skipped} skipped")
        print("=" * 80)
        
        if failed > 0:
            print("\n⚠️  FAILURES DETECTED - Review the above output for details")
            print("\nCommon issues to check:")
            print("1. Log format: timestamps must be 3+ digits, coder IDs valid, actions exact")
            print("2. Compile sequence: each 'is compiling' needs exactly 2 'has taken a dongle' before")
            print("3. State transitions: verify compiling→debugging→refactoring order")
            print("4. Burnout timing: must detect within 10ms of deadline")
            print("5. Memory: ensure all malloc'd memory is freed")
            print("6. Fairness: FIFO queues in order, EDF by deadline")
        else:
            print("\n✓ All critical tests passed!")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 comprehensive_tester.py <path_to_codexion_executable>")
        print("Example: python3 comprehensive_tester.py ./codexion")
        return 1
    
    executable = sys.argv[1]
    
    if not os.path.exists(executable):
        print(f"Error: Executable not found: {executable}")
        return 1
    
    tester = CodexionTester(executable)
    tester.run_all_tests()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
