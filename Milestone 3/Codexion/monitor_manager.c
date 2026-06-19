/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitor_manager.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 16:31:15 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/18 15:06:15 by joshde-s         ###   ########.fr       */
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

void	handle_burnout(t_monitor *monitor, t_coder *coder)
{
	int	i;

	i = 0;
	monitor->state = 0;
	handle_print(coder, "burned out");
	while (i < monitor->number_of_coders)
	{
		pthread_mutex_lock(monitor->dongles[i].lock);
		monitor->dongles->cooldown = 0;
		pthread_cond_broadcast(monitor->dongles[i].condition);
		pthread_mutex_unlock(monitor->dongles[i].lock);
		i++;
	}
}

void	*check_coders(t_monitor *monitor)
{
	int	i;

	i = 0;
	while (i < monitor->number_of_coders)
	{
		if (monitor->coders[i].next_deadline <= current_time())
		{
			if (monitor->coders[i].remaining_compiles > 0)
			{
				handle_burnout(monitor, &monitor->coders[i]);
				return (NULL);
			}
		}
		i++;
	}
	usleep(1000);
	return (monitor);
}

void	*track_burnout(void *arg)
{
	t_monitor	*monitor;
	int			remaining;

	monitor = (t_monitor *)arg;
	while (monitor->state)
	{
		pthread_mutex_lock(monitor->compile_lock);
		remaining = monitor->remaining_compiles;
		pthread_mutex_unlock(monitor->compile_lock);
		if (remaining < 1)
			monitor->state = 0;
		else if (check_coders(monitor) == NULL)
			return (NULL);
	}
	return (NULL);
}
