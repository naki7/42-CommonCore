/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   backtack.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/07 10:59:00 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/07 16:04:13 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	totalrow(char *grid, int *point, int j)
{
	int	i;

	*point = 0;
	i = 0;
	while (i < 4)
	{
		if (grid[j][i])
			*point += grid[j][i];
		i++;
	}
}

void	limitadd(int *add, int *counters)
{
	*add++;
	if (add > 4)
		*add = 1;
	*counters++;
}

void	testrow(char *grid, int temp_tot, int j, int k, int i)
{
	int	add;

	add = 0;
	while (k < 5)
	{
		limitAdd(&add);
		while (i < 4)
		{
			if (grid[j][i] == 0)
				temp_tot += add;
			if (temp_tot == 10)
			{
				k = 0;
				while (k < i)
				{
					if (grid[j][k] == 0)
						grid[j][k] = add;
					limitAdd(&add, &k);
				}
				return (0);
			}
			limitAdd(&add, &i);
		}
		k++;
	}
}

void	backtrack(char *grid)
{
	int	i;
	int	j;
	int	k;
	int	tot_line;

	i = 0;
	j = 0;
	k = 1;
	while (j < 4)
	{
		totalrow(grid, &tot_line, j);
		if (tot_line < 10)
		{
			testrow(grid, tot_line, j, k, i);
		}
		j++;
	}
}

int	main(int argc, char *argv)
{
	char	*grid[4][4];
	int		x;
	int		y;

	x = 0;
	if (argc == 2)
	{
		while (argv[1][x] && x < 4)
		{
			y = 0;
			while (argv[1][x][y] && y < 4)
			{
				grid[x][y] = argv[1][x][y];
				y++;
			}
			x++;
		}
	}
	backtrack(grid);
	return (0);
}
