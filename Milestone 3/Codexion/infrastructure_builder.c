/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   infrastructure_builder.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/22 12:23:56 by joshde-s          #+#    #+#             */
/*   Updated: 2026/05/23 18:35:17 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

# include "libcodexion.h"

t_coder		*assign_coders(int coder_num, int burnout_time);

t_dongle	*assign_dongles(int cooldown);

void	*base_build(int *configs, char *priority)
{
	t_coder			*coders;
	t_dongle		*dongles;
	t_monitor		*monitor;
	pthread_mutex_t	print_lock;

	pthread_mutex_init(&print_lock, NULL);
	coders = assign_coders(configs[0], configs[1]);
	dongles = assign_dongles(configs[6]);
	monitor = (t_monitor *)(1, configs[0], configs[1], configs[2], configs[3], configs[4], coders, dongles);
}
