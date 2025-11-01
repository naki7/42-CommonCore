/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_display_file.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/10 13:32:25 by joshde-s          #+#    #+#             */
/*   Updated: 2025/10/10 15:16:24 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <fcntl.h>

int	main(int argc, char *argv[])
{
	int		data;
	char	buff[4096];
	int		len;

	if (argc == 2)
	{
		data = open(argv[1], O_RDONLY);
		if (data < 0)
			write(1, "Cannot read file.\n", 18);
		len = read(data, buff, sizeof(buff));
		while (len > 0)
		{
			write(1, buff, len);
			len = read(data, buff, sizeof(buff));
		}
		close(data);
	}
	else
	{
		if (argc > 2)
			write(1, "Too many arguments.\n", 20);
		else
			write(1, "File name missing.\n", 19);
	}
	return (0);
}
