/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 11:21:10 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/07 11:30:08 by joshde-s         ###   ########.fr       */
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
//	int	a;
//	int	b;
//	int	div;
//	int	mod;
//
//	a = 16;
//	b = 7;
//	div = 0;
//	mod = 0;
//	ft_div_mod(a, b, &div, &mod);
//	printf("a = %i; b = %i; div = %i; mod = %i", a, b, div, mod);
//	return(0);
//}
