/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_numbers.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 10:49:28 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/07 16:07:51 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c);
//void	ft_putchar(char c)
//{
//	write(1, &c, 1);
//}

void	ft_print_numbers(void)
{
	char	n;

	n = 48;
	while (n < 58)
	{
		ft_putchar(n);
		n++;
	}
}

//int	main(void)
//{
//	ft_print_numbers();
//	return (0);
//}
