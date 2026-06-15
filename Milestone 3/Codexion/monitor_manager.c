/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitor_manager.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 16:31:15 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/15 18:00:01 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

void	handle_print(t_coder *coder, char *message)
{
	long	curr_time;

	curr_time = current_time() - coder->monitor->init_time;
	pthread_mutex_lock(coder->monitor->print_lock);
	printf("%lu %i %s\n", curr_time, coder->n, message);
	pthread_mutex_unlock(coder->monitor->print_lock);
}

void	*track_burnout(void *arg)
{
	int			i;
	t_monitor	*monitor;
	int			remaining;

	monitor = (t_monitor *)arg;
	while (monitor->state)
	{
		i = 0;
		pthread_mutex_lock(monitor->compile_lock);
		remaining = monitor->remaining_compiles;
		pthread_mutex_unlock(monitor->compile_lock);
		if (remaining == 0)
			monitor->state = 0;
		else
		{
			while (i < monitor->number_of_coders)
			{
				if (monitor->coders[i].next_deadline <= current_time())
				{
					if (monitor->coders[i].remaining_compiles > 0)
					{
						handle_print(&monitor->coders[i], "burned out");
						monitor->state = 0;
						while (i < monitor->number_of_coders)
						{
							pthread_mutex_lock(monitor->dongles[i].lock);
							pthread_cond_broadcast(monitor->dongles[i].condition);
							pthread_mutex_unlock(monitor->dongles[i].lock);
							i++;
						}
						return (NULL);
					}
				}
				i++;
			}
			usleep(1000);
		}
	}
	return (NULL);
}
