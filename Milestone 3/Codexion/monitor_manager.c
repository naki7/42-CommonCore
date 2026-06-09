/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitor_manager.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 16:31:15 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/09 11:28:31 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

void	handle_print(t_coder *coder)
{
	int		curr_time;

	curr_time = current_time() - coder->monitor->init_time;
	pthread_mutex_lock(coder->monitor->print_lock);
	printf("%i ", curr_time / 1000);
}

// void	burnout_monitor(t_monitor *monitor)
// {
// 	int	original_count;
// 	int	curr_count;

// 	original_count = monitor->number_of_coders;
// 	curr_count = 0;
// 	while (curr_count <= original_count)
// 	{
// 		if (monitor->remaining_compiles < 1)
// 			break ;
// 		if (monitor->coders[curr_count].time_to_burnout <= current_time())
// 		{
// 			if (monitor->coders[curr_count].remaining_compiles > 0)
// 			{
// 				printf("%i burned out\n", curr_count + 1);
// 				exit(0);
// 			}
// 		}
// 		original_count++;
// 		if (curr_count > original_count)
// 			curr_count = 0;
// 	}
// }
