/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radix.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/06 16:48:27 by joshde-s          #+#    #+#             */
/*   Updated: 2026/01/12 16:37:10 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libpushswap.h"

void	radix(int *norm, int *alen, int *stackb, int *blen)
{
	int	max_bits;
	int	curr_bit;
	int	og_len;
	int	i;

	max_bits = 0;
	curr_bit = -1;
	og_len = *alen - 1;
	while ((og_len >> max_bits) != 0)
		max_bits++;
	while (curr_bit++ < max_bits)
	{
		i = 0;
		while (i++ < og_len + 1)
		{
			if (((norm[0] >> curr_bit) & 1) == 0)
				pushtob(stackb, blen, norm, alen);
			else
				rotate_a(norm, *alen);
		}
		while (*blen > 0)
			pushtoa(norm, alen, stackb, blen);
	}
}

int	*handle_temp(int *stacka, int *norm, int alen)
{
	int	i;
	int	j;
	int	*temp;

	i = 0;
	temp = malloc((alen) * sizeof(int));
	while (i < alen)
	{
		j = 0;
		while (j < alen)
		{
			if (norm[i] == stacka[j])
			{
				temp[i] = j;
				break ;
			}
			j++;
		}
		i++;
	}
	return (temp);
}

void	swap_to_i(int *stacka, int alen, int *norm)
{
	int	i;
	int	j;
	int	*temp;

	i = 0;
	temp = handle_temp(stacka, norm, alen);
	while (i < alen)
	{
		j = 0;
		while (j < alen)
		{
			if (temp[j] == i)
			{
				norm[i] = j;
				break ;
			}
			j++;
		}
		i++;
	}
	free(temp);
	temp = NULL;
}

void	normalize(int *stacka, int alen, int *norm)
{
	int	i;
	int	j;
	int	temp;

	i = 0;
	dup_atonorm(norm, stacka, alen);
	while (i < alen)
	{
		j = i + 1;
		temp = norm[i];
		while (j < alen)
		{
			if (norm[j] < temp)
			{
				norm[i] = norm[j];
				norm[j] = temp;
				temp = norm[i];
			}
			else if ((norm[j] == norm[i]) && (i != (alen - 1)))
				handle_error();
			j++;
		}
		i++;
	}
	swap_to_i(stacka, alen, norm);
}

void	handle_stack(int *stacka, int *alen, int *stackb, int *blen)
{
	int	*normstack;
	int	ordered;

	normstack = malloc((*alen) * sizeof(int));
	normalize(stacka, *alen, normstack);
	ordered = check_if_ordered(normstack, *alen);
	if (ordered == 1)
	{
		free_stacks(stacka, stackb, normstack);
		return ;
	}
	if (*alen == 2)
		rotate_a(stacka, *alen);
	else if (*alen == 3)
		sort_three(normstack);
	else if (*alen < 6)
		small_sort(normstack, alen, stackb, blen);
	else
	{
		large_radix(normstack, alen, stackb, blen);
		large_sort(normstack, alen, stackb, blen);
	}
	free_stacks(stacka, stackb, normstack);
}
