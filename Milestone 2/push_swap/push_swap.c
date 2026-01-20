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
#include <stdio.h>

void	handle_error(void)
{
	write(1, "Error\n", 6);
	exit(0);
}

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
		if (str[0] == '-' && -value < -2147483648)
			return (0);	
		if (str[0] != '-' && value > 2147483647)
			return (0);
		i++;
	}
	return (1);
}

t_stack	**produce_stack(t_stack **a, char **argv, int argc)
{
	int		i;
	int		j;
	char	**temp;
	t_stack	*node;

	i = 1;
	while (i < argc)
	{
		temp = ft_split(argv[i], ' ');
		if (!temp)
			handle_error();
		j = 0;
		while (temp[j])
		{
			if (!validate_arg(temp[j]))
				handle_error();
			else
			{
				node = ft_stacknew(ft_atoi(temp[j]));
				ft_stackadd_back(a, node);
			}
			j++;
		}
		i++;
	}
	return (a);
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
	if (!stacka || !stackb)
		handle_error();
	handle_stack(stacka, &alen, stackb, &blen);
}

int	main(int argc, char *argv[])
{
	t_stack *a;

	a = ft_stacknew(0);
	if (argc > 1)
	{
		a = *produce_stack(&a, argv, argc);
		push_swap(&a);
		return (1);
	}
	else
		return (0);
}
