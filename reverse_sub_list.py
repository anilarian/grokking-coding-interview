"""Reverse a Sub-list (medium)


Problem Statement

Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.


Solution

The problem follows the In-place Reversal of a LinkedList pattern. We can use a similar approach as discussed in Reverse a LinkedList. Here are the steps we need to follow:

Skip the first p-1 nodes, to reach the node at position p.
Remember the node at position p-1 to be used later to connect with the reversed sub-list.
Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
Connect the p-1 and q+1 nodes to the reversed sub-list.
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


def reverse_sub_list(head: Node, p: int, q: int) -> Node:
    if p == q:
        return head
    # Track nodes till we reach the sub list
    current, prev = head, None
    i = 0
    while current and i < p - 1:
        prev = current
        current = current.next
        i += 1
    # store the lat node of the first part and first node the sublist as last node.
    first_list_last_node = prev
    sub_list_last_node = current

    # Reverse the sublist
    next = None
    i = 0
    while current and i < q - p + 1:
        next = current.next
        current.next = prev
        prev = current
        current = next
        i += 1
    # link last node of reversed sublist to last node of first list
    if first_list_last_node:
        first_list_last_node.next = prev
    else:
        head = prev
    # link next node of last node of sublist to current node of reversed list
    sub_list_last_node.next = current
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 1, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
