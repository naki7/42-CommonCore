/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/01 16:22:44 by joshde-s          #+#    #+#             */
/*   Updated: 2025/11/04 12:47:21 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ftprintf.h"
#include <stdio.h>

int	validateset(char c, char *set)
{
	int	j;

	j = 0;
	while (set[j])
	{
		if (set[j] == c)
			return (1);
		j++;
	}
	return (0);
}

int	writeargs(char *substr, int *index, va_list args)
{
	char	*set = "cspdiuxX";
	char	*flags = "-0.# +123456789";

	if (validateset(substr[0], set))
		return (handleset(substr[0], args));
	else if (validateset(substr[0], flags))
		return (handleflags(substr, index, args));
	else
		return (-1);
}

int	ft_printf(const char *format, ...)
{
	int		length;
	int		i;
	va_list	args;

	length = 0;
	i = 0;
	va_start(args, format);
	while (format[i])
	{
		if (format[i] == '%')
		{
			i++;
			if (!format[i])
				break ;
			else if (format[i] == '%')
				length += write(1, "%", 1);
			else
				length += writeargs((char *)&format[i], &i, args);
		}
		else
			length += write(1, &format[i], 1);
		i++;
	}
	return (length);
}

int	main(void)
{
	int	length;

	length = ft_printf("How come you can %s, and you are a hero. %cut when I do the same I'm evil. I don't see %%, %s.. %i, %d, %x, %X, %p, %s, %p, %u\n", "break the rules", 'B', "how that's fair.", 12, -5002, 255, 255, &length, (char *)NULL, NULL, 234);
	printf("\nlength: %i\n", length);
	length = printf("How come you can %s, and you are a hero. %cut when I do the same I'm evil. I don't see %%, %s.. %i, %d, %x, %X, %p, %s, %p, %u\n", "break the rules", 'B', "how that's fair.", 12, -5002, 255, 255, &length, (char *)NULL, NULL, 234);
	printf("\nlength: %i\n", length);
	return (0);
}
