/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   large_utils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 12:48:09 by joshde-s          #+#    #+#             */
/*   Updated: 2026/01/22 12:48:39 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libpushswap.h"

void	rev_rotate_to_values(int *norm, int *stackb, int*sizes, int*costs)
{
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

int	init_best_index(int *norm, int *curr_small, int *curr_big, int alen)
{
	int	i;
	int	indx;

	i = 0;
	indx = 0;
	while (i < alen)
	{
		if (norm[i] < *curr_small)
			*curr_small = norm[i];
		if (norm[i] > *curr_big)
		{
			*curr_big = norm[i];
			indx = i;
		}
		i++;
	}
	return (indx);
}

void	init_costs(int a_indx, int b_indx, int *sizes, int *costs)
{
	if (a_indx > (sizes[0] / 2))
		costs[0] = a_indx - sizes[0];
	else
		costs[0] = a_indx;
	if (b_indx > (sizes[1] / 2))
		costs[1] = b_indx - sizes[1];
	else
		costs[1] = b_indx;
}

void	get_best_vars(int *norm, int size, int *best_len, int *best_arr)
{
	int	i;
	int	*temp_arr;
	int	temp_len;

	i = 0;
	temp_arr = malloc(size * sizeof(int));
	if (temp_arr == NULL)
		return ;
	while (i < size)
	{
		temp_len = get_lis(norm, size, temp_arr);
		if (*best_len < temp_len)
		{
			*best_len = temp_len;
			while (temp_len > 0)
			{
				temp_len--;
				best_arr[temp_len] = temp_arr[temp_len];
			}
		}
		i++;
	}
	free(temp_arr);
}

void	large_radix(int *norm, int *alen, int *stackb, int *blen)
{
	int	max_bits;
	int	curr_bit;
	int	og_len;
	int	i;

	max_bits = 0;
	og_len = *alen - 1;
	curr_bit = 4;
	while ((og_len >> max_bits) != 0)
		max_bits++;
	while (curr_bit++ < max_bits - 1)
	{
		i = 0;
		while (i++ < og_len + 1)
		{
			if (((norm[0] >> (curr_bit)) & 1) == 0)
				pushtob(stackb, blen, norm, alen);
			else
				rotate_a(norm, *alen);
		}
		while (*blen > 0)
			pushtoa(norm, alen, stackb, blen);
	}
}
