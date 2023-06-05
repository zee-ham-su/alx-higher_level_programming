#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
listint_t *current = list;
listint_t *runner = list;

if (list == NULL || list->next == NULL)
return (0);

while (current != NULL && runner != NULL && runner->next
!= NULL)
{
if (current == runner)
return (1);
current = current->next;
runner = runner->next->next;


}

return (0);
}
