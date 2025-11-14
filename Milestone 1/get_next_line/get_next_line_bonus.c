/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 18:13:32 by joshde-s          #+#    #+#             */
/*   Updated: 2025/11/10 19:18:13 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

char	*get_init_line(int fd, char *line)
{
	char	*addline;
	int		len;

	len = 1;
	addline = NULL;
	while (!get_strchr(addline) && len != 0)
	{
		free(addline);
		addline = get_calloc(BUFFER_SIZE + 1, sizeof(char));
		if (!addline)
			return (NULL);
		len = read(fd, addline, BUFFER_SIZE);
		if (len == -1)
		{
			free(line);
			line = NULL;
			free(addline);
			return (NULL);
		}
		else if (len != 0)
			line = get_strjoin(line, addline);
	}
	free(addline);
	return (line);
}

char	*get_current(char *line)
{
	int		i;
	char	*currline;

	i = 0;
	if (!line)
		return (NULL);
	while (line[i] && line[i] != '\n')
		i++;
	currline = get_calloc(i + 2, sizeof(char));
	if (!currline)
		return (NULL);
	i = 0;
	while (line[i] && line[i] != '\n')
	{
		currline[i] = line[i];
		i++;
	}
	if (line[i] == '\n')
		currline[i] = '\n';
	return (currline);
}

char	*setup_next_call(char *line)
{
	int		i;
	int		j;
	char	*nextline;

	i = 0;
	j = 0;
	while (line[i] && line[i] != '\n')
		i++;
	if (!line[i] || (line[i] == '\n' && line[i + 1] == '\0'))
	{
		free(line);
		return (NULL);
	}
	nextline = get_calloc(get_strlen(line) - i + 1, sizeof(char));
	if (!nextline)
		return (NULL);
	if (line[i] == '\n')
		i++;
	while (line[i])
		nextline[j++] = line[i++];
	free(line);
	return (nextline);
}

char	*get_next_line(int fd)
{
	static char	*lines[4200];
	char		*current;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (0);
	lines[fd] = get_init_line(fd, lines[fd]);
	if (!lines[fd])
	{
		free(lines[fd]);
		lines[fd] = NULL;
		return (NULL);
	}
	current = get_current(lines[fd]);
	lines[fd] = setup_next_call(lines[fd]);
	return (current);
}

//#include <fcntl.h>
//#include <stdio.h>
//
//int	main(void)
//{
//	char	*printline;
//	int		agatha;
//	int		billy;
//	int		scene;
//	int		i;
//
//	printf("[open scene]\n");
//	agatha = open("scripts/Agatha.txt", O_RDONLY);
//	billy = open("scripts/Billy.txt", O_RDONLY);
//	scene = open("scripts/Scene.txt", O_RDONLY);
//	i = 0;
//	while (i < 11)
//	{
//		printline = get_next_bonus(billy);
//		printf("Billy: %s", printline);
//		free(printline);
//		printline = get_next_bonus(agatha);
//		printf("Agatha: %s", printline);
//		free(printline);
//		if (i == 8)
//		{
//			printline = get_next_bonus(scene);
//			printf(" - - - %s", printline);
//			free(printline);
//			printline = get_next_bonus(scene);
//			printf(" - - - %s", printline);
//			free(printline);
//		}
//		if (i == 10)
//		{
//			printline = get_next_bonus(scene);
//			printf(" - - - %s", printline);
//			free(printline);
//		}
//		i++;
//	}
//	close(agatha);
//	close(billy);
//	close(scene);
//	printf("[end scene]");
//	return (0);
//}
