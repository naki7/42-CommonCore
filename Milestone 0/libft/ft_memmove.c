/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 19:59:15 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/17 16:16:55 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	size_t	i;
	char	*str;
	char	*cpy;

	i = 0;
	if (!dest && !src)
		return (NULL);
	str = (char *)src;
	cpy = (char *)dest;
	if (cpy > str)
	{
		while (n-- > 0)
			cpy[n] = str[n];
	}
	else
	{
		while (i < n)
		{
			cpy[i] = str[i];
			i++;
		}
	}
	return (dest);
}
