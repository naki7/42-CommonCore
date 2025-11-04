/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_handleprint.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 12:13:04 by joshde-s          #+#    #+#             */
/*   Updated: 2025/11/04 12:38:15 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ftprintf.h"

int	handlehex(char spec, unsigned long num)
{
	char	*base;
	int		count;

	if (spec == 'X')
		base = "0123456789ABCDEF";
	else
		base = "0123456789abcdef";
	if (spec == 'p')
	{
		if (num == 0)
			return (write(1, "(nil)", 5));
		write(1, "0x", 2);
		return (2 + handlehex('x', num));
	}
	if (num < 16)
		return (write(1, &base[num], 1));
	else
	{
		count = handlehex(spec, num / 16);
		return (count + handlehex(spec, num % 16));
	}
	return (0);
}

int	handlestr(char specifier, char *str)
{
	int	len;

	if (specifier == 's' && str == NULL)
		return (write(1, "(null)", 6));
	len = ft_strlen(str);
	return (write(1, str, len));
}

int	handleset(char specifier, va_list args)
{
	char	c;

	if (specifier == 'c')
	{
		c = va_arg(args, int);
		return(write(1, &c, 1));
	}
	else
	{
		if (specifier == 's')
			return handlestr(specifier, va_arg(args, char *));
		else if (specifier == 'd' || specifier == 'i')
			return handlestr(specifier, ft_itoa(va_arg(args, int)));
		else if (specifier == 'u')
			return handlestr(specifier, ft_itoa(va_arg(args, unsigned int)));
		else if (specifier == 'x' || specifier == 'X')
			return (handlehex(specifier, va_arg(args, unsigned int)));
		else
			return (handlehex(specifier, (unsigned long)va_arg(args, void *)));
	}
	return (-1);
}
