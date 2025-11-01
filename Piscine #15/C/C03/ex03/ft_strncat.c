/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/06 14:25:04 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/09 19:44:49 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

char	*ft_strncat(char *dest, char *src, unsigned int nb)
{
	unsigned int	i;
	unsigned int	nul_indx;

	i = 0;
	nul_indx = 0;
	while (dest[nul_indx])
		nul_indx++;
	while (src[i] && i < nb)
	{
		dest[nul_indx] = src[i];
		i++;
		nul_indx++;
	}
	if (!src[i] || i >= nb)
		dest[nul_indx] = '\0';
	return (dest);
}

//int	main(void)
//{
//	char	*original = "are you?";
//	char	*copy[18] = "Hey! How ";
//
//	ft_strncat(copy, original, 7);
//	printf("%s", copy);
//	return (0);
//}
