/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/01 21:54:59 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/02 14:39:05 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_rev_int_tab(int *tab, int size)
{
	int	temp_int;
	int	start_count;
	int	size_count;

	start_count = 0;
	size_count = size - 1;
	while (size_count > start_count)
	{
		temp_int = tab[start_count];
		tab[start_count] = tab[size_count];
		tab[size_count] = temp_int;
		start_count++;
		size_count--;
	}
}

//int	main(void)
//{
//	int	integers[] = {7, 16, 25, 34, 43, 52, 61};
//	int	length;
//	int	count;
//
//	length = 7;
//	count = 0;
//	printf("array was: ");
//	while(count < length)
//        {
//                printf("%i ", integers[count]);
//                count++;
//        }
//	ft_rev_int_tab(integers, length);
//	count = 0;
//	printf("- array is now: ");
//	while(count < length)
//	{
//		printf("%i ", integers[count]);
//		count++;
//	}
//	return (0);
//}
