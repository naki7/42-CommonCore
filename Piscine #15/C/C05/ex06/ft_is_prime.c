/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_prime.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/11 11:27:50 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/11 16:49:04 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_is_prime(int nb)
{
	int	num;
	int	count;

	num = nb;
	count = 0;
	if (nb < 2)
		return (0);
	while (nb > 0)
	{
		if ((num % nb) == 0)
			count++;
		if (count > 2)
			return (0);
		nb--;
	}
	return (1);
}

//int	main(void)
//{
//	int	num;
//	int	result;
//
//	num = 7;
//	result = ft_is_prime(num);
//	if (result == 1)
//		printf("%i is a prime number ", num);
//	else
//		printf("%i is not a prime number ", num);
//	num = 0;
//	result = ft_is_prime(num);
//	if (result == 1)
//		printf("%i is a prime number ", num);
//	else
//		printf("%i is not a prime number ", num);
//	num = 16;
//	result = ft_is_prime(num);
//	if (result == 1)
//		printf("%i is a prime number ", num);
//	else
//		printf("%i is not a prime number ", num);
//	return (0);
//}
