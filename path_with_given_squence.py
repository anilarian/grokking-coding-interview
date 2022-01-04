"""Path With Given Sequence (medium)


Problem Statement

Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in
the given tree.



Solution

This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach and
additionally, track the element of the given sequence that we should match with the current node.
Also, we can return false as soon as we find a mismatch between the sequence and the node value.

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root: TreeNode, sequence: [int]) -> bool:
    if not root:
        return len(sequence) == 0

    return find_path_recursive(root, sequence, 0)


def find_path_recursive(current_node: TreeNode, sequence: [int], seq_index: int):
    if current_node is None:
        return False

    seq_len = len(sequence)
    if seq_index >= seq_len or current_node.val != sequence[seq_index]:
        return False

    if current_node.left is None and current_node.right is None and seq_index == seq_len - 1:
        return True

    return (find_path_recursive(current_node.left, sequence, seq_index + 1) or
            find_path_recursive(current_node.right, sequence, seq_index + 1))


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(10)
    root.right.right.left = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6, 12])))


main()
