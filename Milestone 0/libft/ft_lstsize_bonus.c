/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 19:50:31 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/17 22:05:51 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_lstsize(t_list *lst)
{
	t_list	*temp;
	size_t	len;

	len = 0;
	temp = lst;
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	return (len);
}
