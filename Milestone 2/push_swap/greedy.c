/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   greedy.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/14 15:46:49 by joshde-s          #+#    #+#             */
/*   Updated: 2026/01/16 14:19:17 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libpushswap.h"

int	cost_to_rotate(int a_indx, int b_indx, int *sizes, int *costs)
{
	init_costs(a_indx, b_indx, sizes, costs);
	if (costs[0] > 0 && costs[1] > 0)
	{
		if (costs[0] >= costs[1])
			return (costs[0]);
		return (costs[1]);
	}
	else if (costs[0] < 0 && costs[1] < 0)
	{
		if (costs[0] <= costs[1])
			return (costs[0] * -1);
		return (costs[1] * -1);
	}
	else if (costs[0] >= costs[1])
	{
		if (costs[0] > 0)
			return (costs[0]);
		return (costs[0] * -1);
	}
	else if (costs[1] > 0)
		return (costs[1]);
	return (costs[1] * -1);
}

int	get_best_indx(int *norm, int alen, int b_val)
{
	int	i;
	int	curr_small;
	int	curr_big;
	int	big_indx;

	i = 0;
	big_indx = init_best_index(norm, &curr_small, &curr_big, alen);
	if (b_val < curr_small || b_val > curr_big)
		return ((big_indx + 1) % alen);
	while (i < alen - 1)
	{
		if (norm[i] < b_val && b_val < norm[i + 1])
			return (i + 1);
		i++;
	}
	return (0);
}

void	get_cheapest_move(int *norm, int *stackb, int *sizes, int *best_costs)
{
	int	i;
	int	mincost;
	int	temp_costs[3];
	int	a_indx;
	int	value;

	i = 0;
	mincost = 2147483647;
	while (i < sizes[1])
	{
		value = stackb[i];
		a_indx = get_best_indx(norm, sizes[0], value);
		temp_costs[2] = cost_to_rotate(a_indx, i, sizes, temp_costs);
		if (temp_costs[2] < mincost)
		{
			mincost = temp_costs[2];
			best_costs[0] = temp_costs[0];
			best_costs[1] = temp_costs[1];
		}
		i++;
	}
}

void	rotate_to_values(int *norm, int *stackb, int*sizes, int*costs)
{
	while (costs[0] > 0 && costs[1] > 0)
	{
		rotate_both(norm, sizes[0], stackb, sizes[1]);
		costs[0]--;
		costs[1]--;
	}
	while (costs[0] > 0)
	{
		rotate_a(norm, sizes[0]);
		costs[0]--;
	}
	while (costs[1] > 0)
	{
		rotate_b(stackb, sizes[1]);
		costs[1]--;
	}
}

void	greedy(int *norm, int *alen, int *stackb, int *blen)
{
	int	costs[2];
	int	sizes[2];
	int	direction;

	while (*blen > 0)
	{
		sizes[0] = *alen;
		sizes[1] = *blen;
		get_cheapest_move(norm, stackb, sizes, costs);
		rotate_to_values(norm, stackb, sizes, costs);
		rev_rotate_to_values(norm, stackb, sizes, costs);
		pushtoa(norm, alen, stackb, blen);
	}
	if (norm[0] < (*alen / 2))
		direction = -1;
	else
		direction = 1;
	while (norm[0] != 0)
	{
		if (direction == 1)
			rotate_a(norm, *alen);
		else
			rev_rotate_a(norm, *alen);
	}
}
