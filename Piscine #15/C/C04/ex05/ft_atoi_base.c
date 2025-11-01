/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 20:26:03 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/16 10:54:12 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

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

int	converter(long int total, char c, char *base, int *len)
{
	int	j;

	j = 0;
	while (j < *len)
	{
		if (base[j] != c)
			j++;
		else
			return ((total * *len) + j);
	}
	*len = 1;
	return (total);
}

int	ft_atoi_base(char *str, char *base)
{
	int			i;
	int			neg;
	long int	total;
	int			len;

	i = 0;
	neg = 1;
	total = 0;
	len = validate(base);
	while (str[i] == 32 || (str[i] >= 9 && str[i] <= 13))
		i++;
	while (str[i] == 43 || str[i] == 45)
	{
		if (str[i] == 45)
			neg *= -1;
		i++;
	}
	while (len != 1)
	{
		total = converter(total, str[i], base, &len);
		i++;
	}
	return (total * neg);
}

//int	main(void)
//{
//	char	*string = " \t  --++---+3f621jla12e";
//	char	*base = "0123456789abcdef";
//	int		result;
//	
//
//	result = ft_atoi_base(string, base);
//	printf("With a base of: %s,\n", base);
//	printf("and a string of: %s,\n", string);
//	printf("the int is: %i", result);
//	return (0);
//}
