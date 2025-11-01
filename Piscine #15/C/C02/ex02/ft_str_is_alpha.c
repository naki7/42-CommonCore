/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_alpha.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/02 18:28:26 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/04 14:56:40 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_str_is_alpha(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] == '\0')
			return (1);
		if (!(str[i] >= 65 && str[i] <= 90) && !(str[i] >= 97 && str[i] <= 122))
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
//	char	*string2 = "apples";
//	char	*string3 = "apple&";
//	int	truthy_prnt;
//
//	truthy_prnt = ft_str_is_alpha(string);
//	printf("The 1st truthy is: %i, ", truthy_prnt);
//	truthy_prnt = ft_str_is_alpha(string2);
//	printf("The 2nd truthy is: %i, ", truthy_prnt);
//	truthy_prnt = ft_str_is_alpha(string3);
//	printf("The 3rd truthy is: %i", truthy_prnt);
//	return (0);
//}
