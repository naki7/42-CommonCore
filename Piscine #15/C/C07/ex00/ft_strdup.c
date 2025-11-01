/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/12 21:31:55 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/18 23:01:20 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

char	*ft_strdup(char *src)
{
	char	*cpy;
	int		i;
	int		len;

	i = 0;
	len = 0;
	while (src[len])
		len++;
	cpy = malloc(len + 1);
	while (src[i])
	{
		cpy[i] = src[i];
		i++;
	}
	while (i <= (len +1))
	{
		cpy[i] = '\0';
		i++;
	}
	return (cpy);
}

//int	main(void)
//{
//	char	*str = "Yay another string...";
//	char	*cpy;
//
//	cpy = ft_strdup(str);
//	printf("%s", cpy);
//	free(cpy);
//	return (0);
//}
