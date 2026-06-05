#include "libcodexion.h"

void	locked_print(pthread_mutex_t *lock, int num)
{
	pthread_mutex_lock(lock);
	printf("%i just printed\n", num);
	pthread_mutex_unlock(lock);
}

void	grab_one(t_dongle *dongle, char *side, int num)
{
	pthread_mutex_lock(&dongle->lock);

	while (dongle->usable != 1)
		pthread_cond_wait(&dongle->condition, &dongle->lock);
	printf("%i grabbed the %s dongle\n", num, side);
	dongle->usable = 0;
	pthread_mutex_unlock(&dongle->lock);
}

int	main(void)
{
	t_coder	coder1;
	t_coder	coder2;
	int		run;
	int		stop_i;
	pthread_t	thread1 = 0;
	pthread_t	thread2 = 0;
	t_dongle	left;
	t_dongle	right;
	pthread_mutex_t	left_lock;
	pthread_mutex_t	right_lock;
	pthread_cond_t	condition;
	pthread_mutex_t	print_lock;

	run = 1;
	pthread_mutex_init(&left_lock, NULL);
	pthread_mutex_init(&right_lock, NULL);
	pthread_mutex_init(&print_lock, NULL);
	pthread_cond_init(&condition, NULL);
	left = (t_dongle){1, 1, left_lock, condition};
	right = (t_dongle){1, 1, right_lock, condition};
	coder1 = (t_coder){1, 10, thread1, &left, &right};
	coder2 = (t_coder){2, 10, thread2, &right, &left};
	stop_i = (coder1.n + coder2.n) * 3;
	while (run)
	{
		left.usable = 1;
		right.usable = 1;
		if (stop_i % 2 == 0)
		{
			grab_one(&left, "left", coder1.n);
			grab_one(&right, "right", coder1.n);
			if (left.usable == 1 && right.usable == 1)
				locked_print(&print_lock, coder1.n);
		}
		else
		{
			grab_one(&left, "left", coder2.n);
			grab_one(&right, "right", coder2.n);
			if (left.usable == 1 && right.usable == 1)
				locked_print(&print_lock, coder2.n);
		}
		stop_i--;
		if (stop_i == 0)
			run = 0;
	}
}
