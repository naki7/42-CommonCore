# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/10 14:32:52 by joshde-s          #+#    #+#              #
#    Updated: 2025/10/10 15:03:44 by joshde-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
NAME = ft_display_file

CC = gcc
CFLAGS = -Wall -Wextra -Werror

all: $(NAME)

$(NAME): objectify
	$(CC) $(CFLAGS) ft_display_file.o -o $(NAME)

objectify:
	$(CC) -c $(CFLAGS) ft_display_file.c
clean:
	rm -f ft_display_file.o

fclean: clean
	rm -f $(NAME)

.PHONY: all clean fclean
