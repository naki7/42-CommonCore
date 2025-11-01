/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 16:23:08 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/07 17:39:13 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] || s2[i])
	{
		if (s1[i] != s2[i])
			return (s1[i] - s2[i]);
		i++;
	}
	return (0);
}

//int	main(int argc, char *argv[])
//{
//	int	result;
//
//	result = 0;
//	if (argc == 3)
//	{
//		result = ft_strcmp(argv[1], argv[2]);
//		printf("%i", result);
//	}
//	return (0);
//}
