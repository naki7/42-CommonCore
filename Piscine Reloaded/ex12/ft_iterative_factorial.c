/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 11:31:21 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/07 11:51:47 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_iterative_factorial(int nb)
{
	long int	total;

	if (nb < 0)
		return (0);
	total = 1;
	while (nb > 0)
	{
		if ((total * nb) > 2147483647)
			return (0);
		total = total * nb;
		nb--;
	}
	return (total);
}

//int	main(void)
//{
//	int	num;
//	int	result;
//
//	num = 7;
//	result = ft_iterative_factorial(num);
//	printf("%i", result);
//	return (0);
//}
