#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
 * copy_listint - creates a copy of a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the new list
 */

listint_t *copy_listint(listint_t *head)
{
listint_t *new_list = NULL;
listint_t *current = head;
listint_t *tail = NULL;

while (current)
{
listint_t *new_node = malloc(sizeof(listint_t));
if (!new_node)
{
free_listint(new_list);
return (NULL);
}

new_node->n = current->n;
new_node->next = NULL;

if (!new_list)
{
new_list = new_node;
tail = new_list;
}
else
{
tail->next = new_node;
tail = tail->next;
}

current = current->next;
}

return (new_list);
}

/**
 * reverse_listint - Reverses a linked list.
 * @head: A double pointer to the head of the linked list.
 *
 * Return: A pointer to the new head of the reversed list.
 */

listint_t *reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
return (*head);
}

/**
 * compare_lists - Compares two linked lists for equality.
 * @list1: The first linked list.
 * @list2: The second linked list.
 *
 * Return: 1 if the lists are equal, 0 otherwise.
 */

int compare_lists(listint_t *list1, listint_t *list2)
{
while (list1 != NULL && list2 != NULL)
{
if (list1->n != list2->n)
return (0);

list1 = list1->next;
list2 = list2->next;
}

if (list1 == NULL && list2 == NULL)
return (1);
else
return (0);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is a palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
listint_t *list_copy = copy_listint(*head);
reverse_listint(&list_copy);

int is_palindrome = compare_lists(*head, list_copy);

free_listint(list_copy);

return (is_palindrome);
}
