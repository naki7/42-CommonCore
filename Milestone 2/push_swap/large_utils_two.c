/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   large_utils_two.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 15:09:45 by joshde-s          #+#    #+#             */
/*   Updated: 2026/02/10 14:23:39 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libpushswap.h"

int	reset_indexes(int *maxindx, int maxlen, int **dyn_arr)
{
	int	index;

	index = *maxindx;
	*maxindx = maxlen - 1;
	free(dyn_arr[0]);
	return (index);
}

void	free_larger_stack(t_stack **a)
{
	t_stack	*temp;
	t_stack	*curr_node;

	temp = *a;
	while (temp->next != NULL)
	{
		curr_node = temp;
		temp = temp->next;
		free(curr_node);
		if (temp->next == NULL)
			free(temp);
	}
}
