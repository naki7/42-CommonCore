/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 12:25:29 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/17 15:32:15 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static void	*freevars(char **arr, int num)
{
	int	i;

	i = 0;
	while (i < num)
		free(arr[i++]);
	free(arr);
	return (NULL);
}

static int	countwords(const char *src, char c)
{
	int	i;
	int	count;
	int	truthy;

	i = 0;
	count = 0;
	truthy = 0;
	while (src[i] != '\0')
	{
		if (src[i] == c && truthy == 1)
		{
			count++;
			truthy = 0;
		}
		else if (src[i] != c && truthy == 0)
			truthy = 1;
		i++;
	}
	if (truthy == 1)
		count++;
	return (count);
}

static char	*assignstrs(char *src, char c, int *i)
{
	char	*string;
	int		len;

	len = 0;
	string = NULL;
	while (src[len] != c && src[len] != '\0')
		len++;
	if (len > 0)
		len++;
	string = malloc(len);
	if (!string)
		return (NULL);
	ft_strlcpy(string, src, len);
	*i += len;
	return (string);
}

static int	initvars(int *i, int *j, char const *s1, char c)
{
	int	count;

	*i = 0;
	*j = 0;
	count = countwords(s1, c);
	return (count);
}

char	**ft_split(char const *s1, char c)
{
	int		i;
	int		j;
	int		count;
	char	**strings;
	char	*str;

	count = initvars(&i, &j, s1, c);
	strings = malloc((count + 1) * sizeof(char *));
	if (!strings)
		return (NULL);
	while (j < count)
	{
		if (s1[i] == c)
			i++;
		else
		{
			str = assignstrs((char *)s1 + i, c, &i);
			strings[j] = str;
			if (!strings[j])
				return (freevars(strings, j));
			j++;
		}
	}
	strings[j] = NULL;
	return (strings);
}
