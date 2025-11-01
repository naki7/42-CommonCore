/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/02 17:39:05 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/06 11:53:03 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

char	*ft_strncpy(char *dest, char *src, unsigned int n)
{
	unsigned int	i;

	i = 0;
	while (src[i] && i < n)
	{
		dest[i] = src[i];
		i++;
	}
	while (i < n)
	{
		dest[i] = '\0';
		i++;
	}
	return (dest);
}

//int	main(void)
//{
//	char	*str = "words";
//	char	*cpy = (char *)malloc(6);
//
//	printf("old string: %s ", str);
//	ft_strncpy(cpy, str, 4);
//	printf("copied string: %s", cpy);
//	free(cpy);
//	cpy = NULL;
//	return (0);
//}
