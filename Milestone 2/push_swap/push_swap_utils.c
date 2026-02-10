/* *********************************************************************** */
/*                                                                         */
/*                                                     :::      ::::::::   */
/* push_swap_utils.c                                 :+:      :+:    :+:   */
/*                                                 +:+ +:+         +:+     */
/* By: joshde-s <joshde-s@student.42.fr>         +#+  +:+       +#+        */
/*                                             +#+#+#+#+#+   +#+           */
/* Created: 2026/02/10 12:03:19 by joshde-s        #+#    #+#              */
/* Updated: 2026/02/10 14:10:28 by joshde-s        ###   ########.fr       */
/*                                                                         */
/* *********************************************************************** */

#include "libpushswap.h"

void	handle_error(void)
{
	write(2, "Error\n", 6);
	exit(0);
}


void	free_stack_nodes(t_stack **a)
{
	t_stack	*temp;
	t_stack	*next;

	if (!a || !*a)
		return ;
	temp = *a;
	while (temp)
	{
		next = temp->next;
		free(temp);
		temp = next;
	}
	*a = NULL;
}

void	free_split_from(char **arr, int start)
{
	int	i;

	if (!arr)
		return ;
	i = start;
	while (arr[i])
		free(arr[i++]);
	free(arr);
}
