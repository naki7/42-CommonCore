/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 19:00:07 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/21 10:41:18 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static int	nextindex(char c, char const *set)
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

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*trim;
	size_t	len;
	size_t	i;
	size_t	j;

	i = 0;
	len = ft_strlen(s1);
	while (nextindex(s1[i], set) && len > 0)
		i++;
	while (nextindex(s1[len - 1], set) && (len - i) > 0)
		len--;
	trim = malloc((len - i) + 1);
	if (!trim)
		return (NULL);
	j = 0;
	while (i < len)
		trim[j++] = s1[i++];
	trim[j] = '\0';
	return (trim);
}
