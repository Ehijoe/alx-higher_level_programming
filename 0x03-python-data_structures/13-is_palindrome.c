#include "lists.h"
#include <stdlib.h>
#include <stdio.h>


/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: Pointer to the start of the list
 *
 * Return: 1 if it is a palindrome and 0 if it isn't and -1 on error
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	int i, len, *stack;

	if (head == NULL)
		return (-1);
	if (*head == NULL)
		return (1);
	slow = *head;
	if (slow->next == NULL)
		return (1);
	fast = slow;
	len = 0;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		len++;
	}
	stack = malloc(sizeof(int) * len);
	if (stack == NULL)
		return (-1);
	fast = *head;
	for (i = 0; i < len; i++)
	{
		stack[i] = fast->n;
		fast = fast->next;
	}
	slow = (fast != NULL) ? slow->next : slow;
	while (slow != NULL)
	{
		if (slow->n != stack[--len])
		{
			free(stack);
			return (0);
		}
		slow = slow->next;
	}
	free(stack);
	return (1);
}
