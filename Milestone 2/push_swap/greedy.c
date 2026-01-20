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
#include <stdio.h>

int	cost_to_rotate(int a_indx, int b_indx, int *sizes, int *costs)
{
	if (a_indx > (sizes[0] / 2))
		costs[0] = a_indx - sizes[0];
	else
		costs[0] = a_indx;
	if (b_indx > (sizes[1] / 2))
		costs[1] = b_indx - sizes[1];
	else
		costs[1] = b_indx;
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
	int small_indx;
	int curr_big;
	int	big_indx;

	i = 0;
	curr_small = norm[0];
	curr_big = norm[0];
	small_indx = 0;
	big_indx = 0;
	while (i < alen)
	{
		if (norm[i] < curr_small)
		{
			curr_small = norm[i];
			small_indx = i;
		}
		if (norm[i] > curr_big)
		{
			curr_big = norm[i];
			big_indx = i;
		}
		i++;
	}
	if (b_val < curr_small || b_val > curr_big)
		return ((big_indx + 1) % alen);
	i = 0;
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
	while (costs[0] < 0 && costs[1] < 0)
	{
		rev_rotate_both(norm, sizes[0], stackb, sizes[1]);
		costs[0]++;
		costs[1]++;
	}
	while (costs[0] < 0)
	{
		rev_rotate_a(norm, sizes[0]);
		costs[0]++;
	}
	while (costs[1] < 0)
	{
		rev_rotate_b(stackb, sizes[1]);
		costs[1]++;
	}
}

void	greedy(int *norm, int *alen, int *stackb, int *blen)
{
	int	costs[2];
	int	sizes[2];

	while (*blen > 0)
	{
		sizes[0] = *alen;
		sizes[1] = *blen;
		get_cheapest_move(norm, stackb, sizes, costs);
		rotate_to_values(norm, stackb, sizes, costs);
		pushtoa(norm, alen, stackb, blen);
	}
	while (norm[0] != 0)
	{
		//if (norm[0] < (*alen / 2))
			rotate_a(norm, *alen);
		//else
			//rev_rotate_a(norm, *alen);
	}
}
