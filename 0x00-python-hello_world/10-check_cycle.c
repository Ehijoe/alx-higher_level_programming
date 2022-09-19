#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - Checks if there is a cycle in a linked list
 * @list: Pointer to first node of the list
 *
 * Return: 1 if there's is a cycle and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list->next;
	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
