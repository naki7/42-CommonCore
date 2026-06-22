# Codexion Test Report & Issues Found

## Summary
Your program is **78% passing** (14/19 tests) with **5 critical failures** that need to be fixed to meet subject requirements.

### ✓ Passing Tests (14)
- Compilation with flags ✓
- Argument validation ✓
- Single coder execution ✓
- Valid state transitions ✓
- Monotonic timestamps ✓
- No message interleaving ✓
- Burnout detection timing ✓
- Completion condition ✓
- Memory leak check (valgrind) ✓

### ✗ Failing Tests (5)
1. **Log format validation** - 1 malformed line
2. **Compile sequence** - 2 violations
3. **FIFO scheduling** - Format errors
4. **EDF scheduling** - Format errors
5. **High contention** - 3 sequence violations

---

## Detailed Issues

### Issue #1: Invalid Final Message Format
**Severity**: HIGH (Subject Requirement Violation)

**Location**: [codexion.c](codexion.c#L25)

**Problem**: 
The program outputs `"All coders compiled successfully!"` which does NOT match the required log format.

**Current Output**:
```
2303 2 finished with 0 remaining compiles
All coders compiled successfully!    ← INVALID FORMAT
```

**Required Format** (per subject):
```
timestamp_in_ms X has taken a dongle
timestamp_in_ms X is compiling
timestamp_in_ms X is debugging
timestamp_in_ms X is refactoring
timestamp_in_ms X burned out
```

**Solution**: 
Remove the `"All coders compiled successfully!\n"` line from [codexion.c](codexion.c#L25). The program should only output messages in the standardized format.

**Subject Quote**: 
> "Any state change of a coder must be formatted as follows: timestamp_in_ms X [action]"

---

### Issue #2: Compile Sequence Violations - Missing Consecutive Dongle Messages

**Severity**: HIGH (Subject Requirement Violation)

**Locations**: Lines 6, 15 in test output (and similar in high contention)

**Problem**:
The requirement states that every `is compiling` message must be **immediately preceded** by exactly 2 `has taken a dongle` messages from the same coder. Currently, there are cases where this doesn't happen due to output interleaving.

**Current Output**:
```
400 1 is debugging           ← Line 4: Different coder
401 3 has taken a dongle     ← Line 5: Coder 3
401 3 is compiling           ← Line 6: Coder 3 - VIOLATION! Preceded by debug, not 2 dongles
```

Expected:
```
401 3 has taken a dongle     ← Line 4
401 3 has taken a dongle     ← Line 5
401 3 is compiling           ← Line 6
```

**Root Cause**:
Race condition in output serialization. While the mutex prevents text corruption, it doesn't prevent legitimate concurrency from causing messages to interleave. The "finished with 0 remaining compiles" messages are being printed, which is adding extra lines.

**Solution Options**:

**Option A** (Recommended): Remove custom "finished" messages
- Only use the standard log messages per subject requirements
- Don't print "finished with 0 remaining compiles" - this isn't a required action
- The completion is already indicated when all coders have compiled the required times

**Option B**: Ensure strict message bundling
- When a coder acquires both dongles and starts compiling, ensure all 3 messages are printed together without any other coder's messages in between
- This requires more careful synchronization in the print logic

**Subject Quote**:
> "A displayed state message should not be mixed up with another message."

---

### Issue #3: State in Incorrect Context

**Severity**: MEDIUM

**Problem**:
In [coder_actions.c](coder_actions.c#L56-L59), coders print "finished with 0 remaining compiles" when `remaining_compiles < 1`. However:

1. This message doesn't match the required format
2. It's internal state info, not an "action" that should be logged per subject
3. It can appear in the middle of another coder's sequence

**Suggested Fix**:
Remove this debug message entirely. The completion is already tracked by the monitor checking `monitor->remaining_compiles`.

---

## Detailed Test Output Analysis

### Test Case 1: Basic Functionality (3 coders, FIFO, 2 compiles each)

**Raw Output**:
```
0 1 has taken a dongle        ✓ OK
0 1 has taken a dongle        ✓ OK
0 1 is compiling              ✓ OK
0 3 has taken a dongle        ✓ OK
400 1 is debugging            ✓ OK
401 3 has taken a dongle      ✓ OK
401 3 is compiling            ✓ ISSUE: Should be preceded by 2 dongle messages
401 3 is debugging            ✗ Wrong timing? (should be 601)
...
1201 1 finished with 0 remaining compiles   ✗ Invalid format
...
2303 2 finished with 0 remaining compiles   ✗ Invalid format
All coders compiled successfully!            ✗ Invalid format & non-standard
```

**Violations Found**:
1. Extra "finished with..." messages (appears to be your own instrumentation)
2. Final summary message doesn't follow format

---

## Recommendations for Fixing

### Priority 1: Critical Failures (MUST FIX)

1. **Remove non-standard messages from [codexion.c](codexion.c#L25)**
   - Delete: `printf("All coders compiled successfully!\n");`
   - The program should exit silently or just return success

2. **Remove "finished with 0 remaining compiles" messages**
   - Delete from [coder_actions.c](coder_actions.c#L53-L55)
   - This isn't a required action per subject spec
   - It's internal state, not a "state change of a coder"

3. **Verify output is exactly matching format**
   - Each line: `timestamp coder_id action`
   - Allowed actions: `has taken a dongle`, `is compiling`, `is debugging`, `is refactoring`, `burned out`
   - Nothing else

### Priority 2: Verification

After making changes, re-run tests:
```bash
python3 comprehensive_tester.py ./codexion
```

All tests should show **✓ PASS**

---

## Test Requirements from Subject

From Chapter VI - Mandatory Part:

✓ Each coder is a thread
✓ Circular arrangement with dongles (implemented)
✓ Mutex protection per dongle (implemented)
✓ Cooldown after release (implemented)
✓ Fair arbitration - FIFO/EDF (implemented)
✓ Monitor thread for burnout detection (implemented)
✓ Liveness guarantee (implemented)
✓ Serialized logging (mostly - see issues)
✓ Stops on burnout OR completion (implemented)
✓ Compiles with required flags ✓
✓ Priority queue for scheduling (needs verification)
✓ No memory leaks ✓

---

## Subject Log Format Requirements

From Chapter V - Global Rules:

```
About the logs of your program:
• Any state change of a coder must be formatted as follows:
  - timestamp_in_ms X has taken a dongle
  - timestamp_in_ms X is compiling
  - timestamp_in_ms X is debugging
  - timestamp_in_ms X is refactoring
  - timestamp_in_ms X burned out
  
• A displayed state message should not be mixed up with another message.
• A message announcing that a coder burned out should be displayed no more 
  than 10 ms after the actual burnout.
```

Your program's current extra messages violate the first requirement.

---

## How to Use the Test Suite

1. **Comprehensive Test** (recommended):
   ```bash
   python3 comprehensive_tester.py ./codexion
   ```
   Shows all test categories and a summary

2. **Debug Test** (detailed output):
   ```bash
   python3 debug_tester.py
   ```
   Shows exact lines causing failures

3. **Manual Test** (specific case):
   ```bash
   ./codexion 3 5000 200 200 200 2 100 "fifo"
   ```

---

## Next Steps

1. ✏️ Apply the fixes mentioned in Priority 1
2. 🔨 Recompile: `make clean && make`
3. 🧪 Run tests: `python3 comprehensive_tester.py ./codexion`
4. ✅ Verify all tests pass
5. 📝 Ensure README.md meets all requirements from Chapter VII
