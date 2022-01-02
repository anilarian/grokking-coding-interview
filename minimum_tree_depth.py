"""Minimum Depth of a Binary Tree (easy)


Problem Statement

Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest
path from the root node to the nearest leaf node.

Example 1:


Example 2:

Solution

This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS
approach. The only difference will be, instead of keeping track of all the nodes in a level,
we will only track the depth of the tree. As soon as we find our first leaf node, that level will
represent the minimum depth of the tree.

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
    minimum_tree_depth = 0

    while queue:
        minimum_tree_depth += 1
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()
            if current_node.left is None and current_node.right is None:
                return minimum_tree_depth

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("minimum depth: " + str(traverse(root)))


main()
