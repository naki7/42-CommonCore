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
AR = ar rcs

CFILES = 
OBJS = $(CFILES:.c=.o)
#BFILES = 
#BOBJS = $(BFILES:.c=.o)

RM = rm -f

#ifdef BONUS
#	ALLOBJS = $(OBJS) $(BOBJS)
#else
#	ALLOBJS = $(OBJS)
#endif

all: $(NAME)

$(NAME): $(ALLOBJS)
	$(COMPILE) $(ALLOBJS) -o $(NAME)

#bonus:
#	$(MAKE) BONUS=1

clean:
	$(RM) $(OBJS) #$(BOBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re #bonus
