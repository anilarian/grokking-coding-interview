"""Reverse Level Order Traversal (easy)


Problem Statement

Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
i.e., the lowest level comes first. You should populate the values of all nodes in each level from
left to right in separate sub-arrays.

Example 1:


Example 2:

Solution

This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS
approach. The only difference will be that instead of appending the current level at the end,
we will append the current level at the beginning of the result list. """

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def reverse_traversal(root: TreeNode):
    result = deque()
    if not root:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            current_ndoe = queue.popleft()
            level_nodes.append(current_ndoe.val)
            if current_ndoe.left:
                queue.append(current_ndoe.left)
            if current_ndoe.right:
                queue.append(current_ndoe.right)
        result.appendleft(level_nodes)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(reverse_traversal(root)))


main()
