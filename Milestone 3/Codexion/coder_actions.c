/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_actions.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 14:07:58 by joshde-s          #+#    #+#             */
/*   Updated: 2026/05/29 15:53:56 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

void	thread_init(t_monitor *monitor)
{
	int			i;
	t_grouper	*groups;

	i = 0;
	groups = malloc(sizeof(t_grouper) * monitor->number_of_coders);
	while (i < monitor->number_of_coders)
	{
		groups[i].coder = &monitor->coders[i];
		groups[i].remaining_time = monitor->remaining_time;
		groups[i].time_to_compile = monitor->time_to_compile;
		groups[i].time_to_debug = monitor->time_to_debug;
		groups[i].time_to_refactor = monitor->time_to_refactor;
		groups[i].print_lock = &monitor->print_lock;
		pthread_create(&groups[i].coder->thread, NULL, coder_loop, &groups[i]);
		i++;
	}
	while (i < monitor->number_of_coders)
	{
		usleep(groups[i].time_to_refactor);
		printf("i%i\n", i);
		groups[i].coder = &monitor->coders[i];
		pthread_join(groups[i].coder->thread, NULL);
		i++;
	}
}

void	*refactor(void *arg)
{
	t_grouper		*group;
	unsigned int	timer;

	group = (t_grouper *)arg;
	timer = group->time_to_refactor;
	usleep(timer);
	printf("refactor - %i\n", group->coder->n);
	return (NULL);
}

void	*debug(void *arg)
{
	t_grouper		*group;
	unsigned int	timer;

	group = (t_grouper *)arg;
	timer = group->time_to_debug;
	usleep(timer);
	printf("debug - %i\n", group->coder->n);
	return (NULL);
}

void	*compile(void *arg)
{
	t_grouper		*group;
	unsigned int	timer;
	t_dongle		*left;
	struct timeval	tv;

	group = (t_grouper *)arg;
	timer = group->time_to_compile;
	left = group->coder->left;
	pthread_mutex_lock(&left->lock);
	printf("%i grabs their left dongle\n", group->coder->n);
	dongle_refresh(left);
	gettimeofday(&tv, NULL);
	if (left->usable_time >= tv.tv_sec)
		pthread_cond_wait(&left->condition, &left->lock);
	printf("compile - %i\n", group->coder->n);
	pthread_mutex_unlock(&left->lock);
	printf("%i lets go of their left dongle\n", group->coder->n);
	return (NULL);
}

void	*coder_loop(void *arg)
{
	t_grouper	*code_arg;
	int			running;

	code_arg = (t_grouper *)arg;
	running = 1;
	while (running)
	{
		compile(code_arg);
		debug(code_arg);
		refactor(code_arg);
	}
	printf("%i\n", running);
	return (NULL);
}
