# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 09:20:55 by joshde-s          #+#    #+#              #
#    Updated: 2025/12/08 09:48:26 by joshde-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap

CC = cc
CFLAGS = -Wall -Wextra -Werror
COMPILE = $(CC) $(CFLAGS)

CFILES = push_swap.c stack_funcs.c ft_atoi.c ft_split.c ft_strchr.c ft_strlcpy.c ft_strlen.c swap.c push.c rotate.c reverse.c radix.c largesort.c greedy.c large_utils.c radix_utils.c
OBJS = $(CFILES:.c=.o)

RM = rm -f

all: $(NAME)

$(NAME): $(OBJS)
	$(COMPILE) $(OBJS) -o $(NAME)

HUND_MIN := 1
HUND_MAX := 100

FIVE_MAX:= 500

test_both: test_hundred test_five

test_hundred: num_hundred check_hundred

num_hundred:
	ARGS=$$(shuf -i "$(HUND_MIN)-$(HUND_MAX)" -n 100); \
	./$(NAME) $$ARGS | wc -l

check_hundred:
	ARGS=$$(shuf -i "$(HUND_MIN)-$(HUND_MAX)" -n 100); \
	./$(NAME) $$ARGS | ./checker_linux $$ARGS

test_five: num_five check_five

num_five:
	ARGS=$$(shuf -i "$(HUND_MIN)-$(FIVE_MAX)" -n 500); \
	./$(NAME) $$ARGS | wc -l

check_five:
	ARGS=$$(shuf -i "$(HUND_MIN)-$(FIVE_MAX)" -n 500); \
	./$(NAME) $$ARGS | ./checker_linux $$ARGS

clean:
	$(RM) $(OBJS) #$(BOBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
