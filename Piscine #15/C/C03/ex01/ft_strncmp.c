/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/04 20:49:36 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/11 08:52:25 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_strncmp(char *s1, char *s2, unsigned int n)
{
	unsigned int	i;

	i = 0;
	while (s1[i] && i < n)
	{
		if (s1[i] != s2[i])
			return (s1[i] - s2[i]);
		i++;
		if (!s1[i] && s2[i])
			return (-s2[i]);
		if (!s1[i] && !s2[i])
			return (0);
	}
	if (!s1[0] && s2[0] && n > 0)
		return (-s2[0]);
	return (0);
}

/*int	main(void)
{
	char	*word1 = "ABCDE";
	char	*word2 = "ABCDe";
	int	result;

	result = ft_strncmp(word1, word2, 4);
	printf("The difference with a size limit is: %i", result);
	return (0);
}*/
