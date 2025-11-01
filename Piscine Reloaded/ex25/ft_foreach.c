/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_foreach.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 19:51:06 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/09 20:01:39 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_foreach(int *tab, int length, void (*f)(int))
{
	int	i;

	i = 0;
	while (i < length)
	{
		f(tab[i]);
		i++;
	}
}

//int	main(void)
//{
//	int	arr[] = {-34, 0, -16, 7, 25};
//	int	len = 5;
//
//	ft_foreach(arr, len, &ft_is_negative);
//	return (0);
//}
