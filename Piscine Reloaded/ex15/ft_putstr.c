/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 15:52:26 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/07 16:06:09 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c);
//void	ft_putchar(char c)
//{
//	write(1, &c, 1);
//}

void	ft_putstr(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		ft_putchar(str[i++]);
}

//int	main(void)
//{
//	char	*str = "That's chaos magic, Wanda!";
//
//	ft_putstr(str);
//	return(0);
//}
