/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/01 17:38:06 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/01 17:54:23 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

void	ft_ultimate_div_mod(int *a, int *b)
{
	int	a_holder;
	int	b_holder;

	a_holder = *a;
	b_holder = *b;
	*a = a_holder / b_holder;
	*b = a_holder % b_holder;
}

//int main(void)
//{
//	int	num1;
//	int	num2;
//
//	num1 = 25;
//	num2 = 7;
//	printf("a was %i ", num1);
//	printf("b was %i ", num2);
//	ft_ultimate_div_mod(&num1, &num2);
//	printf("a is now %i ", num1);
//	printf("b is now %i", num2);
//	return (0);
//}
