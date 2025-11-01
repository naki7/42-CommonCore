/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_uppercase.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/02 22:11:58 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/04 14:57:40 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_str_is_uppercase(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] == '\0')
			return (1);
		if (!(str[i] >= 65 && str[i] <= 90))
		{
			return (0);
		}
		i++;
	}
	return (1);
}

//int	main(void)
//{
//	char	*string = "apple Pie";
//	char	*string2 = "APPLES";
//	char	*string3 = "APPLES&";
//	int	truthy_prnt;
//
//	truthy_prnt = ft_str_is_uppercase(string);
//	printf("The 1st truthy is: %i, ", truthy_prnt);
//	truthy_prnt = ft_str_is_uppercase(string2);
//	printf("The 2nd truthy is: %i, ", truthy_prnt);
//	truthy_prnt = ft_str_is_uppercase(string3);
//	printf("The 3rd truthy is: %i", truthy_prnt);
//	return (0);
//}
