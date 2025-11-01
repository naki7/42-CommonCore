/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/02 16:37:25 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/06 11:48:56 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

char	*ft_strcpy(char *dest, char *src)
{
	int	i;

	i = 0;
	while (src[i])
	{
		dest[i] = src[i];
		i++;
	}
	if (!src[i])
		dest[i] = '\0';
	return (dest);
}

//int	main(void)
//{
//	char	*str = "Boots!";
//	char	*cpy = (char *)malloc(7);
//
//	printf("old string: %s", str);
//	ft_strcpy(cpy, str);
//	printf("copied string: %s", cpy);
//	free(cpy);
//	cpy = NULL;
//	return (0);
//}
