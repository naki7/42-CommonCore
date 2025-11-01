/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strupcase.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/03 11:07:22 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/08 17:59:09 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

char	*ft_strupcase(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] >= 97 && str[i] <= 122)
			str[i] -= 32;
		i++;
	}
	if (!str[i])
		str[i] = '\0';
	return (str);
}

//int	main(void)
//{
//	char	string[6] = "words!";
//
//	ft_strupcase(string);
//	printf("After yasssification: %s", string);
//	return (0);
//}
