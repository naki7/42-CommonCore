/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 20:33:56 by joshde-s          #+#    #+#             */
/*   Updated: 2026/01/06 11:50:38 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libpushswap.h"

void	rotate_a(int *stack, int len)
{
	int	i;
	int	temp;

	i = 0;
	temp = stack[0];
	len--;
	while (i < len)
	{
		stack[i] = stack[i + 1];
		i++;
	}
	stack[len] = temp;
	write(1, "ra\n", 3);
}

void	rotate_b(int *stack, int len)
{
	int	i;
	int	temp;

	i = 0;
	temp = stack[0];
	len--;
	while (i < len)
	{
		stack[i] = stack[i + 1];
		i++;
	}
	stack[len] = temp;
	write(1, "rb\n", 3);
}

void	rotate_both(int *stacka, int alen, int *stackb, int blen)
{
	int	i;
	int	temp;

	i = 0;
	temp = stacka[0];
	alen--;
	while (i < alen)
	{
		stacka[i] = stacka[i + 1];
		i++;
	}
	stacka[alen] = temp;
	i = 0;
	temp = stackb[0];
	blen--;
	while (i < blen)
	{
		stackb[i] = stackb[i + 1];
		i++;
	}
	stackb[blen] = temp;
	write(1, "rr\n", 3);
}
