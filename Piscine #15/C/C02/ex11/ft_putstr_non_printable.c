/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_non_printable.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/03 16:19:08 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/09 12:47:01 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

char	char_to_hex(int calc)
{
	if (calc < 10)
		return ('0' + calc);
	else
		return ('a' + calc - 10);
}

void	ft_putstr_non_printable(char *str)
{
	unsigned char	c;
	int				i;
	char			hex[2];

	i = 0;
	while (str[i])
	{
		c = str[i];
		if (str[i] < 32 || str[i] == 127)
		{
			write(1, "\\", 1);
			hex[0] = char_to_hex(c / 16);
			hex[1] = char_to_hex(c % 16);
			write(1, hex, 2);
		}
		else
			write(1, &str[i], 1);
		i++;
	}
	if (!str)
		return ;
}

//int	main(void)
//{
//	char	*string = "Hi!\n I\t like\r Otters!";
//
//	ft_putstr_non_printable(string);
//	return (0);
//}
