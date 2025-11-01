/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/01 17:10:13 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/01 17:34:38 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
}

//int	main(void)
//{
//	int	a_var;
//	int	b_var;
//	int	divided;
//	int	modular;
//
//	a_var = 16;
//	b_var = 9;
//	ft_div_mod(a_var, b_var, &divided, &modular);
//	printf("a= %i ", a_var);
//	printf("b= %i ", b_var);
//	printf("div= %i ", divided);
//	printf("mod= %i ", modular);
//	return (0);
//}
