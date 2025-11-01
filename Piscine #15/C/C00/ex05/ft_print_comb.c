/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/28 15:58:30 by joshde-s          #+#    #+#             */
/*   Updated: 2025/08/30 16:20:03 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	write_three(char one, char two, char three)
{
	write(1, &one, 1);
	write(1, &two, 1);
	write(1, &three, 1);
}

void	ft_print_comb(void)
{
	char	num1;
	char	num2;
	char	num3;

	num1 = 48;
	while (num1 < 56)
	{
		num2 = num1 + 1;
		while (num2 < 57)
		{
			num3 = num2 + 1;
			while (num3 < 58)
			{
				write_three(num1, num2, num3);
				if (num1 != 55)
				{
					write(1, ", ", 2);
				}
				num3++;
			}
			num2++;
		}
		num1++;
	}
}

/*int	main(void)
{
	ft_print_comb();
	return (0);
}*/
