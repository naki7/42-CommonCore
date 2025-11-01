/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/12 21:56:21 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/16 11:25:50 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

int	*ft_range(int min, int max)
{
	int	*ints;
	int	i;

	i = 0;
	if (min >= max)
		return (NULL);
	ints = malloc((max - min) * 4);
	while (min < max)
	{
		ints[i] = min;
		min++;
		i++;
	}
	return (ints);
}

//int	main(void)
//{
//	int	i;
//	int	small;
//	int	big;
//	int	*array;
//
//	i = 0;
//	small = 7;
//	big = 16;
//	array = malloc((big - small) * 4);
//	array = ft_range(small, big);
//	if (array == NULL)
//	{
//		printf("NULL");
//		return (0);
//	}
//	while (array[i])
//	{
//		printf("%i, ", array[i]);
//		i++;
//	}
//	return(0);
//}
