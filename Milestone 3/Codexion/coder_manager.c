/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_manager.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/19 11:02:48 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/22 11:10:17 by joshde-s         ###   ########.fr       */
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

void	reduce_compiles(t_coder *code_arg)
{
	pthread_mutex_lock(code_arg->monitor->compile_lock);
	if (code_arg->monitor->state != 0)
		code_arg->monitor->remaining_compiles--;
	pthread_mutex_unlock(code_arg->monitor->compile_lock);
}

int	handle_even(t_coder *code_arg, int *left, int *right)
{
	*right = grab_dongle(code_arg->right, code_arg);
	if (*right == -1 || !code_arg->monitor->state)
		return (-1);
	*left = grab_dongle(code_arg->left, code_arg);
	if (*left == -1 || !code_arg->monitor->state)
	{
		if (*right == 0)
			release_dongle(code_arg->right);
		return (-1);
	}
	return (0);
}

int	handle_odd(t_coder *code_arg, int *left, int *right)
{
	*left = grab_dongle(code_arg->left, code_arg);
	if (*left == -1 || !code_arg->monitor->state)
		return (-1);
	*right = grab_dongle(code_arg->right, code_arg);
	if (*right == -1 || !code_arg->monitor->state)
	{
		if (*left == 0)
			release_dongle(code_arg->left);
		return (-1);
	}
	return (0);
}

void	*coder_loop(void *arg)
{
	t_coder		*code_arg;
	int			right_acquired;
	int			left_acquired;
	int			result;

	code_arg = (t_coder *)arg;
	while (code_arg->monitor->state && code_arg->remaining_compiles > 0)
	{
		right_acquired = 0;
		left_acquired = 0;
		if (code_arg->n % 2 == 0)
			result = handle_even(code_arg, &left_acquired, &right_acquired);
		else
			result = handle_odd(code_arg, &left_acquired, &right_acquired);
		if (result == -1)
			break ;
		compile(code_arg);
		if (code_arg->remaining_compiles < 1)
			break ;
		debug(code_arg);
		refactor(code_arg);
	}
	reduce_compiles(code_arg);
	return (NULL);
}
