/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/09 16:58:58 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/16 10:34:46 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	str_to_int(char *str, int i, int length)
{
	int	num;
	int	total;
	int	count;

	count = length;
	total = 0;
	while (count > 0)
	{
		length = count;
		num = str[i - count] - 48;
		while (length > 1)
		{
			num *= 10;
			length--;
		}
		total += num;
		count--;
	}
	return (total);
}

int	ft_atoi(char *str)
{
	int			i;
	int			neg;
	long int	length;
	int			total;

	i = 0;
	neg = 1;
	length = 0;
	total = 0;
	while (str[i] == 32 || (str[i] >= 9 && str[i] <= 13))
		i++;
	while (str[i] == 43 || str[i] == 45)
	{
		if (str[i] == 45)
			neg *= -1;
		i++;
	}
	while (str[i] >= 48 && str[i] <= 57)
	{
		length++;
		i++;
	}
	total = str_to_int(str, i, length);
	return (total * neg);
}

//int	main(void)
//{
//	int	tester;
//
//	tester = ft_atoi("    \r -+--+--+341944ade2");
//	printf("%i", tester);
//	return (0);
//}
