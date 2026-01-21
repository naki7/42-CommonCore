/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   largesort.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 16:37:27 by joshde-s          #+#    #+#             */
/*   Updated: 2026/01/21 14:35:11 by joshde-s         ###   ########.fr       */
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

void	init_dynamic_array(int **dyn_arr, int *len, int *indx, int size)
{
	int	i;

	dyn_arr[0] = malloc(size * sizeof(int));
	dyn_arr[1] = malloc(size * sizeof(int));
	*len = 0;
	*indx = 0;
	i = 0;
	while (i < size)
	{
		dyn_arr[0][i] = 1;
		dyn_arr[1][i] = -1;
		i++;
	}
}

int	get_lis(int *norm, int size, int *temp)
{
	int	*dyn_arr[2];
	int	maxlen;
	int	maxindx;
	int	i;

	i = 0;
	init_dynamic_array(dyn_arr, &maxlen, &maxindx, size);
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
		temp[maxindx--] = i;
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
	while (i < size)//create as own func, removes 14ish lines
	{
		temp_len = get_lis(norm, size, temp_arr);
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
	return (best_len);
}

void	large_sort(int *norm, int *alen, int *stackb, int *blen)
{
	int	keep[*alen];
	int	keep_len;
	int	total;
	int	i;

	i = 0;
	total = *alen;
	keep_len = build_keep(norm, *alen, keep);
	while (i < total)
	{
		if (keep[i] == 0)
			pushtob(stackb, blen, norm, alen);
		else
			rotate_a(norm, *alen);
		i++;
	}
	greedy(norm, alen, stackb, blen);
}
