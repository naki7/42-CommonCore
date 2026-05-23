/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/22 11:31:51 by joshde-s          #+#    #+#             */
/*   Updated: 2026/05/23 10:44:58 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

int	main(int argc, char *argv[])
{
	int		arguments[7];
	char	*priority;
	int		i;

	i = 0;
	*arguments = *parser(argc, argv, arguments);
	if (arguments[0] == -1)
		return (0);
	priority = argv[8];
	while (i < 7)
	{
		printf("%i\n", arguments[i]);
		i++;
	}
	if (i == 7)
		printf("%s\n", priority);
	return (1);
}
