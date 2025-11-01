/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_rush01.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aellen-s <aellen-s@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/06 19:10:20 by aellen-s          #+#    #+#             */
/*   Updated: 2025/09/07 16:47:21 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <stdlib.h>

void	errmsg(void)
{
	write(1, "Error\n", 6);
}

void	rmvspc(char temp, char *vals, int j, int *pnt)
{
	if (temp >= '1' && temp <= '4')
	{
		vals[j] = temp;
		j++;
		*pnt = j;
	}
	if (temp < '1' || temp > '4')
		errmsg();
	if (pnt >= 16)
		errmsg();
}

int	main(int argc, char *argv[])
{
	char	*values = (char *)malloc(16 * sizeof(char));
	char	temp;
	int		j;
	int		k;
	int		*pnt;

	j = 0;
	k = 0;
	pnt = &j;
	if (argc == 2)
	{
		while (argv[1][k] != '\0')
		{
			temp = argv[1][k];
			k++;
			rmvspc(temp, values, j, pnt);
		}
	}
	else
		errmsg();
	free(values);
	return (0);
}
