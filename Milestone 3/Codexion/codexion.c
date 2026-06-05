/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/22 11:31:51 by joshde-s          #+#    #+#             */
/*   Updated: 2026/05/29 15:27:44 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

int	main(int argc, char *argv[])
{
	int		arguments[8];
	char		*priority;
	int			i;
	t_monitor	*monitor;

	i = 0;
	parser(argc, argv, arguments);
	if (arguments[0] == -1)
		return (0);
	priority = argv[8];
	monitor = base_build(arguments, priority);
	return (1);
}
