"""All Paths for a Sum (medium)


Problem Statement

Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the
node values of each path equals ‘S’.


Image label

Solution

This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach. There will
be two differences:

Every time we find a root-to-leaf path, we will store it in a list.
We will traverse all paths and will not stop processing after finding the first path.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_all_paths(root: TreeNode, path_sum: int) -> list:
    all_paths = []
    find_paths_recursively(root, path_sum, [], all_paths)
    return all_paths


def find_paths_recursively(current_node: TreeNode, required_sum: int, current_path: list,
                           all_paths: list):
    if current_node is None:
        return

    current_path.append(current_node.val)

    if current_node.val == required_sum and current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:
        find_paths_recursively(current_node.left,
                               required_sum - current_node.val,
                               current_path,
                               all_paths)
        find_paths_recursively(current_node.right,
                               required_sum - current_node.val,
                               current_path,
                               all_paths)

    del current_path[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print("Tree paths with required_sum " + str(required_sum) +
          ": " + str(find_all_paths(root, required_sum)))


main()
