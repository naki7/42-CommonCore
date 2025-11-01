/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/06 14:44:10 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/09 19:51:47 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	stringcmp(char *str, char *to_find, int i, int size)
{
	int	k;

	k = 0;
	while (str[i] == to_find[k])
	{
		if (k == size - 1)
			return (1);
		i++;
		k++;
		if (str[i] != to_find[k])
			break ;
	}
	return (0);
}

char	*ft_strstr(char *str, char *to_find)
{
	int	i;
	int	size;
	int	truthy;

	i = 0;
	size = 0;
	while (to_find[size])
	{
		size++;
	}
	while (str[i])
	{
		if (size == 0)
			return (&str[i]);
		truthy = stringcmp(str, to_find, i, size);
		if (truthy == 1)
			return (&str[i]);
		i++;
	}
	return (NULL);
}

//int	main(void)
//{
//	char	*needle = "here";
//	char	*stack = "knowhere";
//	char	*ptr;
//
//	ptr = ft_strstr(stack, needle);
//	printf("%p", ptr);
//	return (0);
//}
