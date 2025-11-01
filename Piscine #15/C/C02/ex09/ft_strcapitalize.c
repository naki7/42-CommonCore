/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/03 12:38:26 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/08 17:58:23 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

char	ft_struplow(char letter, int *capital)
{
	if ((letter >= 97 && letter <= 122) && (*capital == 1))
		letter -= 32;
	if ((letter >= 65 && letter <= 90) && (*capital == 0))
		letter += 32;
	*capital = 0;
	return (letter);
}

char	*ft_strcapitalize(char *str)
{
	int	i;
	int	truthy;
	int	*next_cap;

	i = 0;
	truthy = 1;
	next_cap = &truthy;
	while (str[i])
	{
		if (!(str[i] >= 65 && str[i] <= 90) && !(str[i] >= 97 && str[i] <= 122))
		{
			if (!(str[i] >= 48 && str[i] <= 57))
				truthy = 1;
			else
				truthy = 0;
		}
		else
			str[i] = ft_struplow(str[i], next_cap);
		i++;
	}
	if (!str[i])
		str[i] = '\0';
	return (str);
}

//int	main(void)
//{
//	char	string[12] = "sL4y b0o1s!";
//
//	ft_strcapitalize(string);
//	printf("The final string is %s", string);
//	return (0);
//}
