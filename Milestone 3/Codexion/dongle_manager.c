/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   dongle_manager.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 14:43:12 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/19 10:49:44 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

long	current_time(void)
{
	struct timeval	tv;

	gettimeofday(&tv, NULL);
	return (tv.tv_sec * 1000L + tv.tv_usec / 1000L);
}

void	join_queue(t_dongle *dongle, t_coder *coder)
{
	if (dongle->queue_size == 0)
		dongle->queue[0] = (t_request){coder->n, current_time(),
			coder->next_deadline};
	else if (dongle->queue_size == 1)
	{
		if (coder->next_deadline > dongle->queue[0].next_deadline
			|| strcmp(dongle->priority, "fifo") == 0)
			dongle->queue[1] = (t_request){coder->n, current_time(),
				coder->next_deadline};
		else
		{
			dongle->queue[1] = dongle->queue[0];
			dongle->queue[0] = (t_request){coder->n, current_time(),
				coder->next_deadline};
		}
	}
	dongle->queue_size++;
}

void	wait_for_dongle(t_dongle *dongle, int coder_num, t_monitor *monitor)
{
	while ((dongle->queue[0].coder_num != coder_num
			|| dongle->usable == 0 || current_time() < dongle->usable_time)
		&& monitor->state)
		pthread_cond_wait(dongle->condition, dongle->lock);
	if (monitor->state)
	{
		if (dongle->queue_size == 2)
			dongle->queue[0] = dongle->queue[1];
		dongle->queue_size--;
	}
}

int	grab_dongle(t_dongle *dongle, t_coder *coder)
{
	pthread_mutex_lock(dongle->lock);
	if (!coder->monitor->state)
	{
		pthread_mutex_unlock(dongle->lock);
		return (-1);
	}
	join_queue(dongle, coder);
	wait_for_dongle(dongle, coder->n, coder->monitor);
	if (coder->monitor->state)
	{
		handle_print(coder, "has taken a dongle");
		dongle->usable = 0;
		pthread_mutex_unlock(dongle->lock);
		return (0);
	}
	pthread_mutex_unlock(dongle->lock);
	return (-1);
}

void	release_dongle(t_dongle *dongle)
{
	pthread_mutex_lock(dongle->lock);
	dongle->usable_time = current_time() + dongle->cooldown;
	pthread_mutex_unlock(dongle->lock);
	usleep(dongle->cooldown * 1000);
	pthread_mutex_lock(dongle->lock);
	dongle->usable = 1;
	pthread_cond_broadcast(dongle->condition);
	pthread_mutex_unlock(dongle->lock);
}
