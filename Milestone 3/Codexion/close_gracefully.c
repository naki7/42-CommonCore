/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   close_gracefully.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/12 10:31:43 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/18 11:18:01 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

void	*free_dongles(t_dongle *dongles, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		pthread_mutex_destroy(dongles[i].lock);
		free(dongles[i].lock);
		pthread_cond_destroy(dongles[i].condition);
		free(dongles[i].condition);
		free(dongles[i].queue);
		i++;
	}
	return (NULL);
}

void	*free_monitor(t_monitor *monitor)
{
	free_dongles(monitor->dongles, monitor->number_of_coders);
	free(monitor->dongles);
	free(monitor->coders);
	pthread_mutex_destroy(monitor->print_lock);
	free(monitor->print_lock);
	pthread_mutex_destroy(monitor->compile_lock);
	free(monitor->compile_lock);
	free(monitor);
	return (NULL);
}
