#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * struct list_span_s - Portion of a linked list
 * @start: beginning of the span
 * @end: end of the span
 */
typedef struct list_span_s
{
	listint_t *start;
	listint_t *end;
} list_span_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

int check_palindrome(list_span_t *span, listint_t *middle, int even);

#endif /* LISTS_H */
