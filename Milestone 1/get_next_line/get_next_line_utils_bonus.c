/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils_bonus.c                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 10:57:37 by joshde-s          #+#    #+#             */
/*   Updated: 2025/11/10 19:19:01 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

int	get_strlen(char *str)
{
	int	len;

	len = 0;
	while (str[len] != '\0')
		len++;
	return (len);
}

char	*get_strchr(char *addline)
{
	int	i;

	i = 0;
	if (!addline)
		return (0);
	while (addline[i] != '\0')
	{
		if (addline[i] == '\n')
		{
			return ((char *)&addline[i]);
		}
		i++;
	}
	return (0);
}

char	*get_calloc(size_t num, size_t tsize)
{
	size_t	i;
	size_t	len;
	char	*ptr;

	i = 0;
	if (num > 2147483647 / tsize)
		return (NULL);
	len = num * tsize;
	if (len == 0)
		len = 2;
	ptr = malloc(len);
	if (!ptr)
		return (NULL);
	while (i < len)
		ptr[i++] = 0;
	return (ptr);
}

char	*get_strjoin(char *line, char *addline)
{
	char	*joinline;
	int		i;
	int		j;
	int		len;

	i = 0;
	j = 0;
	if (!line)
		line = get_calloc(0, sizeof(char));
	len = get_strlen(line) + get_strlen(addline);
	joinline = get_calloc(len + 1, sizeof(char));
	if (!joinline)
		return (NULL);
	while (line[i])
		joinline[j++] = line[i++];
	i = 0;
	while (addline[i])
		joinline[j++] = addline[i++];
	free(line);
	return (joinline);
}
