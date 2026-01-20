/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverse.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 20:34:17 by joshde-s          #+#    #+#             */
/*   Updated: 2026/01/06 16:26:47 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libpushswap.h"

void	rev_rotate_a(int *stack, int len)
{
	int	i;
	int	temp;

	len--;
	i = len;
	temp = stack[len];
	while (i > 0)
	{
		stack[i] = stack[i - 1];
		i--;
	}
	stack[0] = temp;
	write(1, "rra\n", 4);
}

void	rev_rotate_b(int *stack, int len)
{
	int	i;
	int	temp;

	len--;
	i = len;
	temp = stack[len];
	while (i > 0)
	{
		stack[i] = stack[i - 1];
		i--;
	}
	stack[0] = temp;
	write(1, "rrb\n", 4);
}

void	rev_rotate_both(int *stacka, int alen, int *stackb, int blen)
{
	int	i;
	int	temp;

	alen--;
	i = alen;
	temp = stacka[alen];
	while (i > 0)
	{
		stacka[i] = stacka[i - 1];
		i--;
	}
	stacka[0] = temp;
	blen--;
	i = blen;
	temp = stackb[blen];
	while (i > 0)
	{
		stackb[i] = stackb[i - 1];
		i--;
	}
	stackb[0] = temp;
	write(1, "rrr\n", 4);
}
