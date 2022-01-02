"""Level Order Successor (easy)


Problem Statement

Given a binary tree and a node, find the level order successor of the given node in the tree. The
level order successor is the node that appears right after the given node in the level order traversal.

Example 1:


Example 2:

Example 3:

Solution

This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS
approach. The only difference will be that we will not keep track of all the levels. Instead we will
keep inserting child nodes to the queue. As soon as we find the given node, we will return the next
node from the queue as the level order successor.

"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse_successor(root: TreeNode, key: int):
    result = []
    if not root:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        current_node = queue.popleft()

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        if current_node.val == key:
            break
    return queue[0].val if queue else None


def main():
    root = TreeNode(12)
    key = 7
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order successor of {}: ".format(key) + str(traverse_successor(root, key)))


main()
