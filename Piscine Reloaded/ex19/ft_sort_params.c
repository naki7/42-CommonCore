/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_params.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 17:54:43 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/07 18:30:38 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c);
//void	ft_putchar(char c)
//{
//	write(1, &c, 1);
//}

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] || s2[i])
	{
		if (s1[i] != s2[i])
			return (s1[i] - s2[i]);
		i++;
	}
	return (0);
}

void	ft_sort_params(int len, char **arg)
{
	int		i;
	int		diff;
	char	*temp;

	i = 1;
	diff = 0;
	while (i < len)
	{
		temp = arg[i];
		diff = ft_strcmp(arg[i], arg[i + 1]);
		if (diff > 0)
		{
			arg[i] = arg[i + 1];
			arg[i + 1] = temp;
		}
		i++;
		if (i == len)
		{
			i = 1;
			len--;
		}
	}
}

void	ft_print_params(char *arg)
{
	int	j;

	j = 0;
	while (arg[j])
		ft_putchar(arg[j++]);
	ft_putchar('\n');
}

int	main(int argc, char *argv[])
{
	int	i;

	i = 1;
	if (argc > 1)
	{
		ft_sort_params(argc - 1, argv);
		while (i < argc)
			ft_print_params(argv[i++]);
	}
	return (0);
}
