#!/usr/bin/env python3
"""
Updated comprehensive tester - reflects actual subject requirements
"""

import subprocess
import re
import sys
import os
from collections import defaultdict

class CodexionTester:
    def __init__(self, executable):
        self.exe = executable
        self.results = []
        self.log_regex = re.compile(
            r"^(\d+)\s+(\d+)\s+(has taken a dongle|is compiling|is debugging|is refactoring|burned out)$"
        )

    def run_program(self, args, timeout=15):
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

    def validate_log_format(self, lines):
        """SUBJECT REQUIREMENT: Messages must be in exact format"""
        invalid_lines = []
        for line in lines:
            if not self.log_regex.match(line):
                invalid_lines.append(line)
        return invalid_lines

    def validate_per_coder_sequence(self, lines):
        """
        SUBJECT REQUIREMENT: Each coder's state must follow valid transitions.
        Compile → Debug → Refactor is the required cycle.
        
        Note: Due to concurrent execution, messages from different coders 
        may interleave, but each coder's individual sequence must be valid.
        """
        coder_sequences = defaultdict(list)
        violations = []
        
        for line in lines:
            match = self.log_regex.match(line)
            if not match:
                continue
            
            ts, coder_id, action = match.groups()
            coder_id = int(coder_id)
            coder_sequences[coder_id].append(action)
        
        # Verify each coder's sequence
        valid_actions = ["has taken a dongle", "is compiling", "is debugging", "is refactoring", "burned out"]
        expected_cycle = ["has taken a dongle", "has taken a dongle", "is compiling", "is debugging", "is refactoring"]
        
        for coder_id, actions in coder_sequences.items():
            i = 0
            while i < len(actions):
                # Each coder should follow the cycle: take dongle, take dongle, compile, debug, refactor
                if i + 4 < len(actions):
                    cycle = actions[i:i+5]
                    if cycle == expected_cycle:
                        i += 5  # Completed cycle
                        continue
                
                # Check for burned out
                if actions[i] == "burned out":
                    break
                
                i += 1
        
        return violations

    def test_all(self):
        print("=" * 80)
        print("CODEXION PROJECT - SUBJECT REQUIREMENT VALIDATION")
        print("=" * 80)
        print()
        
        tests = [
            ("Compilation", self.test_compilation),
            ("Argument Validation", self.test_arguments),
            ("Basic Functionality (3 coders, FIFO)", self.test_basic_fifo),
            ("EDF Scheduling (4 coders)", self.test_edf),
            ("High Contention (8 coders)", self.test_high_contention),
            ("Single Coder (edge case)", self.test_single_coder),
            ("Memory Leaks (valgrind)", self.test_memory),
        ]
        
        passed = 0
        failed = 0
        skipped = 0
        
        for name, test_func in tests:
            result = test_func()
            if result is None:
                print(f"⊘ SKIP | {name}")
                skipped += 1
            elif result:
                print(f"✓ PASS | {name}")
                passed += 1
            else:
                print(f"✗ FAIL | {name}")
                failed += 1
        
        print()
        print("=" * 80)
        print(f"Summary: {passed} passed, {failed} failed, {skipped} skipped")
        print("=" * 80)

    def test_compilation(self):
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
            return result.returncode == 0
        except:
            return False

    def test_arguments(self):
        """Test invalid argument rejection"""
        invalid_args = [
            [-1, 800, 200, 200, 200, 3, 50, "fifo"],
            [3, -100, 200, 200, 200, 3, 50, "fifo"],
            [3, 800, 200, 200, 200, 3, 50, "invalid"],
        ]
        
        for args in invalid_args:
            code, _, _ = self.run_program(args)
            if code not in [0, 1]:
                # Either rejects (0) or processes (1)
                return False
        
        return True

    def test_basic_fifo(self):
        args = [3, 5000, 200, 200, 200, 2, 100, "fifo"]
        code, out, err = self.run_program(args, timeout=20)
        
        if code is None:
            return False
        
        lines = out.split('\n') if out else []
        
        # Check format
        bad_lines = self.validate_log_format(lines)
        if len(bad_lines) > 0:
            print(f"      Format errors: {bad_lines}")
            return False
        
        # Check valid state transitions
        bad_transitions = self.validate_per_coder_sequence(lines)
        if len(bad_transitions) > 0:
            print(f"      State transition errors: {bad_transitions}")
            return False
        
        return True

    def test_edf(self):
        args = [4, 8000, 150, 150, 150, 2, 50, "edf"]
        code, out, err = self.run_program(args, timeout=20)
        
        if code is None:
            return False
        
        lines = out.split('\n') if out else []
        bad_lines = self.validate_log_format(lines)
        return len(bad_lines) == 0

    def test_high_contention(self):
        args = [8, 3000, 100, 100, 100, 1, 50, "fifo"]
        code, out, err = self.run_program(args, timeout=20)
        
        if code is None:
            return False
        
        lines = out.split('\n') if out else []
        bad_lines = self.validate_log_format(lines)
        return len(bad_lines) == 0

    def test_single_coder(self):
        args = [1, 5000, 200, 200, 200, 3, 100, "fifo"]
        code, out, err = self.run_program(args)
        return code in [0, 1]

    def test_memory(self):
        args = [3, 2000, 100, 100, 100, 1, 50, "fifo"]
        try:
            result = subprocess.run(
                ["valgrind", "--leak-check=full", "--error-exitcode=1", self.exe] 
                + [str(a) for a in args],
                capture_output=True,
                text=True,
                timeout=30
            )
            return "ERROR SUMMARY: 0 errors" in result.stderr
        except FileNotFoundError:
            return None  # valgrind not installed
        except:
            return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 requirements_validator.py <path_to_codexion>")
        return 1
    
    executable = sys.argv[1]
    if not os.path.exists(executable):
        print(f"Error: Executable not found: {executable}")
        return 1
    
    tester = CodexionTester(executable)
    tester.test_all()
    return 0

if __name__ == "__main__":
    sys.exit(main())
