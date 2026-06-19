/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/22 11:31:51 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/18 14:17:52 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

int	main(int argc, char *argv[])
{
	int			arguments[8];
	char		*priority;
	t_monitor	*monitor;

	parser(argc, argv, arguments);
	if (arguments[0] == -1)
		return (0);
	priority = argv[8];
	monitor = base_build(arguments, priority);
	if (monitor == NULL)
	{
		printf("Error while malloc'ing the monitor");
		return (0);
	}
	else if (monitor->print_lock == NULL)
	{
		printf("Error while malloc'ing the dongles/coders");
		free(monitor);
		return (0);
	}
	free_monitor(monitor);
	return (1);
}
