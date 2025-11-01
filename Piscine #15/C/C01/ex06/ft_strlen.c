/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/01 21:35:17 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/02 14:38:00 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strlen(char *str)
{
	int	counter;

	counter = 0;
	while (str[counter])
	{
		counter++;
	}
	return (counter);
}

//int	main(void)
//{
//	char	*phrase = "dragons";
//	int count;
//
//	count = ft_strlen(phrase);
//	printf("%i bytes in the phrase", count);
//	return (0);
//}
