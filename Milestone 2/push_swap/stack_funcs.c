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

void	ft_stackadd_back(t_stack **stack, t_stack *add, char *string)
{
	t_stack	*end;

	free(string);
	if (!add)
		return ;
	if (!*stack)
	{
		*stack = add;
		return ;
	}
	end = *stack;
	while (end->next != NULL)
		end = end->next;
	end->next = add;
}

void	produce_arrays(t_stack **a, int **stacka, int **stackb, int stklen)
{
	int		i;
	t_stack	*temp_a;

	i = 0;
	temp_a = *a;
	*stacka = malloc(stklen * sizeof(int));
	if (!*stacka)
		return ;
	*stackb = malloc(stklen * sizeof(int));
	if (!*stackb)
		return ;
	while (i < stklen)
	{
		temp_a = temp_a->next;
		stacka[0][i] = temp_a->value;
		i++;
	}
}

void	free_small_stack(t_stack **a, int size)
{
	t_stack	*temp;

	temp = *a;
	if (size >= 6)
		free(temp->next->next->next->next->next->next);
	if (size >= 5)
		free(temp->next->next->next->next->next);
	if (size >= 4)
		free(temp->next->next->next->next);
	if (size >= 3)
		free(temp->next->next->next);
	if (size >= 2)
		free(temp->next->next);
	free(temp->next);
	free(temp);
}
