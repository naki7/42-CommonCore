/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   refresh.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 14:43:12 by joshde-s          #+#    #+#             */
/*   Updated: 2026/05/27 17:36:05 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

void	dongle_refresh(t_dongle *dongle)
{
	int	cooldown;
	int	i;

	dongle->usable = 0;
	printf("%p", &dongle->lock);
	cooldown = dongle->cooldown;
	usleep(cooldown);
	dongle->usable = 1;
	pthread_cond_signal(&dongle->condition);
}
