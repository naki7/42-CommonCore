/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_numbers.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/28 14:50:36 by joshde-s          #+#    #+#             */
/*   Updated: 2025/08/30 16:18:53 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_print_numbers(void)
{
	char	num;
	char	count;

	num = 48;
	count = 0;
	while (count < 10)
	{
		write(1, &num, 1);
		num = num + 1;
		count = count + 1;
	}
}

/*int	main(void)
{
	ft_print_numbers();
	return (0);
}*/
