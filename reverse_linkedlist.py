"""Reverse a LinkedList (easy)


Problem Statement

Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head
of the reversed LinkedList.


Solution

To reverse a LinkedList, we need to reverse one node at a time. We will start with a variable current
which will initially point to the head of the LinkedList and a variable previous which will point to
the previous node that we have processed; initially previous will point to null.

In a stepwise manner, we will reverse the current node by pointing it to the previous before moving on
to the next node. Also, we will update the previous to always point to the previous node that we have
processed. Here is the visual representation of our algorithm:

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse(head: Node) -> Node:
    prev, current, next = None, head, None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
