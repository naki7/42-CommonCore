/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/01 14:38:25 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/01 17:33:25 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

void	ft_swap(int *a, int *b)
{
	int	holder_a;
	int	holder_b;

	holder_a = *a;
	holder_b = *b;
	*a = holder_b;
	*b = holder_a;
}

//int	main(void)
//{
//	int	first_num;
//	int	second_num;
//	int	*first_ptr;
//	int	*second_ptr;
//
//	first_num = 1;
//	second_num = 2;
//	first_ptr = &first_num;
//	second_ptr = &second_num;
//	printf("first: %i, ", first_num);
//        printf("second: %i", second_num);
//	ft_swap(first_ptr, second_ptr);
//	printf("first: %i, ", first_num);
//	printf("second: %i", second_num);
//}
