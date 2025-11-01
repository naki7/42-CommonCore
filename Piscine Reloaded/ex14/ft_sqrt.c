/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 15:37:26 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/10 12:27:38 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_sqrt(int nb)
{
	long int	root;

	if (nb > 10000)
		root = nb / 16;
	if (nb > 1000)
		root = nb / 8;
	else if (nb > 100)
		root = nb / 4;
	else
		root = nb / 2;
	if (nb < 1)
		return (0);
	if (nb == 1)
		return (1);
	while (root > 0)
	{
		if (nb == (root * root))
			return (root);
		root--;
	}
	return (0);
}

//int	main(void)
//{
//	int	num;
//	int	result;
//
//	num = 2089312681;
//	result = ft_sqrt(num);
//	printf("%i", result);
//	return (0);
//}
