*This project has been created as part of the 42 curriculum by joshde-s*

# Codexion

## Description

### Overview
Codexion is a multi-thread handling program. Codexion takes in the task of
	coders who use 2 dongles at a time to be able to compile their code.
	Each coder shares 2 dongles, one to their left, and one to their right.
	Each dongle is therefore used by two coders, one to its left and one to
	its right. A dongle can not be used by two coders at the same time, and
	after use the dongles immediately go on a cooldown time period. For the
	coders, once they have compiled, they will then start debugging, and
	then refactoring. After refactoring they will immediately try to compile
	their code again, thus making this process a full circle.

The multi-thread part of this project comes from the compiling threads, as
	each coder will have access to a dongle only when their thread is
	permitted to do so. However multiple coders can compile at the same time,
	as long as they are not using each others shared resources (the same dongle
	being used by another coder). If the coders can not compile their code
	before their task timer runs out, then they will be considered a burnout and
	the entire program will end. However, if each coder is able to complete the
	specified number of compiles as individuals without burning out, then the
	program completes as a success.

A scheduling process is chosen, either specifying "fifo"(First In First Out)
	or "edf" (Earliest Deadline First). The default view of the schedule is
	to be fifo, as whichever coder requests access of their dongles first, is
	the one that is given access to it once the dongle comes off cooldown. Edf
	on the other hand checks each coder to see which one has the least amount
	of time before they burnout, thus prioritizing not burning out over
	possible mistakes.
	
Coffman's conditions are made up of 4 notable instances where deadlocks can occur.
	These are related to hold & wait, preemption, circular wait, and mutual
	exclusion. These situation primarily revolve around sitautions where multiple
	coders could try to grab the same dongle at the same time, or each coder
	grabbing their left dongle at the same time, both these situations lead to
	the coders waiting indefinitely for both dongles as the other dongle they need
	will always be held by another coder thus meaning no coder will get to compile.
	
The issues on deadlock were resolved by making it so that each even number and each odd
	numbered coder takes their dongle either left first, or right first, thus giving
	each coder the time to grab both a left and right dongles before letting their
	neighbor grab theirs.

Starvation prevention is handled by releasing dongles and giving them to priority based
	on either join or deadline times. Cooldown was handled by updating each dongle's
	cooldown directly, sending it through condition to wakeup the coders and updating
	their burnout timer. Burnout was constantly tracked by a monitoring thread which
	would constantly check each coder's burnout timer ever milisecond. The log was
	also serialized through the monitor by attaching a mutex_t to it, this allowed
	the printing function to be locked and unlocked before and after each print was
	used.

Pthread_mutex_t and pthread_cond_t were both used by the dongles and the print lock.
	this was helpful as mutex is what directly gets locked and unlocked thus preventing
	other threads from using the process while using the process itself. The condition
	on the other hand would be sent out to signal to all waiting dongles, that if
	they are the next one in the heap queue to use the dongle, that they can go and
	use that process/dongle. Since the monitor is constantly aware of all coders, the
	monitor can have altered states that then will cause each coder to behave the right
	way such as stopping operations when burnout happens. This also manages the race
	condition as coders can behave as if on their own, dividing themselves base on
	even or odd identity, mean while the monitor safe runs and watches in it own thread
	along side them and only stepping in when it matters.

### Simplified
Codexion breaks individual process threads into managable pipelines by passing
	them into dongles that use mutex to lock and unlock. While locked no other
	coder can use that thread until it is unlocked. By having the right kind
	of prioritizing this unlocking system, can be optimized to make sure that
	those who need access the most, get it.

## Instructions

### Create Executable

- In the command terminal run 'make'

### Use Executable with predefined values

- Run 'make "command_here"' where "command_here" is the commands listed below:
	- "easy" - runs a simple set of arguments
	- "medium" - runs a mildly complex set of arguments
	- "hard" - runs a highly complex set of arguments that is meant to be more
		constrained
	- "edf" - runs a time constrained test with the edf scheduler, this pushes
		the schedule tester to its limit
	- "one_coder" - runs the program with only 1 coder which should after the
		burnout amount of time, result in a burnout
	- "burnout" - runs the program with a burnout time that will happen almost
		immmediately
	- "no_cooldown" - runs the program with dongle cooldown set to 0 which makes
		for a very rapid result
	- "large_cooldown" - uses a large cooldown timer for the dongles so that it
		can be easier to see when dongles cooldown
	- "valgrind_ok" - checks the program with valgrind for leaks on an easy run
	- "valgrind_burnout" - checks the program with valgrind for leaks for when it
		results in burnout
	- "valgrind_no_args" - checks the program with valgrind for leaks for when no
		arguments are used on the command line
	- "all_tests" - runs all the above commands with 5 second breaks in-between
		each run

### Utility

- 'make clean' - removes all object files
- 'make fclean' - removes all object files and the codexion executable
- 'make all' - compiles the files into an executable
- 'make re' - runs make fclean and then re-runs make

## Resources
 - [Multithreading in C](https://www.geeksforgeeks.org/c/multithreading-in-c/)
 - [Thread Management Functions in C](https://www.geeksforgeeks.org/c/thread-functions-in-c-c/)
 - [Multithreaded Programming Guide](https://docs.oracle.com/cd/E26502_01/html/E35303/tlib-1.html)

### AI usage
Primarily used for trouble shooting errors that were more difficult to find
	manually. As well as for finding recommended sources to do further
	research.
