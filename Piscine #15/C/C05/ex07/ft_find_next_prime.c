/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_find_next_prime.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/11 16:50:38 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/17 15:31:52 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	check_prime(int nb, int num, int count)
{
	if (count > 2)
		return (0);
	if (num == 0)
		return (nb);
	if ((nb % num) == 0)
		return (check_prime(nb, num - 1, count + 1));
	else
		return (check_prime(nb, num - 1, count));
}

int	ft_find_next_prime(int nb)
{
	int	found;

	found = 0;
	if (nb <= 2)
		return (2);
	found = check_prime(nb, nb, 0);
	if (found == 0 && nb < 2147483647)
		return (ft_find_next_prime(nb + 1));
	else
		return (nb);
}

//int	main(void)
//{
//	int	num;
//	int	result;
//
//	num = 98;
//	result = ft_find_next_prime(num);
//	printf("The next prime number for %i : ", num);
//	printf("is: %i... wait 101?!... that is the dalmation movie!", result);
//	return (0);
//}
