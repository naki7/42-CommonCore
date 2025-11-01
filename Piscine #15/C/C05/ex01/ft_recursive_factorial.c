/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/10 21:14:23 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/10 21:23:48 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_recursive_factorial(int nb)
{
	if (nb < 0)
		return (0);
	if (nb > 1)
		nb *= ft_recursive_factorial(nb - 1);
	if (nb == 0)
		return (1);
	return (nb);
}

//int	main(void)
//{
//	int	num;
//	int	result;
//
//	num = 5;
//	result = ft_recursive_factorial(num);
//	printf("!%i = ", num);
//	printf("%i", result);
//	return (0);
//}
