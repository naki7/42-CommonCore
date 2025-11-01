/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_convert_base2.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/17 12:17:55 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/17 12:22:02 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	validate(char *base)
{
	int	i;
	int	j;

	i = 0;
	if (!base[i] || !base[i + 1])
		return (1);
	while (base[i])
	{
		if (base[i] == '-' || base[i] == '+')
			return (1);
		j = i + 1;
		while (base[j])
		{
			if (base[j] == base[i])
				return (1);
			j++;
		}
		i++;
	}
	return (i);
}

int	tointconverter(long int total, char c, char *base, int *len)
{
	int			j;
	long int	temptotal;

	j = 0;
	temptotal = 0;
	while (j < *len)
	{
		if (base[j] != c)
			j++;
		else
		{
			temptotal = (total * *len) + j;
			if (temptotal >= -2147483648 && temptotal <= 2147483647)
				return ((total * *len) + j);
			else
			{
				*len = 0;
				return (total);
			}
		}
	}
	*len = 1;
	return (total);
}
