#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - checks whether list has a cycle or not
 * @list: the list
 * Return: 0 for no cycle and 1 for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *i = list, *k = list;

	if (!list)
		return (0);


	while (i && k && i->next)
	{

		k = k->next;
		i = i->next->next;		
		if (k == i)
		{
			return (1);
		}
	}
	return (0);
}
