#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list of integers is a palindrome.
 * @head: A double pointer to the head of the linked list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}

	listint_t *prev_ptr = NULL;
	listint_t *curr_ptr = slow_ptr->next;

	while (curr_ptr != NULL)
	{
		listint_t *next_ptr = curr_ptr->next;

		curr_ptr->next = prev_ptr;
		prev_ptr = curr_ptr;
		curr_ptr = next_ptr;
	}

	listint_t *first_ptr = *head;

	while (prev_ptr != NULL)
	{
		if (first_ptr->n != prev_ptr->n)
			return (0);
		first_ptr = first_ptr->next;
		prev_ptr = prev_ptr->next;
	}

	return (1);
}
