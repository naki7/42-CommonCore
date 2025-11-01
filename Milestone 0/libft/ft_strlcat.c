/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 14:46:20 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/20 11:46:11 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	dstlen;
	size_t	srclen;
	size_t	i;
	size_t	j;

	dstlen = ft_strlen(dst);
	srclen = ft_strlen(src);
	i = 0;
	j = 0;
	i = dstlen;
	if (size == 0)
		return (srclen);
	if (i >= size)
		return (size + srclen);
	while ((i + 1) < size && src[j])
		dst[i++] = src[j++];
	dst[i] = '\0';
	return (dstlen + srclen);
}
