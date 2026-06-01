/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   dongle_manager.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 14:43:12 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/01 11:33:05 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

void	dongle_refresh(t_dongle *dongle)
{

	dongle->usable = 0;
	dongle->usable_time += (dongle->cooldown * 1000);
	usleep(dongle->cooldown * 1000);
	dongle->usable = 1;
	pthread_cond_signal(dongle->condition);
}
