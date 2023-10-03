#include "lists.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node- insert a node into a sorted linked list
 * @head: the head of the linked list
 * @number: is the number inserted
 * Return: the linked list address, after insertion
 */
listint_t *insert_node(listint_t **head, int number)
{
	struct listint_s *node = malloc(sizeof(listint_t));
	struct listint_s *tracker = *head;
	struct listint_s *step_back = NULL;

	if ((*head)->n > number)
	{
		node->next = (*head);
		return (node);
	}
	node->n = number;
	node->next = NULL;
	/*if head is null , return null*/
	if ((*head) == NULL)
		return (node);
	/*finding the spot where number < tracker->n*/
	while (tracker->n < number && tracker != NULL)
	{
		step_back = tracker;
		tracker = tracker->next;
	}
	/*if tracker null , then there is no bigger element,add last*/
	if (tracker == NULL)
	{
		add_nodeint_end(head, number);
	}
	/*if tacker != null, then a bigger element must have been found*/
	/*insert it*/
	else
	{
		node->next = tracker;
		step_back->next = node;
	}
	return (*head);

}
