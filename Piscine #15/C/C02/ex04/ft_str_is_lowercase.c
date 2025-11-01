/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_lowercase.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/02 21:15:19 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/04 14:57:24 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_str_is_lowercase(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] == '\0')
			return (1);
		if (!(str[i] >= 97 && str[i] <= 122))
		{
			return (0);
		}
		i++;
	}
	return (1);
}

//int	main(void)
//{
//	char	*string = "Boots";
//	char	*string1 = "boots";
//	char	*string2 = "ab24 1a";
//	int	truthy;
//
//	truthy = ft_str_is_lowercase(string);
//	printf("The 1st truthy is: %i ", truthy);
//	truthy = ft_str_is_lowercase(string1);
//	printf("The 2nd truthy is: %i ", truthy);
//	truthy = ft_str_is_lowercase(string2);
//	printf("The 3rd truthy is: %i", truthy);
//}
