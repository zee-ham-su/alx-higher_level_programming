#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: pointer to the head of the linked list
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */


int check_cycle(listint_t *list)
{
listint_t *p1, *p2;

p1 = list;
p2 = list;

while (p1 && p2 && p2->next)
{
p1 = p1->next;
p2 = p2->next->next;

if (p1 == p2)
return (1);
}

return (0);
}
