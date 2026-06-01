/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_actions.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 14:07:58 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/01 12:11:04 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

void	thread_init(t_monitor *monitor)
{
	int			i;

	i = 0;
	while (i < monitor->number_of_coders)
	{
		pthread_create(&monitor->coders[i].thread, NULL, coder_loop,
			&monitor->coders[i]);
		i++;
	}
	i = 0;
	while (i < monitor->number_of_coders)
	{
		printf("i%i\n", i);
		pthread_join(monitor->coders[i].thread, NULL);
		i++;
	}
}

void	*refactor(void *arg)
{
	t_coder			*coder;
	unsigned int	timer;

	coder = (t_coder *)arg;
	timer = coder->monitor->time_to_refactor;
	usleep(timer * 1000);
	printf("refactor - %i\n", coder->n);
	return (NULL);
}

void	*debug(void *arg)
{
	t_coder			*coder;
	unsigned int	timer;

	coder = (t_coder *)arg;
	timer = coder->monitor->time_to_debug;
	usleep(timer * 1000);
	printf("debug - %i\n", coder->n);
	return (NULL);
}

void	*compile(void *arg)
{
	t_coder			*coder;
	unsigned int	timer;
	t_dongle		*left;
	struct timeval	tv;

	coder = (t_coder *)arg;
	timer = coder->monitor->time_to_compile;
	left = coder->left;
	pthread_mutex_lock(left->lock);
	printf("%i grabs their left dongle\n", coder->n);
	dongle_refresh(left);
	gettimeofday(&tv, NULL);
	if (left->usable_time >= tv.tv_sec)
		pthread_cond_wait(left->condition, left->lock);
	usleep(timer * 1000);
	printf("compile - %i\n", coder->n);
	pthread_mutex_unlock(left->lock);
	printf("%i lets go of their left dongle\n", coder->n);
	return (NULL);
}

void	*coder_loop(void *arg)
{
	t_coder		*code_arg;
	int			running;

	code_arg = (t_coder *)arg;
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
