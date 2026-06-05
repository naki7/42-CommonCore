/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libcodexion.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/22 13:49:29 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/02 14:16:37 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBCODEXION_H
# define LIBCODEXION_H
# include <stdio.h>
# include <unistd.h>
# include <stdlib.h>
# include <string.h>
# include <pthread.h>
# include <sys/time.h>

typedef struct s_coder
{
	int					n;
	int					time_to_burnout;
	int					remaining_compiles;
	pthread_t			thread;
	struct s_dongle		*left;
	struct s_dongle		*right;
	struct s_monitor	*monitor;
}	t_coder;

typedef struct s_dongle
{
	int				usable;
	long			cooldown;
	long			usable_time;
	pthread_mutex_t	*lock;
	pthread_cond_t	*condition;
}	t_dongle;

typedef struct s_monitor
{
	int				state;
	int				number_of_coders;
	int				remaining_time;
	int				time_to_compile;
	int				time_to_debug;
	int				time_to_refactor;
	int				remaining_compiles;
	pthread_mutex_t	*print_lock;
	t_coder			*coders;
	t_dongle		*dongles;
}	t_monitor;

int		*parser(int argc, char *argv[], int *arguments);

void	*base_build(int *configs, char *priority);

void	*coder_loop(void *arg);
void	thread_init(t_monitor *monitor);

long	current_time(void);
void	wait_for_dongle(t_dongle *dongle);
void	grab_dongle(t_dongle *dongle, int coder_num, t_dongle *other);
void	release_dongle(t_dongle *dongle, int coder_num);

#endif
