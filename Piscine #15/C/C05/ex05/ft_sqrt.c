/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/11 09:59:08 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/11 11:26:20 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	rooter(int sqr, int num)
{
	if (sqr != num * num)
		return (1);
	return (0);
}

int	ft_sqrt(int nb)
{
	int	root;

	root = nb;
	while (root > 0 && nb != root * root)
		root -= rooter(nb, root);
	if (nb == root * root)
		return (root);
	else
		return (0);
}

//int	main(void)
//{
//	int	num;
//	int	result;
//
//	num = 64;
//	result = ft_sqrt(num);
//	printf("the square root of %i is: ", num);
//	printf("%i", result);
//	return (0);
//}
