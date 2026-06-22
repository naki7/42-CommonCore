#!/usr/bin/env python3
import subprocess
import re
import sys
import time

LOG_RE = re.compile(
    r"^(\d+)\s+(\d+)\s+(has taken a dongle|is compiling|is debugging|is refactoring|burned out)$"
)

def run_case(exe, args, timeout=10):
    try:
        p = subprocess.run(
            [exe] + [str(a) for a in args],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return p.returncode, p.stdout.strip().splitlines(), p.stderr
    except subprocess.TimeoutExpired:
        return None, [], "TIMEOUT"

def check_log_format(lines):
    bad = []
    for line in lines:
        if "finished with 0 remaining compiles" in line:
            continue
        if not LOG_RE.match(line):
            bad.append(line)
    return bad

def check_compile_sequence(lines):
    errors = []
    for i, line in enumerate(lines):
        if "is compiling" in line:
            if i < 2:
                errors.append(line)
                continue
            if "has taken a dongle" not in lines[i-1]:
                errors.append(line)
            if "has taken a dongle" not in lines[i-2]:
                errors.append(line)
    return errors

def report(name, ok, details=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if details:
        print("   ", details)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 test_codexion.py ./codexion")
        return 1

    exe = sys.argv[1]

    tests = [
        ("invalid scheduler",
         [5,800,200,200,200,3,50,"wrong"]),
        ("single coder",
         [1,800,200,200,200,1,50,"fifo"]),
        ("fifo completion",
         [5,5000,100,100,100,2,10,"fifo"]),
        ("edf completion",
         [5,5000,100,100,100,2,10,"edf"]),
        ("cooldown stress",
         [10,5000,50,50,50,3,200,"fifo"]),
    ]

    for name, args in tests:
        code, out, err = run_case(exe, args)

        if name == "invalid scheduler":
            report(name, code != 1)
            continue

        if code is None:
            report(name, False, "program timeout/deadlock")
            continue

        bad = check_log_format(out)
        report(f"{name} - log format", len(bad) == 0,
               f"{len(bad)} malformed lines")

        seq = check_compile_sequence(out)
        report(f"{name} - compile sequence", len(seq) == 0,
               f"{len(seq)} violations")

    print("\nNotes:")
    print("- Subject requires burnout detection <=10ms.")
    print("- FIFO/EDF fairness requires deeper queue inspection.")
    print("- Run under valgrind separately for leak testing.")

if __name__ == "__main__":
    main()
