"""Level Averages in a Binary Tree (easy)


Problem Statement

Given a binary tree, populate an array to represent the averages of all of its levels.

Example 1:


Example 2:

Solution

This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS
approach. The only difference will be that instead of keeping track of all nodes of a level,
we will only track the running sum of the values of all nodes in each level. In the end,
we will append the average of the current level to the result array.

"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root: TreeNode):
    result = []
    if not root:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            current_node = queue.popleft()
            level_sum += current_node.val

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(level_sum/ level_size)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level sums: " + str(traverse(root)))


main()
