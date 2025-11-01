/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_printable.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/02 22:34:21 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/04 14:57:55 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_str_is_printable(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] == '\0')
			return (1);
		if (!(str[i] >= 32 && str[i] <= 126))
			return (0);
		i++;
	}
	return (1);
}

//int	main(void)
//{
//	char	*string = "\n";
//	char	*string1 = " ";
//	char	*string2 = "\r";
//	int	truthy;
//
//	truthy = ft_str_is_printable(string);
//	printf("The first strings truthy is: %i ", truthy);
//	truthy = ft_str_is_printable(string1);
//        printf("The second strings truthy is: %i ", truthy);
//	truthy = ft_str_is_printable(string2);
//        printf("The third strings truthy is: %i ", truthy);
//}
