/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/03 14:40:08 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/08 17:57:59 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

unsigned int	ft_strlcpy(char *dest, char *src, unsigned int size)
{
	unsigned int	i;
	unsigned int	nul_indx;

	nul_indx = 0;
	i = 0;
	while (src[nul_indx])
		nul_indx++;
	while (i < (size - 1) && i < nul_indx)
	{
		dest[i] = src[i];
		i++;
	}
	if (!src[i])
		dest[i] = '\0';
	return (nul_indx);
}

//int	main(void)
//{
//	char	*string = "I'm sleepy";
//	char	copy[11] = "";
//	int	length = 11;
//
//	ft_strlcpy(copy, string, length);
//	printf("String is: %s, ", string);
//	printf("The copied one is: %s", copy);
//	return (0);
//}
