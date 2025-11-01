/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde@student.42porto.com>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/04 15:16:03 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/04 20:41:18 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i])
	{
		if (s1[i] != s2[i])
			return (s1[i] - s2[i]);
		i++;
		if (!s1[i] && s2[i])
			return (-s2[i]);
		if (!s1[i] && !s2[i])
			return (0);
	}
	if (!s1[0] && s2[0])
		return (-s2[0]);
	return (0);
}

/*int	main(void)
{
	char	*word1 = "ABCDE";
	char	*word2 = "ABCDe";
	int	result;

	result = ft_strcmp(word1, word2);
	printf("The difference between the two strings is: %i", result);
	return (0);
}*/
