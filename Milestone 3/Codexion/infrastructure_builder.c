/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   infrastructure_builder.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/22 12:23:56 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/12 16:08:52 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

t_dongle	dongle_maker(int cooldown, char *priority)
{
	t_dongle	dongle;

	dongle.usable = 1;
	dongle.cooldown = cooldown;
	dongle.usable_time = current_time();
	dongle.lock = malloc(sizeof(pthread_mutex_t));
	if (dongle.lock == NULL)
		return (dongle);
	pthread_mutex_init(dongle.lock, NULL);
	dongle.condition = malloc(sizeof(pthread_cond_t));
	if (dongle.condition == NULL)
		{
			free(dongle.lock);
			return (dongle);
		}
	pthread_cond_init(dongle.condition, NULL);
	dongle.queue = malloc(sizeof(t_request) * 2);
	if (dongle.queue == NULL)
		{
			free(dongle.lock);
			free(dongle.condition);
			return (dongle);
		}
	dongle.queue_size = 0;
	dongle.priority = priority;
	return (dongle);
}

t_dongle	*assign_dongles(int dong_num, int cooldown, char *priority)
{
	int				i;
	t_dongle		*dongles;

	i = 0;
	dongles = malloc(sizeof(t_dongle) * dong_num);
	if (!dongles)
		return (NULL);
	while (i < dong_num)
	{
		dongles[i] = dongle_maker(cooldown, priority);
		if (dongles[i].lock == NULL || dongles[i].condition == NULL ||
			dongles[i].queue == NULL)
			return (free_dongles(dongles, i));
		i++;
	}
	return (dongles);
}

pthread_t	thread_maker(void)
{
	pthread_t	thread;

	thread = 0;
	return (thread);
}

t_coder	*assign_coders(int *config, t_dongle *dongles, t_monitor *monitor)
{
	int			i;
	t_coder		*coders;
	t_dongle	*left;
	t_dongle	*right;
	pthread_t	thread;

	i = 0;
	coders = malloc(sizeof(t_coder) * config[0]);
	if (!coders)
	{
		free(dongles);
		return (free_dongles(dongles, config[0]));
	}
	while (i < config[0])
	{
		left = &dongles[i];
		if (i == config[0] - 1)
			right = &dongles[0];
		else
			right = &dongles[i + 1];
		thread = thread_maker();
		coders[i] = (t_coder){i + 1, current_time() + config[1], config[5],
			thread, left, right, monitor};
		i++;
	}
	return (coders);
}

void	*base_build(int *configs, char *priority)
{
	t_coder			*coders;
	t_dongle		*dongles;
	t_monitor		*monitor;

	monitor = malloc(sizeof(t_monitor));
	if (monitor == NULL)
		return (NULL);
	monitor->print_lock = NULL;
	dongles = assign_dongles(configs[0], configs[6], priority);
	if (dongles == NULL)
		return (monitor);
	monitor->init_time = current_time();
	coders = assign_coders(configs, dongles, monitor);
	if (coders == NULL)
		return (monitor);
	monitor->state = 1;
	monitor->number_of_coders = configs[0];
	monitor->time_to_burnout = configs[1];
	monitor->time_to_compile = configs[2];
	monitor->time_to_debug = configs[3];
	monitor->time_to_refactor = configs[4];
	monitor->remaining_compiles = configs[5];
	monitor->print_lock = malloc(sizeof(pthread_mutex_t));
	if (monitor->print_lock == NULL)
		return (monitor);//add to codexion main to check if print_lock is null
	pthread_mutex_init(monitor->print_lock, NULL);
	monitor->coders = coders;
	monitor->dongles = dongles;
	monitor->burn_monitor = thread_maker();
	thread_init(monitor);
	return (monitor);
}
