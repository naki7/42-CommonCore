/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   largesort.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 16:37:27 by joshde-s          #+#    #+#             */
/*   Updated: 2026/01/15 13:04:57 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libpushswap.h"
#include <stdio.h>

void	fill_dynamic_array(int *norm, int **dyn_arr, int indx)
{
	int	curr_v;
	int	prev_v;
	int	j;

	j = 0;
	while (j < indx)
	{
		curr_v = norm[indx];
		prev_v = norm[j];
		if (prev_v < curr_v && dyn_arr[0][j] + 1 > dyn_arr[0][indx])
		{
			dyn_arr[0][indx] = dyn_arr[0][j] + 1;
			dyn_arr[1][indx] = j;
		}
		j++;
	}
}

int	get_lis(int *norm, int size, int start, int *temp)
{
	int	*dyn_arr[2];
	int	maxlen;
	int	maxindx;
	int	i;

	i = 0;
	dyn_arr[0] = malloc(size * sizeof(int));
	dyn_arr[1] = malloc(size * sizeof(int));
	maxlen = 0;
	maxindx = 0;
	while (i < size)
	{
		dyn_arr[0][i] = 1;
		dyn_arr[1][i] = -1;
		i++;
	}
	i = 0;
	while (i < size)
	{
		fill_dynamic_array(norm, dyn_arr, i);
		if(dyn_arr[0][i] > maxlen)
		{
			maxlen = dyn_arr[0][i];
			maxindx = i;
		}
		i++;
	}
	i = maxindx;
	maxindx = maxlen - 1;
	while (i != -1)
	{
		temp[maxindx--] = start + i;
		i = dyn_arr[1][i];
	}
	return (maxlen);
}

int	build_keep(int *norm, int size, int *keep)
{
	int	temp_arr[size];
	int	temp_len;
	int	best_arr[size];
	int	best_len;
	int	i;

	i = 0;
	best_len = 0;
	while (i < size)
	{
		temp_len = get_lis(norm, size, i, temp_arr);
		if (best_len < temp_len)
		{
			best_len = temp_len;
			while (temp_len > 0)
			{
				temp_len--;
				best_arr[temp_len] = temp_arr[temp_len];
			}
		}
		i++;
	}
	i = 0;
	while (i < size)
	{
		keep[i] = 0;
		i++;
	}
	i = 0;
	while (i < best_len)
	{
		keep[best_arr[i]] = 1;
		i++;
	}
	i = 0;
	while (i < size)
	{
		printf("\nkeep i: %i, - v: %i\n", i, keep[i]);
		i++;
	}
	return (best_len);
}

void	large_sort(int *norm, int *alen, int *stackb, int *blen)
{
	int	keep[*alen];
	int	keep_len;
	int	i;

	i = 0;
	keep_len = build_keep(norm, *alen, keep);
	while (keep_len < *alen)
	{
		if (keep[i] == 0)
			pushtob(stackb, blen, norm, alen);
		else
			rotate_a(norm, *alen);
		i++;
	}
	greedy(norm, alen, stackb, blen);
	i = 0;
	while (i < *alen)
		printf("\nstacka: %i\n", norm[i++]);
	i = 0;
	while (i < *blen)
		printf("\nstackb: %i\n", stackb[i++]);
}
