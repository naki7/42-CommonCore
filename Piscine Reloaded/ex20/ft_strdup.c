/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 18:32:36 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/08 10:58:55 by joshde-s         ###   ########.fr       */
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

char	*ft_strdup(char *src)
{
	char	*dup;
	int		i;
	int		len;

	len = ft_strlen(src);
	dup = malloc(len + 1);
	i = 0;
	while (i < len)
	{
		dup[i] = src[i];
		i++;
	}
	dup[i] = '\0';
	return (dup);
}

//int	main(int argc, char *argv[])
//{
//	char	*dup;
//
//	if (argc == 2)
//	{
//		dup = ft_strdup(argv[1]);
//		printf("%s", dup);
//		free(dup);
//	}
//	return (0);
//}
