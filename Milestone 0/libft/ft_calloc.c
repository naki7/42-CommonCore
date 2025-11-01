/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 12:50:54 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/21 09:58:05 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	size_t			i;
	size_t			len;
	unsigned char	*ptr;

	i = 0;
	len = nmemb * size;
	if (len == 0)
	{
		ptr = malloc(len);
		return (ptr);
	}
	if (nmemb > 2147483647 / size)
		return (NULL);
	ptr = malloc(len);
	if (!ptr)
		return (NULL);
	while (i < len)
		ptr[i++] = 0;
	return (ptr);
}
