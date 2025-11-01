/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlowcase.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/03 12:26:46 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/08 17:58:44 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

char	*ft_strlowcase(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] >= 65 && str[i] <= 90)
			str[i] += 32;
		i++;
	}
	if (!str[i])
		str[i] = '\0';
	return (str);
}

//int	main(void)
//{
//	char	string[6] = "WORDS!";
//
//	ft_strlowcase(string);
//	printf("After dullification: %s", string);
//	return (0);
//}
