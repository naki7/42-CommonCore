/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radix_utils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 13:49:14 by joshde-s          #+#    #+#             */
/*   Updated: 2026/01/22 13:49:31 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libpushswap.h"

void	dup_atonorm(int *norm, int *stacka, int alen)
{
	int	i;

	i = 0;
	while (i < alen)
	{
		norm[i] = stacka[i];
		i++;
	}
}

int	check_if_ordered(int *normstack, int alen)
{
	int	i;

	i = 0;
	while (i < ((alen) - 1))
	{
		if (normstack[i] == i)
			i++;
		else
			return (0);
		if (i == ((alen) - 1))
			return (1);
	}
	return (1);
}

void	sort_three(int *norm)
{
	if (norm[0] == 2)
	{
		if (norm[1] == 1)
		{
			swap_a(norm, 3);
			rev_rotate_a(norm, 3);
		}
		else
			rotate_a(norm, 3);
	}
	else if (norm[0] == 1)
	{
		if (norm[1] == 0)
			swap_a(norm, 3);
		else
			rev_rotate_a(norm, 3);
	}
	else
	{
		swap_a(norm, 3);
		rotate_a(norm, 3);
	}
}

void	small_sort(int *norm, int *alen, int *stackb, int *blen)
{
	if (norm[0] == 2 && norm[1] == 0 && norm[2] == 3 && norm[3] == 1)
	{
		swap_a(norm, *alen);
		pushtob(stackb, blen, norm, alen);
		pushtob(stackb, blen, norm, alen);
		pushtob(stackb, blen, norm, alen);
		greedy(norm, alen, stackb, blen);
	}
	else if (norm[0] == 3 && norm[1] == 2 && norm[2] == 0 && norm[3] == 4)
	{
		rotate_a(norm, *alen);
		pushtob(stackb, blen, norm, alen);
		pushtob(stackb, blen, norm, alen);
		greedy(norm, alen, stackb, blen);
	}
	else
	{
		pushtob(stackb, blen, norm, alen);
		pushtob(stackb, blen, norm, alen);
		pushtob(stackb, blen, norm, alen);
		greedy(norm, alen, stackb, blen);
	}
}

void	free_stacks(int *stacka, int *stackb, int *normstack)
{
	free(stacka);
	free(stackb);
	free(normstack);
}
