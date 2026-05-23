/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libcodexion.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/22 13:49:29 by joshde-s          #+#    #+#             */
/*   Updated: 2026/05/23 10:37:55 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBCODEXION_H
# define LIBCODEXION_H
# include <stdio.h>
# include <stdlib.h>
# include <string.h>

typedef struct s_stack
{
	int				value;
	struct s_stack	*next;
}	t_stack;

int	*parser(int argc, char *argv[], int *arguments);

#endif
