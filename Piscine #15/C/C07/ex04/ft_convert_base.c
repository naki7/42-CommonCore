/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_convert_base.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/16 12:24:25 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/18 22:29:42 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

int	validate(char *base);
int	tointconverter(long int total, char c, char *base, int *len);

void	getnumber(char *nbr, int *i, int *neg)
{
	while (nbr[*i] == 32 || (nbr[*i] > 8 && nbr[*i] < 14))
		(*i)++;
	while (nbr[*i] == 43 || nbr[*i] == 45)
	{
		if (nbr[*i] == 45)
			*neg = *neg * -1;
		(*i)++;
	}
}

char	*tostrconverter(int num, char *string, char *base, int len)
{
	int	i;
	int	temp;
	int	j;

	i = 0;
	if (num < 0)
	{
		num *= -1;
		string[0] = '-';
		i++;
	}
	temp = num;
	j = i;
	while (temp >= len)
	{
		temp = temp / len;
		j++;
	}
	string[j + 1] = '\0';
	while (j >= i)
	{
		string[j--] = base[num % len];
		num /= len;
	}
	return (string);
}

char	*finalstr(int num, char *base, int len)
{
	char	*string;
	int		tempnum;
	int		digits;

	tempnum = num;
	digits = 0;
	while (tempnum / len >= len)
	{
		digits++;
		tempnum /= len;
	}
	string = malloc(digits + 1);
	return (tostrconverter(num, string, base, len));
}

char	*ft_convert_base(char *nbr, char *base_from, char *base_to)
{
	int	from_len;
	int	to_len;
	int	i;
	int	neg;
	int	total;

	from_len = validate(base_from);
	to_len = validate(base_to);
	i = 0;
	neg = 1;
	total = 0;
	if (from_len == 1 || to_len == 1)
		return (NULL);
	getnumber(nbr, &i, &neg);
	while (from_len > 1)
	{
		total = tointconverter(total, nbr[i], base_from, &from_len);
		i++;
	}
	if (from_len == 1)
		return (finalstr(total * neg, base_to, to_len));
	else
		return (NULL);
}

//int	main(void)
//{
//	char	*nbr = "     -+----5bf6z1241md";
//	char	*from = "0123456789abcdef";
//	char	*to = "01";
//	char	*result;
//
//	result = ft_convert_base(nbr, from, to);
//	printf("The number: %s\n", nbr);
//	printf("from the base: %s\n", from);
//	printf("to the base of: %s\n", to);
//	printf("turns into: %s", result);
//	return (0);
//}
