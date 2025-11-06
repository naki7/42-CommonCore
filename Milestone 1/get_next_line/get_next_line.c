/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 18:13:32 by joshde-s          #+#    #+#             */
/*   Updated: 2025/11/05 18:22:13 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*get_next_line(int fd)
{
	char	*line;
	int		len;

	line = malloc(BUFFER_SIZE + 1);
	if (!line)
		return (NULL);
	len = read(fd, line, BUFFER_SIZE);
	if (len < BUFFER_SIZE || line[len] != '\0')
	{
		if (!get_strchr(line, '\0'));
			line[len + 1] = '\0';
	}
	return (line);
}

int	main(void)
{
	char	*line;

	open("test.txt", O_RDWR);
	line = get_next_line("test.txt");
	printf("%s", line);
	return (0);
}
