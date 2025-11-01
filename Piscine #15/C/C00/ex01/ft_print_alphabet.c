/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_alphabet.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/28 11:56:53 by joshde-s          #+#    #+#             */
/*   Updated: 2025/08/30 16:17:47 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_print_alphabet(void)
{
	char	letter;
	char	count;

	letter = 97;
	count = 0;
	while (count < 26)
	{
		write(1, &letter, 1);
		letter = letter +1;
		count = count + 1;
	}
}

/*int	main(void)
{
	ft_print_alphabet();
	return (0);
}*/
