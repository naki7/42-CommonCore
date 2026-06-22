# Codexion Test Suites - Quick Reference Guide

## Three Test Suites Available

### 1. **Requirements Validator** ⭐ RECOMMENDED
**File**: `requirements_validator.py`

Tests the core subject requirements in a simple format.

```bash
python3 requirements_validator.py ./codexion
```

**Output**: 7/7 tests showing what matters for evaluation
- ✓ Compilation with required flags
- ✓ Argument validation
- ✓ Basic functionality
- ✓ EDF scheduling
- ✓ High contention
- ✓ Edge cases
- ✓ Memory integrity

**Best for**: Quick validation before submission

---

### 2. **Comprehensive Tester**
**File**: `comprehensive_tester.py`

Extensive validation including detailed error messages and format checking.

```bash
python3 comprehensive_tester.py ./codexion
```

**Output**: Detailed breakdown of 19 different test categories

**Includes**:
- Argument validation (all error cases)
- Log format verification
- State transition validation
- Timestamp ordering
- Message interleaving detection
- Burnout timing precision (≤10ms)
- FIFO & EDF fairness
- Memory leak detection

**Best for**: Thorough debugging and understanding issues

---

### 3. **Debug Tester**
**File**: `debug_tester.py`

Shows raw program output with line-by-line analysis.

```bash
python3 debug_tester.py
```

**Output**: Raw output from program with validation results for each line

**Shows**:
- Exact output with line numbers
- Format validation for each line
- Compile sequence analysis
- Which lines violate which requirements

**Best for**: Understanding what the program outputs and why tests pass/fail

---

## Manual Testing

### Test FIFO Scheduling
```bash
./codexion 3 5000 200 200 200 2 100 "fifo"
```
- 3 coders
- 5000ms burnout timeout
- 200ms compile time
- 200ms debug time
- 200ms refactor time
- Each coder must compile 2 times
- 100ms dongle cooldown
- FIFO scheduling

### Test EDF Scheduling
```bash
./codexion 3 5000 200 200 200 2 100 "edf"
```
Same as above but with EDF (Earliest Deadline First) scheduling instead of FIFO.

### Test High Contention (Stress Test)
```bash
./codexion 8 3000 100 100 100 1 50 "fifo"
```
- 8 coders (high competition for 8 dongles)
- Shorter timeouts and compile times
- Single compilation required
- Only 50ms cooldown between dongle uses

### Test Single Coder (Edge Case)
```bash
./codexion 1 5000 200 200 200 3 100 "fifo"
```
Single coder with one dongle - minimum case.

### Test Invalid Arguments (Should Reject)
```bash
./codexion -1 1000 100 100 100 1 50 "fifo"     # Negative coders
./codexion 3 1000 100 100 100 1 50 "invalid"   # Bad scheduler
./codexion 3 1000 100 100 100 1 50             # Missing scheduler
```

---

## Memory Leak Testing with Valgrind

### Single run with leak check
```bash
valgrind --leak-check=full --error-exitcode=1 ./codexion 3 2000 100 100 100 1 50 "fifo"
```

Should show: `ERROR SUMMARY: 0 errors`

### With more detail
```bash
valgrind --leak-check=full --show-leak-kinds=all ./codexion 3 2000 100 100 100 1 50 "fifo"
```

---

## Expected Output Format

Each line should be:
```
timestamp_in_ms coder_id action
```

**Valid actions**:
- `has taken a dongle` (appears twice before compiling)
- `is compiling`
- `is debugging`
- `is refactoring`
- `burned out` (optional - only if burnout occurs)

**Example**:
```
0 1 has taken a dongle
2 1 has taken a dongle
2 1 is compiling
202 1 is debugging
402 1 is refactoring
```

---

## Test Interpretation

### ✓ PASS Means
- The test requirement is satisfied
- Program behaves correctly for that scenario
- No issues detected

### ✗ FAIL Means
- The test requirement is NOT satisfied
- Issue details shown below the test name
- Check FINAL_TEST_REPORT.md for explanation

### ⊘ SKIP Means
- Test was skipped (usually missing dependencies like valgrind)
- Not required for submission

---

## Typical Test Runs

### Before Final Submission
```bash
# Quick check
python3 requirements_validator.py ./codexion

# Comprehensive check
python3 comprehensive_tester.py ./codexion

# Memory check
valgrind --leak-check=full --error-exitcode=1 ./codexion 3 2000 100 100 100 1 50 "fifo"
```

All should show success.

### If Tests Fail
1. Run `python3 debug_tester.py` to see what's wrong
2. Check [TEST_REPORT.md](TEST_REPORT.md) for detailed explanations
3. Fix the issue
4. Recompile: `make clean && make`
5. Test again

---

## Program Arguments Reference

```
codexion <args>
```

**Arguments** (all mandatory):
1. `number_of_coders` - Number of coders (≥1)
2. `time_to_burnout` - Milliseconds before burnout (>0)
3. `time_to_compile` - Milliseconds to compile (≥1)
4. `time_to_debug` - Milliseconds to debug (≥1)
5. `time_to_refactor` - Milliseconds to refactor (≥1)
6. `number_of_compiles_required` - Compilations needed to complete (≥1)
7. `dongle_cooldown` - Milliseconds cooldown after dongle release (≥0)
8. `scheduler` - "fifo" or "edf" (required exactly)

**Example**:
```bash
./codexion 4 8000 200 200 200 2 100 "fifo"
```

---

## Files Generated

- **comprehensive_tester.py** - Full test suite
- **requirements_validator.py** - Simple requirements check
- **debug_tester.py** - Debug output generator
- **TEST_REPORT.md** - Detailed issues and fixes
- **FINAL_TEST_REPORT.md** - Summary of changes and status
- **QUICK_REFERENCE.md** - This file

All test files are standalone Python scripts - no special setup needed.

---

## Troubleshooting

### "TIMEOUT" Error
Program is deadlocking or taking too long. Check:
- Dongle cooldown not too high
- No infinite loops in your code
- Coders can actually acquire dongles

### Format Validation Fails
Your output doesn't match required format. Check:
- No extra text besides standard messages
- Each line is: `timestamp coder_id action`
- No "finished with 0 remaining compiles" messages
- No final summary message

### Memory Leaks Detected
Not freeing allocated memory. Check:
- free_monitor() is called
- All dongle queues freed
- All mutexes destroyed
- All pthread_cond_t destroyed

### Burnout Not Detected
Burnout monitor thread might have issues. Check:
- Monitor thread is created
- It's checking deadlines correctly
- It's stopping the simulation when burnout occurs
- Messages printed within 10ms of actual burnout

---

## Questions or Issues?

1. Check TEST_REPORT.md for detailed explanations
2. Run debug_tester.py to see raw output
3. Review your code against subject requirements
4. Look at example output in FINAL_TEST_REPORT.md
