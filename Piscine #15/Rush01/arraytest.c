/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   arraytest.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/06 20:34:06 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/07 16:45:28 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

void	formgrid(char *grid)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	while (i < 4)
	{
		while (j < 4)
		{
			grid[i][j] = '0';
			j++;
		}
		i++;
	}
}

void	calcone(char *grid, int i)
{
	if (i < 4)
		grid[i][0] = '4';
	if (i > 3 && i < 8)
		grid[i - 4][3] = '4';
	if (i > 7 && i < 12)
		grid[0][i - 8] = '4';
	if (i > 11 && i < 16)
		grid[3][i - 12] = '4';
}

void	calcfour(char *grid, int i, int j)
{
	while (i < 4 && j < 4)
	{
		grid[i][j] = '1' + j;
		j++;
		i++;
	}
	while ((i > 3 && i < 8) && j < 4)
	{
		grid[i - 4][3 - j] = '1' + j;
		j++;
		i++;
	}
	while ((i > 7 && i < 11) && j < 4)
	{
		grid[j][i - 8] = '1';
		j++;
		i++;
	}
	while ((i > 12 && i < 16) && j < 4)
	{
		grid[3 - j][i - 12] = '1' + j;
		j++;
		i++;
	}
}

int	main(int argc, char *argv[])
{
	char	*values = (char *)malloc(16 * sizeof(char));
	char	*grid[4][4];
	int		i;

	i = 0;
	if (argc == 2)
	{
		while (argv[1][i])
		{
			values[i] = argv[1][i];
			i++;
		}
	}
	formgrid(grid);
	i = 0;
	while (arr[i])
	{
		if (arr[i] == '4')
			clacfour(grid, i, 0);
		if (arr[i] == '1')
			calcone(grid, i);
		i++;
	}
	free(values);
	return (0);
}
