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
