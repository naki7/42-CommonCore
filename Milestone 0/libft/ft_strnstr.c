/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 17:45:18 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/21 13:34:49 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t			i;
	size_t			j;
	unsigned char	*ptr;

	i = 0;
	if (!little[0])
	{
		ptr = (unsigned char *)big;
		return ((char *)ptr);
	}
	while (i < len && big[i])
	{
		j = 0;
		while (little[j] && big[i + j] == little[j] && (i + j) < len)
		{
			j++;
			if (!little[j])
			{
				ptr = (unsigned char *)&big[i];
				return ((char *)ptr);
			}
		}
		i++;
	}
	return (NULL);
}
