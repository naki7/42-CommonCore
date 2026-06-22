/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder_creator.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/18 17:04:01 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/22 11:07:16 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

pthread_t	thread_maker(void)
{
	pthread_t	thread;

	thread = 0;
	return (thread);
}

void	handle_coders(int *config, t_dongle *dongles, t_monitor *monitor,
						t_coder *coders)
{
	int			i;
	t_dongle	*left;
	t_dongle	*right;
	pthread_t	thread;

	i = 0;
	while (i < config[0])
	{
		left = &dongles[i];
		if (i == config[0] - 1)
			right = &dongles[0];
		else
			right = &dongles[i + 1];
		thread = thread_maker();
		coders[i] = (t_coder){i + 1, current_time() + config[1], config[5],
			thread, left, right, monitor};
		i++;
	}
}

t_coder	*assign_coders(int *config, t_dongle *dongles, t_monitor *monitor)
{
	t_coder		*coders;

	coders = malloc(sizeof(t_coder) * config[0]);
	if (!coders)
	{
		free_dongles(dongles, config[0]);
		free(dongles);
		return (NULL);
	}
	handle_coders(config, dongles, monitor, coders);
	return (coders);
}
