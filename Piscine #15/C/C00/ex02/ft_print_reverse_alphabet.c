/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_reverse_alphabet.c                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/28 14:38:49 by joshde-s          #+#    #+#             */
/*   Updated: 2025/08/30 16:18:24 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_print_reverse_alphabet(void)
{
	char	letter;
	char	count;

	letter = 122;
	count = 0;
	while (count < 26)
	{
		write(1, &letter, 1);
		letter = letter - 1;
		count = count + 1;
	}
}

/*int	main(void)
{
	ft_print_reverse_alphabet();
	return (0);
}*/
