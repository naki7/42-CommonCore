/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/08 09:48:40 by joshde-s          #+#    #+#             */
/*   Updated: 2026/01/12 13:32:28 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libpushswap.h"

int	validate_arg(char *str)
{
	int		i;
	long	value;
	char	*validset;

	i = 0;
	value = 0;
	validset = "0123456789";
	if (str[i] == '+' || str[i] == '-')
		i++;
	if (str[i] == '\0')
		return (0);
	while (str[i])
	{
		if (!(ft_strchr(validset, str[i])))
			return (0);
		value = (value * 10) + (str[i] - '0');
		if (str[0] == '-' && (value * -1) < -2147483648)
			return (0);
		if (str[0] != '-' && value > 2147483647)
			return (0);
		i++;
	}
	return (1);
}

void	handle_split(t_stack **a, char **temp, int j)
{
	t_stack	*node;

	if (!validate_arg(temp[j]))
	{
		free_split_from(temp, j);
		free_stack_nodes(a);
		handle_error();
	}
	else
	{
		node = ft_stacknew(ft_atoi(temp[j]));
		if (!node)
		{
			free_split_from(temp, j);
			free_stack_nodes(a);
			handle_error();
		}
		ft_stackadd_back(a, node, temp[j]);
	}
}

void	produce_stack(t_stack **a, char **argv, int argc, int i)
{
	int		j;
	char	**temp;

	while (i < argc)
	{
		temp = ft_split(argv[i], ' ');
		if (!temp)
		{
			free_stack_nodes(a);
			handle_error();
		}
		j = 0;
		while (temp[j])
		{
			handle_split(a, temp, j);
			j++;
		}
		i++;
		free(temp);
	}
}

void	push_swap(t_stack **a)
{
	int	*stacka;
	int	alen;
	int	*stackb;
	int	blen;

	stacka = NULL;
	alen = ft_stacksize(*a);
	blen = 0;
	stackb = NULL;
	produce_arrays(a, &stacka, &stackb, alen);
	if (alen < 7)
		free_small_stack(a, alen);
	else
		free_larger_stack(a);
	if (!stacka || !stackb)
		return ;
	handle_stack(stacka, &alen, stackb, &blen);
}

int	main(int argc, char *argv[])
{
	t_stack	*a;
	int		i;

	a = ft_stacknew(0);
	i = 1;
	if (argc > 1)
	{
		if (argv[1][0] == '\0')
		{
			free(a);
			handle_error();
		}
		produce_stack(&a, argv, argc, i);
		push_swap(&a);
		return (1);
	}
	else
		return (0);
}
