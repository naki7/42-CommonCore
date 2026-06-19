/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   infrastructure_builder.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/22 12:23:56 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/19 11:47:14 by joshde-s         ###   ########.fr       */
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
		if (dongles[i].lock == NULL || dongles[i].condition == NULL)
			return (free_dongles(dongles, i));
		else if (dongles[i].queue == NULL)
			return (free_dongles(dongles, i));
		i++;
	}
	return (dongles);
}

int	build_monitor(t_monitor *monitor, t_coder *coders, t_dongle *dongles,
		int *configs)
{
	monitor->state = 1;
	monitor->number_of_coders = configs[0];
	monitor->time_to_burnout = configs[1];
	monitor->time_to_compile = configs[2];
	monitor->time_to_debug = configs[3];
	monitor->time_to_refactor = configs[4];
	monitor->remaining_compiles = configs[0];
	monitor->print_lock = malloc(sizeof(pthread_mutex_t));
	if (monitor->print_lock == NULL)
		return (-1);
	pthread_mutex_init(monitor->print_lock, NULL);
	monitor->compile_lock = malloc(sizeof(pthread_mutex_t));
	if (monitor->compile_lock == NULL)
		return (-1);
	pthread_mutex_init(monitor->compile_lock, NULL);
	monitor->coders = coders;
	monitor->dongles = dongles;
	monitor->burn_monitor = thread_maker();
	return (0);
}

void	*base_build(int *configs, char *priority)
{
	t_coder			*coders;
	t_dongle		*dongles;
	t_monitor		*monitor;
	int				result;

	result = 0;
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
	result = build_monitor(monitor, coders, dongles, configs);
	if (result == -1)
		return (monitor);
	thread_init(monitor);
	return (monitor);
}
