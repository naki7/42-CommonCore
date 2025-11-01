/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/10 21:47:50 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/10 21:58:49 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_recursive_power(int nb, int power)
{
	if (power < 0)
		return (0);
	if (power == 0)
		return (1);
	if (power > 1)
		nb *= ft_recursive_power(nb, power -1);
	return (nb);
}

//int	main(void)
//{
//	int	number;
//	int	power;
//	int	result;
//
//	number = 4;
//	power = 2;
//	result = ft_recursive_power(number, power);
//	printf("The number is: %i, ", number);
//	printf("the power is: %i, ", power);
//	printf("the result is: %i, ", result);
//	return (0);
//}
