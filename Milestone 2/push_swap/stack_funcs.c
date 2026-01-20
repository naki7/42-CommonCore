/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_funcs.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 11:49:19 by joshde-s          #+#    #+#             */
/*   Updated: 2026/01/05 12:11:46 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libpushswap.h"
#include <stdio.h>

int	ft_stacksize(t_stack *stack)
{
	t_stack	*temp;
	size_t	len;

	len = 0;
	temp = stack;
	temp = stack->next;
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	return (len);
}

t_stack	*ft_stacknew(int value)
{
	t_stack	*node;

	node = malloc(sizeof(t_stack));
	if (!node)
		return (NULL);
	node->value = value;
	node->next = NULL;
	return (node);
}

void	ft_stackadd_back(t_stack **stack, t_stack *add)
{
	t_stack	*end;

	if (!*stack)
		return ;
	end = *stack;
	while (end->next != NULL)
		end = end->next;
	if (!end)
		*stack = add;
	else
		end->next = add;
}

void	produce_arrays(t_stack **a, int **stacka, int **stackb, int stklen)
{
	int		i;
	t_stack	*temp_a;

	i = 0;
	temp_a = *a;
	*stacka = malloc(stklen * sizeof(int));
	*stackb = malloc(stklen * sizeof(int));
	if (!*stacka || !*stackb)
		return ;
	while (i < stklen)
	{
		temp_a = temp_a->next;
		stacka[0][i] = temp_a->value;
		i++;
	}
}
