# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/04 10:47:24 by joshde-s          #+#    #+#              #
#    Updated: 2025/11/04 12:49:10 by joshde-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libftprintf.a

CC = cc
CFLAGS = -Wall -Wextra -Werror

AR = ar rcs
RM = rm -f

CFILES = ft_printf.c ft_handleprint.c ft_strlen.c ft_itoa.c ft_strdup.c
OBJS = $(CFILES:.c=.o)

BFILES = ft_printf_bonus.c
BOBJS = $(BFILES:.c=.o)

ifdef BONUS
	ALLOBJS = $(OBJS) $(BOBJS)
else
	ALLOBJS = $(OBJS)
endif

all: $(NAME)

$(NAME): $(ALLOBJS)
	$(AR) $(NAME) $(ALLOBJS)

bonus:
	$(MAKE) BONUS=1

clean:
	$(RM) $(OBJS) $(BOBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re bonus
