/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/22 12:22:46 by joshde-s          #+#    #+#             */
/*   Updated: 2026/05/23 15:06:18 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libcodexion.h"

int	*handle_error(int err_code, int *arguments)
{
	if (err_code == 1)
		printf("Invalid item used in first 7 arguments, use an int\n");
	else if (err_code == 2)
		printf("Invalid input used for <scheduler>, use \"fifo\" | \"edf\"\n");
	arguments[0] = -1;
	return (arguments);
}

void	*handle_too_few_args(int argc, int *arguments)
{
	char	*messages[8];
	int		i;

	messages[0] = "<number_of_coders>";
	messages[1] = "<time_to_burnout>";
	messages[2] = "<time_to_compile>";
	messages[3] = "<time_to_debug>";
	messages[4] = "<time_to_refactor>";
	messages[5] = "<number_of_compiles_required>";
	messages[6] = "<dongle_cooldown>";
	messages[7] = "<scheduler>";
	printf("Missing ");
	i = argc - 1;
	while (i < 8)
	{
		printf("%s", messages[i]);
		i++;
		if (i < 8)
			printf(" ");
	}
	printf("\n");
	return (handle_error(0, arguments));
}

int	validate_args(char *argv[])
{
	int	i;
	int	j;

	i = 1;
	while (i < 8)
	{
		j = 0;
		while (argv[i][j] != '\0')
		{
			if (argv[i][j] < 48 || argv[i][j] > 57)
				return (1);
			j++;
		}
		if (atoi(argv[i]) < 1)
			return (1);
		i++;
	}
	if (strcmp(argv[7], "fifo") == 0 || strcmp(argv[7], "edf") == 0)
		return (2);
	return (3);
}

int	*save_args(char *argv[], int *arguments)
{
	int	i;

	i = 0;
	while (i < 8)
	{
		arguments[i] = atoi(argv[i + 1]);
		i++;
	}
	return (arguments);
}

int	*parser(int argc, char *argv[], int *arguments)
{
	int	validate_code;

	if (argc < 9)
		handle_too_few_args(argc, arguments);
	else
	{
		validate_code = validate_args(argv);
		if (validate_code != 3)
			handle_error(validate_code, arguments);
		else
			save_args(argv, arguments);
	}
	return (arguments);
}
