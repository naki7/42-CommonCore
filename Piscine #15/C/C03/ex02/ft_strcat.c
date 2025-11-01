/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcat.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/04 21:19:37 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/05 11:05:24 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

char	*ft_strcat(char *dest, char *src)
{
	int		i;
	int		nul_indx;

	i = 0;
	nul_indx = 0;
	while (dest[nul_indx])
		nul_indx++;
	while (src[i])
	{
		dest[nul_indx] = src[i];
		i++;
		nul_indx++;
	}
	if (!src[i])
		dest[nul_indx] = '\0';
	return (dest);
}

/*int	main(void)
{
	char	*original = "are you?";
	char	copy[18] = "Hey how ";

	ft_strcat(copy, original);
	printf("%s", copy);
	return (0);
}*/
