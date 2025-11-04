/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libftprintf.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 10:39:19 by joshde-s          #+#    #+#             */
/*   Updated: 2025/11/04 10:59:09 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FTPRINTF_H
# define FTPRINTF_H
# include "libft.h"
# include <stdarg.h>

int	ft_printf(const char *format, ...);

int	handleset(char specifier, va_list args);
int	handlehex(char spec, unsigned long num);
int	handlestr(char specifier, char *str);

int	ft_printf_bonus(char *substr, int *index, va_list args);

#endif
