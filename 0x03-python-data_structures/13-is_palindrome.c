#include "lists.h"
#include <stdlib.h>
#include <stdio.h>


/**
 * check_palindrome - Checks if a span is a palindrome
 * @span: Span to check. Shifts end forward before returning
 * @middle: Middle of the span
 * @even: Whether the list has an even number of elements
 *
 * Return: 1 if it is a palindrome and 0 otherwise
 */
int check_palindrome(list_span_t *span, listint_t *middle, int even)
{
	listint_t *curr;

	curr = span->start;
	if (curr->next == middle)
	{
		if (!even)
		{
			span->end = curr;
			return (1);
		}
		span->end = curr->next;
		if (span->end->n == curr->n)
			return (1);
		else
			return (0);
	}
	span->start = span->start->next;
	if (!check_palindrome(span, middle, even))
		return (0);
	span->end = span->end->next;
	if (span->end->n == curr->n)
		return (1);
	else
		return (0);
}


/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: Pointer to the start of the list
 *
 * Return: 1 if it is a palindrome and 0 if it isn't and -1 on error
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	int even;
	list_span_t span;

	if (head == NULL)
		return (-1);
	if (*head == NULL)
		return (1);
	/* Find the middle of the list */
	slow = *head;
	if (slow->next == NULL)
		return (1);
	fast = slow;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/*
	 * For an odd number of elements move slow
	 * forward since there is a center element
	 */
	slow = (fast != NULL) ? slow->next : slow;

	span.start = *head;
	even = (fast == NULL) ? 1 : 0;

	return (check_palindrome(&span, slow, even));
}
