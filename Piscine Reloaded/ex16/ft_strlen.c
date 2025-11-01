/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 16:11:07 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/07 16:21:36 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_strlen(char *str)
{
	int	len;

	len = 0;
	while (str[len])
		len++;
	return (len);
}

//int	main(int argc, char *argv[])
//{
//	int	result;
//
//	if (argc == 2)
//	{
//		result = ft_strlen(argv[1]);
//		printf("%i", result);
//	}
//	return (0);
//}
