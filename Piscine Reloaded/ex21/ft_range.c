/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 11:00:47 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/10 11:02:58 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

int	*ft_range(int min, int max)
{
	int	*arr;
	int	size;
	int	i;

	if (min >= max)
		return (NULL);
	else
	{
		size = max - min;
		arr = malloc(sizeof(int) * size);
		i = 0;
		while (i < size)
		{
			arr[i] = min + i;
			i++;
		}
	}
	return (arr);
}

//int	main(void)
//{
//	int	min;
//	int	max;
//	int	i;
//	int	*arr;
//
//	min = -7;
//	max = 16;
//	i = 0;
//	arr = ft_range(min, max);
//	if (arr == NULL)
//		printf("NULL");
//	while (i < (max - min))
//		printf("%i, ", arr[i++]);
//	free(arr);
//	return (0);
//}
