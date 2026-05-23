/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libcodexion.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/22 13:49:29 by joshde-s          #+#    #+#             */
/*   Updated: 2026/05/23 18:27:59 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBCODEXION_H
# define LIBCODEXION_H
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <pthread.h>

typedef struct s_coder
{
	int				n;
	int				remaining_time;
	pthread_t		thread;
	struct s_dongle	*left;
	struct s_dongle	*right;
}	t_coder;

typedef struct s_dongle
{
	int				usable;
	int				cooldown;
	pthread_mutex_t	lock;
	pthread_cond_t	condition;
}	t_dongle;

typedef struct s_monitor
{
	int				state;
	int				number_of_coders;
	int				time_to_burnout;
	int				time_to_compile;
	int				time_to_debug;
	int				time_to_refactor;
	pthread_mutex_t	print_lock;
	t_coder			*coders;
	t_dongle		*dongles;
}	t_monitor;

int		*parser(int argc, char *argv[], int *arguments);

void	*base_build(int *configs, char *priority);

#endif
