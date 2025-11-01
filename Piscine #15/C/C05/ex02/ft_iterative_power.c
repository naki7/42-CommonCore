/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/10 21:26:10 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/10 21:46:49 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_iterative_power(int nb, int power)
{
	int	i;
	int	num;

	i = 0;
	num = nb;
	if (power < 0)
		return (0);
	if (power == 0)
		return (1);
	while (power > 1)
	{
		num *= nb;
		power --;
	}
	return (num);
}

//int	main(void)
//{
//	int	result;
//	int	number;
//	int	power;
//
//	number = 4;
//	power = 3;
//	result = ft_iterative_power(number, power);
//	printf("The number is: %i, ", number);
//	printf("the power is: %i ", power);
//	printf("and the result is: %i", result);
//}
