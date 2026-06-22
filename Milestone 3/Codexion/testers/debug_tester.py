#!/usr/bin/env python3
"""
Debug version of tester - shows detailed output
"""

import subprocess
import re
import sys

def run_program(exe, args, timeout=15):
    """Run codexion with given arguments"""
    try:
        result = subprocess.run(
            [exe] + [str(a) for a in args],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except subprocess.TimeoutExpired:
        return None, "", "TIMEOUT"
    except Exception as e:
        return None, "", str(e)

def debug_log_output():
    """Show raw output from basic test"""
    print("=" * 80)
    print("DEBUG: Raw program output (3 coders, FIFO, complete 2 compiles)")
    print("=" * 80)
    
    args = [3, 5000, 200, 200, 200, 2, 100, "fifo"]
    code, out, err = run_program("./codexion", args, timeout=20)
    
    print(f"Return code: {code}")
    print(f"Stderr: {err}")
    print("\nStdout output:")
    print("-" * 80)
    lines = out.split('\n') if out else []
    for i, line in enumerate(lines):
        print(f"{i:3d}: {repr(line)}")
    print("-" * 80)
    print()
    
    # Check format
    log_regex = re.compile(
        r"^(\d+)\s+(\d+)\s+(has taken a dongle|is compiling|is debugging|is refactoring|burned out)$"
    )
    
    print("Format validation:")
    bad_lines = []
    for i, line in enumerate(lines):
        if "finished with 0 remaining compiles" in line:
            print(f"  {i:3d}: [SPECIAL] {line}")
            continue
        match = log_regex.match(line)
        if match:
            print(f"  {i:3d}: [OK] {line}")
        else:
            print(f"  {i:3d}: [BAD] {repr(line)}")
            bad_lines.append((i, line))
    
    print()
    print("Compile sequence validation:")
    for i, line in enumerate(lines):
        if "is compiling" in line:
            print(f"  Line {i}: 'is compiling' found")
            if i >= 1:
                print(f"    Line {i-1}: {repr(lines[i-1])}")
            if i >= 2:
                print(f"    Line {i-2}: {repr(lines[i-2])}")
            
            # Check
            prev1_ok = i >= 1 and "has taken a dongle" in lines[i-1]
            prev2_ok = i >= 2 and "has taken a dongle" in lines[i-2]
            print(f"    Prev-1 has dongle: {prev1_ok}, Prev-2 has dongle: {prev2_ok}")

def debug_fifo():
    print("\n" + "=" * 80)
    print("DEBUG: FIFO Test (4 coders)")
    print("=" * 80)
    
    args = [4, 8000, 150, 150, 150, 2, 50, "fifo"]
    code, out, err = run_program("./codexion", args, timeout=20)
    
    print(f"Return code: {code}")
    
    lines = out.split('\n') if out else []
    log_regex = re.compile(
        r"^(\d+)\s+(\d+)\s+(has taken a dongle|is compiling|is debugging|is refactoring|burned out)$"
    )
    
    print(f"Total lines: {len(lines)}")
    bad_count = 0
    for i, line in enumerate(lines):
        if "finished with 0 remaining compiles" in line:
            continue
        match = log_regex.match(line)
        if not match:
            print(f"  Line {i}: BAD FORMAT: {repr(line)}")
            bad_count += 1
    
    print(f"Bad format lines: {bad_count}")

def debug_edf():
    print("\n" + "=" * 80)
    print("DEBUG: EDF Test (4 coders)")
    print("=" * 80)
    
    args = [4, 8000, 150, 150, 150, 2, 50, "edf"]
    code, out, err = run_program("./codexion", args, timeout=20)
    
    print(f"Return code: {code}")
    
    lines = out.split('\n') if out else []
    log_regex = re.compile(
        r"^(\d+)\s+(\d+)\s+(has taken a dongle|is compiling|is debugging|is refactoring|burned out)$"
    )
    
    print(f"Total lines: {len(lines)}")
    bad_count = 0
    for i, line in enumerate(lines):
        if "finished with 0 remaining compiles" in line:
            continue
        match = log_regex.match(line)
        if not match:
            print(f"  Line {i}: BAD FORMAT: {repr(line)}")
            bad_count += 1
    
    print(f"Bad format lines: {bad_count}")

def debug_high_contention():
    print("\n" + "=" * 80)
    print("DEBUG: High Contention (8 coders)")
    print("=" * 80)
    
    args = [8, 3000, 100, 100, 100, 1, 50, "fifo"]
    code, out, err = run_program("./codexion", args, timeout=20)
    
    print(f"Return code: {code}")
    
    lines = out.split('\n') if out else []
    log_regex = re.compile(
        r"^(\d+)\s+(\d+)\s+(has taken a dongle|is compiling|is debugging|is refactoring|burned out)$"
    )
    
    print(f"Total lines: {len(lines)}")
    print("\nCompile sequence violations:")
    violations = 0
    for i, line in enumerate(lines):
        if "is compiling" in line:
            prev1_ok = i >= 1 and "has taken a dongle" in lines[i-1]
            prev2_ok = i >= 2 and "has taken a dongle" in lines[i-2]
            
            if not (prev1_ok and prev2_ok):
                print(f"  Line {i}: 'is compiling' - prev1_ok={prev1_ok}, prev2_ok={prev2_ok}")
                if i >= 1:
                    print(f"    {i-1}: {repr(lines[i-1])}")
                if i >= 2:
                    print(f"    {i-2}: {repr(lines[i-2])}")
                violations += 1
    
    print(f"Total violations: {violations}")

if __name__ == "__main__":
    debug_log_output()
    debug_fifo()
    debug_edf()
    debug_high_contention()
