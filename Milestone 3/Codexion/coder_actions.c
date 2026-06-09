/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_actions.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 14:07:58 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/09 11:35:12 by joshde-s         ###   ########.fr       */
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
	handle_print(coder);
	printf("%i is refactoring\n", coder->n);
	pthread_mutex_unlock(coder->monitor->print_lock);
	usleep(timer * 1000);
	return (NULL);
}

void	*debug(void *arg)
{
	t_coder			*coder;
	unsigned int	timer;

	coder = (t_coder *)arg;
	timer = coder->monitor->time_to_debug;
	handle_print(coder);
	printf("%i is debugging\n", coder->n);
	pthread_mutex_unlock(coder->monitor->print_lock);
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
	handle_print(coder);
	printf("%i is compiling\n", coder->n);
	pthread_mutex_unlock(coder->monitor->print_lock);
	usleep(timer * 1000);
	coder->remaining_compiles--;
	release_dongle(right, coder->n);
	release_dongle(left, coder->n);
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
			grab_dongle(code_arg->right, code_arg->n, code_arg);
			grab_dongle(code_arg->left, code_arg->n, code_arg);
		}
		else
		{
			grab_dongle(code_arg->left, code_arg->n, code_arg);
			grab_dongle(code_arg->right, code_arg->n, code_arg);
		}
		compile(code_arg);
		if (code_arg->remaining_compiles < 1)
			break ;
		debug(code_arg);
		refactor(code_arg);
	}
	handle_print(code_arg);
	printf("coder %i finished with %i remaining cycles\n", code_arg->n,
		code_arg->remaining_compiles);
	pthread_mutex_unlock(code_arg->monitor->print_lock);
	code_arg->monitor->remaining_compiles--;
	return (NULL);
}
