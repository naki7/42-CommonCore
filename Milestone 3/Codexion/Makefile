# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/22 09:49:55 by joshde-s          #+#    #+#              #
#    Updated: 2026/06/22 12:40:42 by joshde-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = codexion

CC = cc
CFLAGS = -Wall -Wextra -Werror
COMPILE = $(CC) $(CFLAGS)

CFILES = close_gracefully.c coder_actions.c coder_creator.c coder_manager.c \
		codexion.c dongle_manager.c infrastructure_builder.c \
		monitor_manager.c parser.c
OBJS = $(CFILES:.c=.o)

RM = rm -fr

all: $(NAME)

$(NAME): $(OBJS)
		$(COMPILE) $(OBJS) -o $(NAME)

easy:
		./$(NAME) 2 1000 200 200 200 3 50 "fifo"

medium:
		./$(NAME) 5 1200 250 200 200 5 100 "fifo"

hard:
		./$(NAME) 10 954 220 150 150 10 97 "fifo"

edf:
		./$(NAME) 15 620 120 120 120 15 80 "edf"

one_coder:
		./$(NAME) 1 800 200 200 200 1 50 "fifo"

burnout:
		./$(NAME) 5 100 200 200 200 3 50 "fifo"

no_cooldown:
		./$(NAME) 5 1000 200 200 200 5 0 "fifo"

large_cooldown:
		./$(NAME) 5 10000 100 100 100 3 1000 "edf"

all_tests:
		echo "running a simple test first" | sleep 5
		$(MAKE) easy
		echo "running a more difficult test next" | sleep 5
		$(MAKE) medium
		echo "running running a really hard test next" | sleep 5
		$(MAKE) hard
		echo "running an edf test with tight constraints next" | sleep 5
		$(MAKE) edf
		echo "running with 1 coder next" | sleep 5
		$(MAKE) one_coder
		echo "running a definite burnout test next" | sleep 5
		$(MAKE) burnout
		echo "running with no dongle cooldown next" | sleep 5
		$(MAKE) no_cooldown
		echo "running with a large cooldown next" | sleep 5
		$(MAKE) large_cooldown

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
