/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_actions.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 14:07:58 by joshde-s          #+#    #+#             */
/*   Updated: 2026/05/28 17:26:24 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

void	thread_init(t_monitor *monitor)
{
	int			i;
	t_grouper	*curr_group;

	i = 0;
	curr_group = malloc(sizeof(t_grouper));
	curr_group->remaining_time = monitor->remaining_time;
	curr_group->time_to_compile = monitor->time_to_compile;
	curr_group->time_to_debug = monitor->time_to_debug;
	curr_group->time_to_refactor = monitor->time_to_refactor;
	curr_group->print_lock = monitor->print_lock;
	while (i < monitor->number_of_coders)
	{
		curr_group->coder = monitor->coders[i];
		pthread_create(&curr_group->coder.thread, NULL, compile, curr_group);
		i++;
	}
	i = 0;
	while (i < monitor->number_of_coders)
	{
		usleep(curr_group->time_to_refactor);
		printf("i%i\n", i);
		curr_group->coder = monitor->coders[i++];
		pthread_join(curr_group->coder.thread, NULL);
	}
}

void	*refactor(void *arg)
{
	t_grouper		*group;
	unsigned int	timer;

	group = (t_grouper *)arg;
	timer = group->time_to_refactor;
	usleep(timer);
	printf("refactor - %i\n", group->coder.n);
	compile(group);
	return (NULL);
}

void	*debug(void *arg)
{
	t_grouper		*group;
	unsigned int	timer;

	group = (t_grouper *)arg;
	timer = group->time_to_debug;
	usleep(timer);
	printf("debug - %i\n", group->coder.n);
	refactor(group);
	return (NULL);
}

void	*compile(void *arg)
{
	t_grouper		*group;
	unsigned int	timer;
	t_dongle		*left;

	group = (t_grouper *)arg;
	timer = group->time_to_compile;
	left = group->coder.left;
	pthread_mutex_lock(&left->lock);
	if (left->usable == 0)
		pthread_cond_wait(&left->condition, &left->lock);
	dongle_refresh(left);
	usleep(timer);
	printf("compile - %i\n", group->coder.n);
	pthread_mutex_unlock(&group->coder.left->lock);
	debug(group);
	return (NULL);
}
