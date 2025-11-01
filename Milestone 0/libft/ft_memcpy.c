/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 19:39:17 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/15 16:50:07 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	size_t			i;
	unsigned char	*str;
	unsigned char	*cpy;

	i = 0;
	if (dest == NULL && src == NULL)
		return (dest);
	str = (unsigned char *)src;
	cpy = (unsigned char *)dest;
	while (i < n)
	{
		*(cpy + i) = *(str + i);
		i++;
	}
	return (dest);
}
