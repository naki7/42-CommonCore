/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/10 20:22:54 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/10 21:22:05 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_iterative_factorial(int nb)
{
	int	num;

	num = nb;
	if (nb < 0)
		return (0);
	if (nb == 0)
		return (1);
	while (nb > 1)
	{
		nb--;
		num *= nb;
	}
	return (num);
}

//int	main(void)
//{
//	int	num;
//	int	result;
//
//	num = 5;
//	result = ft_iterative_factorial(num);
//	printf("!%i = ", num);
//	printf("%i", result);
//	return (0);
//}
