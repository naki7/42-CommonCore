/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_actions.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 14:07:58 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/02 15:53:30 by joshde-s         ###   ########.fr       */
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
	usleep(monitor->remaining_time * 1000);
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
	printf("%i is refactoring\n", coder->n);
	usleep(timer * 1000);
	return (NULL);
}

void	*debug(void *arg)
{
	t_coder			*coder;
	unsigned int	timer;

	coder = (t_coder *)arg;
	timer = coder->monitor->time_to_debug;
	printf("%i is debugging\n", coder->n);
	usleep(timer * 1000);
	return (NULL);
}

void	*compile(void *arg)
{
	t_coder			*coder;
	unsigned int	timer;
	t_dongle		*left;
	//t_dongle		*right;

	coder = (t_coder *)arg;
	timer = coder->monitor->time_to_compile;
	left = coder->left;
	//right = coder->right;
	printf("%i is compiling\n", coder->n);
	usleep(timer * 1000);
	coder->remaining_compiles--;
	//release_dongle(right, coder->n);
	release_dongle(left, coder->n);
	return (NULL);
}

void	*coder_loop(void *arg)
{
	t_coder		*code_arg;
	int			cycles;

	code_arg = (t_coder *)arg;
	while (code_arg->monitor->state)
	{
		if (code_arg->remaining_compiles <= 0)
			break ;
		grab_dongle(code_arg->left, code_arg->n);
		//grab_dongle(code_arg->right, code_arg->n);
		compile(code_arg);
		debug(code_arg);
		refactor(code_arg);
	}
	cycles = code_arg->remaining_compiles;
	printf("coder %i finished with %i remaining cycles\n", code_arg->n,
		cycles);
	return (NULL);
}
