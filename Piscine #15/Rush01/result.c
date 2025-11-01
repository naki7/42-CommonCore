/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   result.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/07 16:04:39 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/07 16:46:16 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	solved(char *grid)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	if (!grid[i])
		return (0);
	while (grid[i])
	{
		while (grid[i][j])
		{
			if (grid[i][j] == '0')
				return (0);
			j++;
		}
		i++;
	}
	return (1);
}

void	showsolution(char *grid)
{
	int	y;
	int	x;

	x = 0;
	while (grid[x])
	{
		y = 0;
		while (grid[x][y])
		{
			write(1, &grid[x][y], 1);
			write(1, " ", 1);
			if (y == 3)
				write(1, "\n", 1);
			y++;
		}
		x++;
	}
}

int	main(int argc, char *argv)
{
	char	*grid[4][4];
	int		y;
	int		x;
	int		truthy;

	x = 0;
	if (argc == 2)
	{
		while (argv[1][x] && x < 4)
		{
			y = 0;
			while (argv[1][x][y] && x < 4)
			{
				grid[x][y] = argv[1][x][y];
				y++;
			}
			x++;
		}
	}
	truthy = solved(grid);
	if (truthy == 0)
		write(1, "Error\n", 6);
	if (truthy == 1)
		showsolution(grid);
	return (0);
}
