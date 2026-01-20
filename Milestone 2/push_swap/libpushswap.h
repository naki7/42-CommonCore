/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libpushswap.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joshde-s <joshde-s@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 11:31:32 by joshde-s          #+#    #+#             */
/*   Updated: 2025/12/15 15:23:39 by joshde-s         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBPUSHSWAP_H
# define LIBPUSHSWAP_H
# include "libft.h"

typedef struct	s_stack
{
	int				value;
	struct s_stack	*next;
}	t_stack;

void	push_swap(t_stack **a);
void	handle_error(void);

void	handle_stack(int *stacka, int *alen, int *stackb, int *blen);
void	large_sort(int *norm, int *alen, int *stackb, int *blen);
void	greedy(int *norm, int *alen, int *stackb, int *blen);

void	swap_a(int *stack, int stklen);
void	swap_b(int *stack, int stklen);
void	swap_both(int *stacka, int alen, int *stackb, int blen);

void	pushtoa(int *into, int *inlen, int *outof, int *outlen);
void	pushtob(int *into, int *inlen, int *outof, int *outlen);

void	rotate_a(int *stack, int len);
void	rotate_b(int *stack, int len);
void	rotate_both(int *stacka, int alen, int *stackb, int blen);

void	rev_rotate_a(int *stack, int len);
void	rev_rotate_b(int *stack, int len);
void	rev_rotate_both(int *stacka, int alen, int *stackb, int blen);

int	ft_stacksize(t_stack *stack);
t_stack	*ft_stacknew(int value);
void	ft_stackadd_back(t_stack **stack, t_stack *add);
void	produce_arrays(t_stack **a, int **stacka, int **stackb, int stklen);

#endif
