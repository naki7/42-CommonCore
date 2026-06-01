/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   infrastructure_builder.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/22 12:23:56 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/01 12:02:52 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

t_dongle	dongle_maker(int cooldown)
{
	t_dongle		dongle;
	struct timeval	tv;

	dongle.usable = 1;
	dongle.cooldown = cooldown;
	gettimeofday(&tv, NULL);
	dongle.usable_time = tv.tv_sec;
	dongle.lock = malloc(sizeof(pthread_mutex_t));
	pthread_mutex_init(dongle.lock, NULL);
	dongle.condition = malloc(sizeof(pthread_cond_t));
	pthread_cond_init(dongle.condition, NULL);
	return (dongle);
}

t_dongle	*assign_dongles(int dong_num, int cooldown)
{
	int				i;
	t_dongle		*dongles;

	i = 0;
	dongles = malloc(sizeof(t_dongle) * dong_num);
	if (!dongles)
		return (NULL);
	while (i < dong_num)
	{
		dongles[i] = dongle_maker(cooldown);
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
		return (NULL);
	while (i < config[0])
	{
		left = &dongles[i];
		if (i == config[0] - 1)
			right = &dongles[0];
		else
			right = &dongles[i + 1];
		thread = thread_maker();
		coders[i] = (t_coder){i + 1, config[1], thread, left, right, monitor};
		i++;
	}
	return (coders);
}

void	*base_build(int *configs, char *priority)
{
	t_coder			*coders;
	t_dongle		*dongles;
	t_monitor		*monitor;
	(void)priority;

	monitor = malloc(sizeof(t_monitor));
	dongles = assign_dongles(configs[0], configs[6]);
	coders = assign_coders(configs, dongles, monitor);
	monitor->state = 1;
	monitor->number_of_coders = configs[0];
	monitor->remaining_time = configs[1];
	monitor->time_to_compile = configs[2];
	monitor->time_to_debug = configs[3];
	monitor->time_to_refactor = configs[4];
	monitor->print_lock = malloc(sizeof(pthread_mutex_t));
	pthread_mutex_init(monitor->print_lock, NULL);
	monitor->coders = coders;
	monitor->dongles = dongles;
	thread_init(monitor);
	return (monitor);
}
