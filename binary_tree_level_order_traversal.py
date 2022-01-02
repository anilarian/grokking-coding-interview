"""Binary Tree Level Order Traversal (easy)


Problem Statement

Given a binary tree, populate an array to represent its level-by-level traversal. You should populate
the values of all nodes of each level from left to right in separate sub-arrays.

Example 1:


Example 2:

Solution

Since we need to traverse all nodes of each level before moving onto the next level, we can use the
Breadth First Search (BFS) technique to solve this problem.

We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:

Start by pushing the root node to the queue. Keep iterating until the queue is empty. In each
iteration, first count the elements in the queue (let’s call it levelSize). We will have these many
nodes in the current level. Next, remove levelSize nodes from the queue and push their value in an
array to represent the current level. After removing each node from the queue, insert both of its
children into the queue. If the queue is not empty, repeat from step 3 for the next level. """

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
        level_nodes = []

        for _ in range(level_size):
            current_node = queue.popleft()
            level_nodes.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(level_nodes)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
