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

typedef struct s_stack
{
	int				value;
	struct s_stack	*next;
}	t_stack;

void	push_swap(t_stack **a);

void	handle_error(void);
void	free_stack_nodes(t_stack **a);
void	free_split_from(char **arr, int start);

void	handle_stack(int *stacka, int *alen, int *stackb, int *blen);
void	large_sort(int *norm, int *alen, int *stackb, int *blen);
void	greedy(int *norm, int *alen, int *stackb, int *blen);
int		get_lis(int *norm, int size, int *temp);

int		check_if_ordered(int *normstack, int alen);
void	dup_atonorm(int *norm, int *stacka, int alen);
void	free_stacks(int *stacka, int *stackb, int *normstack);
void	sort_three(int *norm);
void	small_sort(int *norm, int *alen, int *stackb, int *blen);

void	large_radix(int *norm, int *alen, int *stackb, int *blen);
void	get_best_vars(int *norm, int size, int *best_len, int *best_arr);
void	init_costs(int a_indx, int b_indx, int *sizes, int *costs);
int		init_best_index(int *norm, int *curr_small, int *curr_big, int alen);
void	rev_rotate_to_values(int *norm, int *stackb, int*sizes, int*costs);

int		reset_indexes(int *maxindx, int maxlen, int **dyn_arr);
void	free_larger_stack(t_stack **a);

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

int		ft_stacksize(t_stack *stack);
t_stack	*ft_stacknew(int value);
void	ft_stackadd_back(t_stack **stack, t_stack *add, char *string);
void	produce_arrays(t_stack **a, int **stacka, int **stackb, int stklen);
void	free_small_stack(t_stack **a, int size);

#endif
