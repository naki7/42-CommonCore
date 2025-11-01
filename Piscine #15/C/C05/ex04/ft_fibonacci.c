/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_fibonacci.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/10 21:59:52 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/11 09:48:39 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_fibonacci(int index)
{
	if (index < 0)
		return (-1);
	if (index > 1)
		index = ft_fibonacci(index - 1) + ft_fibonacci(index - 2);
	return (index);
}

//int	main(void)
//{
//	int	indx;
//	int	result;
//
//	indx = 10; 
//	result = ft_fibonacci(indx);
//	printf("At the %i index, ", indx);
//	printf("the element is: %i", result);
//	return (0);
//}
