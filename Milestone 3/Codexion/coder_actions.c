/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_actions.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 14:07:58 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/19 11:31:37 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

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
