# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/09 11:19:11 by joshde-s          #+#    #+#              #
#    Updated: 2025/10/09 19:45:17 by joshde-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
NAME = libft.a

CC = gcc
CFLAGS = -c -Wall -Wextra -Werror

all: $(NAME)

$(NAME): objectify
	ar rcs $(NAME) ft_putchar.o ft_putstr.o ft_strcmp.o ft_strlen.o ft_swap.o

objectify:
	$(CC) $(CFLAGS) ./srcs/ft_putchar.c
	$(CC) $(CFLAGS) ./srcs/ft_putstr.c
	$(CC) $(CFLAGS) ./srcs/ft_strcmp.c
	$(CC) $(CFLAGS) ./srcs/ft_strlen.c
	$(CC) $(CFLAGS) ./srcs/ft_swap.c

clean:
	rm -f ft_putchar.o ft_putstr.o ft_strcmp.o ft_strlen.o ft_swap.o

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
