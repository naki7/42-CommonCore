/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/14 13:23:21 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/18 11:28:19 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

int	ft_strlen(char *str)
{
	int	len;

	len = 0;
	while (str[len])
		len++;
	return (len);
}

void	cpychar(char *str, char **src, char *split, int size)
{
	int	j;
	int	k;
	int	l;

	j = 0;
	k = 0;
	while (k < size)
	{
		l = 0;
		while (src[k][l])
		{
			str[j] = src[k][l];
			j++;
			l++;
		}
		k++;
		l = 0;
		while (k < size && split[l])
		{
			str[j] = split[l];
			j++;
			l++;
		}
	}
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	char	*string;
	int		i;
	int		j;
	int		length;

	i = 0;
	j = 0;
	length = 0;
	if (size == 0)
		string = malloc(1);
	else
	{
		while (i < size)
		{
			length += ft_strlen(strs[i]);
			i++;
		}
		length += ft_strlen(sep) * (size - 1);
		i = 0;
		string = malloc(length + 1);
		cpychar(string, strs, sep, size);
	}
	string[length] = '\0';
	return (string);
}

//int	main(void)
//{
//	char	*array[3] = {"Agatha", "All", "Along!"};
//	int		size;
//	char	*result;
//	char	*seperator = ", ";
//
//	size = 3;
//	result = ft_strjoin(size, array, seperator);
//	printf("%s", result);
//	free(result);
//	return (0);
//}
