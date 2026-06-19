# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/22 09:49:55 by joshde-s          #+#    #+#              #
#    Updated: 2026/06/19 11:52:52 by joshde-s         ###   ########.fr        #
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

test: $(OBJS)
		$(CC) $(OBJS) -o $(NAME)
		./$(NAME) 3 1200 200 200 200 7 100 "fifo"

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
