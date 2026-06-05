/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   dongle_manager.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 14:43:12 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/02 15:26:35 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

long	current_time(void)
{
	struct timeval	tv;

	gettimeofday(&tv, NULL);
	return (tv.tv_sec * 1000L + tv.tv_usec / 1000L);
}

void	wait_for_dongle(t_dongle *dongle)
{
	while (dongle->usable == 0 || current_time() < dongle->usable_time)
		pthread_cond_wait(dongle->condition, dongle->lock);
}

void	grab_dongle(t_dongle *dongle, int coder_num)
{
	pthread_mutex_lock(dongle->lock);
	wait_for_dongle(dongle);
	printf("%i has taken a dongle\n", coder_num);
	dongle->usable = 0;
}

void	release_dongle(t_dongle *dongle, int coder_num)
{
	dongle->usable_time = current_time() + dongle->cooldown;
	usleep(dongle->cooldown * 1000);
	dongle->usable = 1;
	pthread_cond_broadcast(dongle->condition);
	pthread_mutex_unlock(dongle->lock);
	printf("%i lets go of their left dongle\n", coder_num);
}
