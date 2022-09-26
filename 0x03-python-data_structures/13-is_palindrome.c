#include "lists.h"
#include <stdlib.h>
#include <stdio.h>


/**
 * stack_push - Put an item on the stack
 * @stack: The stack to push onto
 * @element: The element to push onto the stack
 *
 * Return: 1 if successful and 0 otherwise
 */
int stack_push(listint_t **stack, int element)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (0);
	}
	new->n = element;
	new->next = *stack;
	*stack = new;
	return (1);
}


/**
 * stack_pop - Pop an item off the stack
 * @stack: The stack to pop off of
 *
 * Return: The value of the popped item
 */
int stack_pop(listint_t **stack)
{
	listint_t *popped;
	int value;

	popped = *stack;
	*stack = popped->next;
	value = popped->n;
	free(popped);
	return (value);
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
	listint_t *stack = NULL;

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
		if (!stack_push(&stack, slow->n))
		{
			free_listint(stack);
			return (-1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}

	/*
	 * For an odd number of elements move slow
	 * forward since there is a center element
	 */
	slow = (fast != NULL) ? slow->next : slow;

	/* Compare remaining elements to stack */
	while (slow != NULL)
	{
		if (slow->n != stack_pop(&stack))
		{
			free_listint(stack);
			return (0);
		}
		slow = slow->next;
	}
	return (1);
}
