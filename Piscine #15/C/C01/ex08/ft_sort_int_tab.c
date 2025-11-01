/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_int_tab.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/02 12:15:18 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/02 16:07:26 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	swap(int *arr, int a, int b)
{
	int	holder;

	holder = arr[a];
	arr[a] = arr[b];
	arr[b] = holder;
}

void	ft_sort_int_tab(int *tab, int size)
{
	int	i;
	int	j;

	i = 0;
	while (i < size)
	{
		j = i + 1;
		while (j < size)
		{
			if (tab[i] > tab[j])
			{
				swap(tab, i, j);
			}
			j++;
		}
		i++;
	}
}

//int	main(void)
//{
//	int	array[] = {52, 16, 7, 43, 34, 61, 25};
//	int	length;
//	int	count;
//
//	length = 7;
//	count = 0;
//	printf("OG array: ");
//	while(count < length)
//	{
//		printf("%i ", array[count]);
//		count++;
//	}
//	ft_sort_int_tab(array, length);
//	count = 0;
//	printf(" - Sorted array: ");
//        while(count < length)
//        {
//                printf("%i ", array[count]);
//                count++;
//        }
//	return (0);
//}
