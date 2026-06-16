/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_actions.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 14:07:58 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/16 10:13:36 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

void	thread_init(t_monitor *monitor)
{
	int			i;

	i = 0;
	pthread_create(&monitor->burn_monitor, NULL, track_burnout, monitor);
	while (i < monitor->number_of_coders)
	{
		pthread_create(&monitor->coders[i].thread, NULL, coder_loop,
			&monitor->coders[i]);
		i++;
	}
	pthread_join(monitor->burn_monitor, NULL);
	i = 0;
	while (i < monitor->number_of_coders)
	{
		pthread_join(monitor->coders[i].thread, NULL);
		i++;
	}
}

void	*refactor(void *arg)
{
	t_coder			*coder;
	unsigned int	timer;

	coder = (t_coder *)arg;
	if (coder->monitor->state != 0)
	{
		timer = coder->monitor->time_to_refactor;
		handle_print(coder, "is refactoring");
		usleep(timer * 1000);
	}
	return (NULL);
}

void	*debug(void *arg)
{
	t_coder			*coder;
	unsigned int	timer;

	coder = (t_coder *)arg;
	if (coder->monitor->state != 0)
	{
		timer = coder->monitor->time_to_debug;
		handle_print(coder, "is debugging");
		usleep(timer * 1000);
	}
	return (NULL);
}

void	*compile(void *arg)
{
	t_coder			*coder;
	unsigned int	timer;
	t_dongle		*left;
	t_dongle		*right;

	coder = (t_coder *)arg;
	timer = coder->monitor->time_to_compile;
	left = coder->left;
	right = coder->right;
	coder->next_deadline = current_time() + coder->monitor->time_to_burnout;
	handle_print(coder, "is compiling");
	usleep(timer * 1000);
	coder->remaining_compiles--;
	release_dongle(right);
	release_dongle(left);
	return (NULL);
}

void	*coder_loop(void *arg)
{
	t_coder		*code_arg;
	int			right_acquired;
	int			left_acquired;

	code_arg = (t_coder *)arg;
	right_acquired = 0;
	left_acquired = 0;
	while (code_arg->monitor->state && code_arg->remaining_compiles > 0)
	{
		right_acquired = 0;
		left_acquired = 0;
		if (code_arg->n % 2 == 0)
		{
			right_acquired = grab_dongle(code_arg->right, code_arg);
			if (right_acquired == -1 || !code_arg->monitor->state)
				break ;
			left_acquired = grab_dongle(code_arg->left, code_arg);
			if (left_acquired == -1 || !code_arg->monitor->state)
			{
				if (right_acquired == 0)
					release_dongle(code_arg->right);
				break ;
			}
		}
		else
		{
			left_acquired = grab_dongle(code_arg->left, code_arg);
			if (left_acquired == -1 || !code_arg->monitor->state)
				break ;
			right_acquired = grab_dongle(code_arg->right, code_arg);
			if (right_acquired == -1 || !code_arg->monitor->state)
			{
				if (left_acquired == 0)
					release_dongle(code_arg->left);
				break ;
			}
		}
		compile(code_arg);
		if (code_arg->remaining_compiles < 1)
			break ;
		debug(code_arg);
		refactor(code_arg);
	}
	if (code_arg->remaining_compiles < 1)
		handle_print(code_arg, "finished with 0 remaining compiles");
	pthread_mutex_lock(code_arg->monitor->compile_lock);
	if (code_arg->monitor->state != 0)
		code_arg->monitor->remaining_compiles--;
	pthread_mutex_unlock(code_arg->monitor->compile_lock);
	return (NULL);
}
