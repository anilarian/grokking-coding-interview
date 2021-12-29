"""Start of LinkedList Cycle (medium)


Problem Statement

Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

"""

from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head: Node):
    cycle_length = 0
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle_length = find_cycle_length(slow)
            break
    if cycle_length:
        return find_start(head, cycle_length)
    else:
        return False


def find_cycle_length(slow):
    current = slow
    len = 0
    while current:
        current = current.next
        len += 1
        if current == slow:
            return len


def find_start(head, len):
    ptr1 = head
    ptr2 = head
    length = len
    while length > 0:
        ptr2 = ptr2.next
        length -= 1
    while ptr1 != ptr2:
        ptr2 = ptr2.next
        ptr1 = ptr1.next
    return ptr1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    x = find_cycle_start(head)
    print("LinkedList cycle start: " + str(x.value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
