/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_count_if.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 20:04:41 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/10 13:24:02 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

//int	ft_strlen(char *str)
//{
//	int	len;
//
//	len = 0;
//	while (str[len])
//		len++;
//	len = len % 2;
//	return (len);
//}

int	ft_count_if(char **tab, int (*f)(char*))
{
	int	i;
	int	count;

	i = 0;
	count = 0;
	while (tab[i] != 0)
	{
		if (f(tab[i]) == 1)
			count++;
		i++;
	}
	return (count);
}

//int	main(void)
//{
//	char	*arr[] = {"hi!", "not hi", "string!", "very stringy", 0};
//	int	total;
//
//	total = ft_count_if(arr, &ft_strlen);
//	printf("%i", total);
//	return (0);
//}
