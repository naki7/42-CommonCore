/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_params.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 17:40:17 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/07 17:54:15 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c);
//void	ft_putchar(char c)
//{
//	write(1, &c, 1);
//}

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
		while (i < argc)
			ft_print_params(argv[i++]);
	}
	return (0);
}
