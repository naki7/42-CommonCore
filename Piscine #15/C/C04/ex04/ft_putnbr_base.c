/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/15 12:39:59 by joshde-s          #+#    #+#             */
/*   Updated: 2025/09/16 10:38:28 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <stdlib.h>

int	validate(char *base)
{
	int	i;
	int	j;

	i = 0;
	if (!base[i] || !base[i + 1])
		return (0);
	while (base[i])
	{
		if (base[i] == '-' || base[i] == '+')
			return (0);
		j = i + 1;
		while (base[j])
		{
			if (base[j] == base[i])
				return (0);
			j++;
		}
		i++;
	}
	return (i);
}

void	converter(long int num, char *base, int len)
{
	char	c;

	if (num < 0)
	{
		num *= -1;
		write(1, "-", 1);
	}
	if (num >= len)
		converter(num / len, base, len);
	c = base[num % len];
	write(1, &c, 1);
}

void	ft_putnbr_base(int nbr, char *base)
{
	int		len;

	len = 0;
	len = validate(base);
	if (len == 0)
		return ;
	converter(nbr, base, len);
}

//int	main(void)
//{
//	char	*basestr;
//	int		num;
//
//	basestr = "0123456789abcdef";
//	num = -2147483648;
//	ft_putnbr_base(num, basestr);
//	return (0);
//}
