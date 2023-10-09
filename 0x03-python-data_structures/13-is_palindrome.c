#include "lists.h"

/**
 * is_palindrome - checks if a single linked list
 * is a pallindrome
 * @head: the list
 * Return: 1 for True and empty, 0 for False
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i = 1;

	if (head == NULL || *head == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		i++;
	}
	return (0);
}
