/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_numeric.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/02 19:00:24 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/04 14:56:57 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_str_is_numeric(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] == '\0')
			return (1);
		if (!(str[i] >= 48 && str[i] <= 57))
			return (0);
		i++;
	}
	return (1);
}

//int	main(void)
//{
//	char *string = "word";
//	char *string1 = "18648723645";
//	char *string2 = "1 2";
//	int truthy;
//
//	truthy = ft_str_is_numeric(string);
//	printf("The 1st truthy is: %i ", truthy);
//	truthy = ft_str_is_numeric(string1);
//        printf("The 2nd truthy is: %i ", truthy);
//	truthy = ft_str_is_numeric(string2);
//        printf("The 3rd truthy is: %i", truthy);
//
//}
