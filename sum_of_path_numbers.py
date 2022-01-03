"""Sum of Path Numbers (medium)


Problem Statement

Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will
represent a number. Find the total sum of all the numbers represented by all paths.



Solution

This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach. The
additional thing we need to do is to keep track of the number representing the current path.

How do we calculate the path number for a node? Taking the first example mentioned above, say we are
at node ‘7’. As we know, the path number for this node is ‘17’, which was calculated by: 1 * 10 + 7 =>
17. We will follow the same approach to calculate the path number of each node.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_numbers_sum(root: TreeNode):
    return find_path_numbers_sum(root, 0)


def find_path_numbers_sum(current_node: TreeNode, path_sum: int):
    if current_node is None:
        return 0

    path_sum = 10 * path_sum + current_node.val

    if current_node.left is None and current_node.right is None:
        return path_sum

    return find_path_numbers_sum(current_node.left, path_sum) + find_path_numbers_sum(current_node.right,
                                                                                      path_sum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(path_numbers_sum(root)))


main()
