/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_actions.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 14:07:58 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/12 15:45:06 by joshde-s         ###   ########.fr       */
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
	timer = coder->monitor->time_to_refactor;
	handle_print(coder, "is refactoring");
	usleep(timer * 1000);
	return (NULL);
}

void	*debug(void *arg)
{
	t_coder			*coder;
	unsigned int	timer;

	coder = (t_coder *)arg;
	timer = coder->monitor->time_to_debug;
	handle_print(coder, "is debugging");
	usleep(timer * 1000);
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

	code_arg = (t_coder *)arg;
	while (code_arg->monitor->state && code_arg->remaining_compiles > 0)
	{
		if (code_arg->n % 2 == 0)
		{
			grab_dongle(code_arg->right, code_arg);
			grab_dongle(code_arg->left, code_arg);
		}
		else
		{
			grab_dongle(code_arg->left, code_arg);
			grab_dongle(code_arg->right, code_arg);
		}
		compile(code_arg);
		if (code_arg->remaining_compiles < 1)
			break ;
		debug(code_arg);
		refactor(code_arg);
	}
	handle_print(code_arg, "finished with 0 remaining compiles");
	code_arg->monitor->remaining_compiles--;
	return (NULL);
}
