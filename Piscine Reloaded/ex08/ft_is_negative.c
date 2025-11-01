/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_negative.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 10:55:01 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/07 16:07:13 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c);
//void	ft_putchar(char c)
//{
//	write(1, &c, 1);
//}

void	ft_is_negative(int n)
{
	if (n < 0)
		ft_putchar('N');
	else
		ft_putchar('P');
}

//int	main(void)
//{
//	int	n;
//
//	n = -1241;
//	ft_is_negative(0);
//	return (0);
//}
