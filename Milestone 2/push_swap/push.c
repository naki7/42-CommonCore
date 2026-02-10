/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 20:33:33 by joshde-s          #+#    #+#             */
/*   Updated: 2026/01/06 11:11:36 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libpushswap.h"

void	pushtoa(int *into, int *inlen, int *outof, int *outlen)
{
	int	a_i;
	int	b_i;
	int	temp;

	a_i = 0;
	b_i = *inlen;
	temp = outof[0];
	(*outlen)--;
	while (a_i < *outlen)
	{
		outof[a_i] = outof[a_i + 1];
		a_i++;
	}
	(*inlen)++;
	while (b_i > -1)
	{
		into[b_i] = into[b_i - 1];
		b_i--;
	}
	into[0] = temp;
	write(1, "pa\n", 3);
}

void	pushtob(int *into, int *inlen, int *outof, int *outlen)
{
	int	a_i;
	int	b_i;
	int	temp;

	a_i = 0;
	b_i = *inlen;
	temp = outof[0];
	(*outlen)--;
	while (a_i < *outlen)
	{
		outof[a_i] = outof[a_i + 1];
		a_i++;
	}
	(*inlen)++;
	while (b_i > -1)
	{
		into[b_i] = into[b_i - 1];
		b_i--;
	}
	into[0] = temp;
	write(1, "pb\n", 3);
}
