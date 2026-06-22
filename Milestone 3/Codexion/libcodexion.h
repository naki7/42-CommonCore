/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libcodexion.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/22 13:49:29 by joshde-s          #+#    #+#             */
/*   Updated: 2026/06/22 11:06:27 by joshde-s         ###   ########.fr       */
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

typedef struct s_request
{
	int					coder_num;
	long				join_time;
	long				next_deadline;
}	t_request;

typedef struct s_coder
{
	int					n;
	long				next_deadline;
	int					remaining_compiles;
	pthread_t			thread;
	struct s_dongle		*left;
	struct s_dongle		*right;
	struct s_monitor	*monitor;
}	t_coder;

typedef struct s_dongle
{
	int					usable;
	long				cooldown;
	long				usable_time;
	pthread_mutex_t		*lock;
	pthread_cond_t		*condition;
	struct s_request	*queue;
	int					queue_size;
	char				*priority;
}	t_dongle;

typedef struct s_monitor
{
	int				state;
	int				number_of_coders;
	long			time_to_burnout;
	long			time_to_compile;
	long			time_to_debug;
	long			time_to_refactor;
	int				remaining_compiles;
	long			init_time;
	pthread_mutex_t	*print_lock;
	pthread_mutex_t	*compile_lock;
	t_coder			*coders;
	t_dongle		*dongles;
	pthread_t		burn_monitor;
}	t_monitor;

int			*parser(int argc, char *argv[], int *arguments);

void		*base_build(int *configs, char *priority);

t_coder		*assign_coders(int *config, t_dongle *dongles, t_monitor *monitor);
pthread_t	thread_maker(void);

void		thread_init(t_monitor *monitor);
void		*coder_loop(void *arg);

void		*compile(void *arg);
void		*debug(void *arg);
void		*refactor(void *arg);

long		current_time(void);
void		wait_for_dongle(t_dongle *dongle, int coder_num,
				t_monitor *monitor);
int			grab_dongle(t_dongle *dongle, t_coder *coder);
void		release_dongle(t_dongle *dongle);

void		handle_print(t_coder *coder, char *message);
void		*track_burnout(void *arg);

void		*free_dongles(t_dongle *dongles, int size);
void		*free_monitor(t_monitor *monitor);

#endif
