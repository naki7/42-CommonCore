/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 19:54:59 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/20 14:00:34 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static void	fillstr(int n, char *string, int i)
{
	if (n >= 10)
		fillstr(n / 10, string, i - 1);
	string[i] = (n % 10) + 48;
}

static int	setvars(int n)
{
	int	digits;

	digits = 0;
	if (n < 1)
		digits++;
	if (n < 0)
		n = -n;
	while (n > 0)
	{
		digits++;
		n /= 10;
	}
	return (digits);
}

static char	*edgecase(void)
{
	char	*str;

	str = malloc(12);
	if (!str)
		return (NULL);
	str[0] = 45;
	str[1] = 50;
	fillstr(147483648, str, 10);
	str[11] = '\0';
	return (str);
}

char	*ft_itoa(int n)
{
	char	*string;
	int		digits;

	if (n == -2147483648)
	{
		string = edgecase();
		return (string);
	}
	digits = setvars(n);
	string = malloc(digits + 1);
	if (!string)
		return (NULL);
	if (n < 0)
	{
		string[0] = 45;
		fillstr(n * -1, string, digits - 1);
	}
	else
		fillstr(n, string, digits - 1);
	string[digits] = '\0';
	return (string);
}
