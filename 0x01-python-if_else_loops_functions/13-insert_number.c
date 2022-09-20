#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Insert a node into a sorted linked list
 * @head: Pointer to the start of the list
 * @number: The value to insert
 *
 * Return: The address of the new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *prev;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	prev = *head;
	if (prev == NULL || prev->n >= number)
	{
		new->next = prev;
		*head = new;
		return (new);
	}

	curr = prev->next;
	while (curr != NULL && curr->n <= new->n)
	{
		curr = curr->next;
		prev = prev->next;
	}
	new->next = curr;
	prev->next = new;
	return (NULL);
}
