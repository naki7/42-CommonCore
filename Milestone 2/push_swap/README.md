*This project has been created as part of the 42 curriculum by joshde-s*

# Push_Swap

## Description

Push_Swap is a sorting algorithm project that sorts a stack of integers using two stacks (A and B) with a limited set of operations. The goal is to find the most efficient sequence of operations to sort stack A in ascending order while minimizing the total number of moves.

### Problem Overview

Given a stack of random integers, you must:
- Sort the integers in ascending order in stack A
- Use only two stacks: A (source) and B (auxiliary)
- Use only these operations:
  - **sa/sb**: Swap the first two elements of stack A or B within themselves
  - **ss**: Swap the first two elements of both stacks
  - **pa/pb**: Push the first element from stack B to A or from stack A to B
  - **ra/rb**: Rotate stack A or B upwards (first element goes to bottom)
  - **rr**: Rotate both stacks upwards
  - **rra/rrb**: Reverse rotate stack A or B (last element goes to top)
  - **rrr**: Reverse rotate both stacks

## How It Works

### Features

This implementation includes multiple sorting strategies to optimize for different input sizes:

- **Input Validation**: Validates integer range (INT_MIN to INT_MAX) and checks for duplicates
- **Stack Normalization**: Converts unsorted values to their rank indices for efficient processing
- **Radix Sort**: Used for smaller datasets and then used in part for larger datasets just to give a small sorting boost(optimized bit-by-bit sorting)
- **Longest Increasing Subsequence (LIS) + Greedy Algorithm**: Used for medium-sized inputs
  - Finds the longest increasing subsequence to minimize unnecessary rotations
  - Uses a greedy approach to place remaining elements optimally by verifying how many rotation operations it would cost per stack push into stack a

### Algorithm Flow

1. **Input Validation**
   - Validate that all arguments are valid integers within INT_MIN to INT_MAX
   - Check for duplicate values
   - Handle error cases gracefully

2. **Stack Normalization**
   - Create a mapping of original values to their sorted indices
   - This reduces complexity and works with cleaner integer ranges

3. **Sorting Strategy Selection**
   - For small stacks (≤ 5 elements): Use simple operations through Radix alone
   - For larger stacks: Use LIS + Greedy algorithm

4. **Operation Execution**
   - Execute the optimal sequence of operations
   - Output each operation to stdout

### Project Files

- **push_swap.c**: Main program, argument parsing, and dispatcher
- **stack_funcs.c**: Stack utility functions
- **radix.c**: Radix sort implementation
- **largesort.c**: LIS algorithm for finding longest increasing subsequence
- **greedy.c**: Greedy algorithm for optimal element placement
- **swap.c, push.c, rotate.c, reverse.c**: Operation implementations
- **large_utils.c, radix_utils.c**: Helper functions for sorting algorithms
- **libpushswap.h**: Header file with function declarations
- **libft.h**: Custom C library utilities (ft_atoi, ft_split, ft_strchr, ft_strlen, ft_strlcpy)

### Complexity Analysis

- **Small inputs (n ≤ 5)**: O(n) operations
- **Medium inputs (radix + LIS)**: O(n + k) where k is based on bit length
- **Theoretical minimum**: O(n log n) comparisons (information-theoretic lower bound)

## Instructions

### Build

```bash
make
```

This compiles the program and creates a `push_swap` executable.

### Running

```bash
./push_swap 4 67 3 87 23
```

Output is a sequence of operations needed to sort stack A:
```
ra
pb
rra
...
```

### Verification

To verify the output, pipe to a checker program:

```bash
./push_swap 4 67 3 87 23 | wc -l  # Count number of operations
./push_swap 4 67 3 87 23 | ./checker_linux 4 67 3 87 23 # Checks if operations
#applied to stack results in a sorted stack - either OK or KO as output
```

### Testing

The Makefile includes test targets and normal 42 subject Makefile calls:

```bash
make				# Can take arguments of all, push_swap, clean, fclean, re
# only use the bellow if the push_swap program has been compiled and the checker_linux program has been included
make test_hundred   # Test with 100 random numbers (1-100 range)
make test_five      # Test with 500 random numbers (1-500 range)
make test_both      # Run both tests
# These run the checker with the compiled program but does not produce the operation count like above
make check_hundred	# same as ./push_swap $ARG | ./checker_linux $ARG (ARG is 100 random numbers (1-100 range))
make check_five	# same as ./push_swap $ARG | ./checker_linux $ARG (ARG is 500 random numbers (1-500 range))
# the bellow can be checked with just the push_swap program being compiled
make num_hundred	# Runs the program with 100 random numbers (1-100 range) and then uses | wc -l
make num_five		# Runs the program with 500 random numbers (1-500 range) and then uses | wc -l
```

## Resources

- [Sorting Algorithms](https://en.wikipedia.org/wiki/Sorting_algorithm)
  - [Radix Sort](https://en.wikipedia.org/wiki/Radix_sort)
  - [Longest Increasing Subsequence](https://en.wikipedia.org/wiki/Longest_increasing_subsequence)
  - [Greedy Algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)
- [Block Sorts](https://en.wikipedia.org/wiki/Block_sort)
- [Push Swap Visualizer](https://push.eliotlucas.ch/)

### AI Usage

*AI was used primarily as a research and trouble shooting tool. This includes cases of verifying if certain algoritms might work without working on nor gaining direct code as a result. Also in cases where bugs or issues were more difficult to find AI was used to test where edgecases were being problematic. Lastly, AI was used in assistance to help refine this README document.*
