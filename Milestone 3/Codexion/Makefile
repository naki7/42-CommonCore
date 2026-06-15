# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/22 09:49:55 by joshde-s          #+#    #+#              #
#    Updated: 2026/06/15 15:33:21 by joshde-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = codexion

CC = cc
CFLAGS = -Wall -Wextra -Werror
COMPILE = $(CC) $(CFLAGS)

CFILES = coder_actions.c codexion.c infrastructure_builder.c parser.c dongle_manager.c monitor_manager.c close_gracefully.c
OBJS = $(CFILES:.c=.o)

RM = rm -fr

all: $(NAME)

$(NAME): $(OBJS)
		$(COMPILE) $(OBJS) -o $(NAME)

test: $(OBJS)
		$(CC) $(OBJS) -o $(NAME)
		./$(NAME) 5 2000 400000 500000 60000 7 80000 "fifo"

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
