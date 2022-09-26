#include "lists.h"
#include <stdlib.h>


/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: Pointer to the start of the list
 *
 * Return: 1 if it is a palindrome and 0 if it isn't and -1 on error
 */
int is_palindrome(listint_t **head)
{
	listint_t *start, *end;
	listint_t *tmp;

	if (head == NULL)
		return (-1);
	if (*head == NULL)
		return (1);

	start = *head;
	for (end = start; end->next != NULL; end = end->next)
		continue;

	while (start != end && end->next != start)
	{
		if (start->n != end->n)
			return (0);
		tmp = end;
		for (end = start; end->next != tmp; end = end->next)
			continue;
		start = start->next;
	}

	return (1);
}
