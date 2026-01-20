/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 20:33:14 by joshde-s          #+#    #+#             */
/*   Updated: 2026/01/05 15:23:54 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libpushswap.h"

void	swap_a(int *stack, int stklen)
{
	int	temp;

	if (stklen > 1)
	{
		temp = stack[0];
		stack[0] = stack[1];
		stack[1] = temp;
		write(1, "sa\n", 3);
	}
}

void	swap_b(int *stack, int stklen)
{
	int	temp;

	if (stklen > 1)
	{
		temp = stack[0];
		stack[0] = stack[1];
		stack[1] = temp;
		write(1, "sb\n", 3);
	}
}

void	swap_both(int *stacka, int alen, int *stackb, int blen)
{
	int	temp;

	if (alen > 1)
	{
		temp = stacka[0];
		stacka[0] = stacka[1];
		stacka[1] = temp;
	}
	if (blen > 1)
	{
		temp = stackb[0];
		stackb[0] = stackb[1];
		stackb[1] = temp;
	}
	write(1, "ss\n", 3);
}
