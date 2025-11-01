/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 12:34:05 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/21 12:14:44 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strchr(const char *s, int c)
{
	int				i;
	unsigned char	ch;
	char			*ptr;

	i = 0;
	ch = (unsigned char)c;
	while (s[i] != '\0')
	{
		if (ch == s[i])
		{
			ptr = (char *)&s[i];
			return (ptr);
		}
		i++;
	}
	if (s[i] == '\0' && ch == 0)
	{
		ptr = (char *)&s[i];
		return (ptr);
	}
	return (NULL);
}
