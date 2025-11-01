/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/13 14:30:26 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/18 11:23:44 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

int	ft_ultimate_range(int **range, int min, int max)
{
	int	i;

	i = 0;
	if (min >= max)
	{
		*range = NULL;
		return (0);
	}
	if (max < -2147483648 || min > 2147483647)
		return (-1);
	*range = malloc((max - min) * 4);
	while (min < max)
	{
		(*range)[i] = min;
		min++;
		i++;
	}
	return (i);
}

//int	main(void)
//{
//	int	*array;
//	int	min;
//	int	max;
//	int	size;
//
//	min = -3;
//	max = 3;
//	size = ft_ultimate_range(&array, min, max);
//	printf("The size of the array is: %i", size);
//	return (0);
//}
