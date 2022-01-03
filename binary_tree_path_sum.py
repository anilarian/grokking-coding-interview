"""Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the
sum of all the node values of that path equals ‘S’.



Solution

As we are trying to search for a root-to-leaf path, we can use the Depth First Search (DFS) technique
to solve this problem.

To recursively traverse a binary tree in a DFS fashion, we can start from the root and at every step,
make two recursive calls one for the left and one for the right child.

Here are the steps for our Binary Tree Path Sum problem:

Start DFS with the root of the tree. If the current node is not a leaf node, do two things: Subtract
the value of the current node from the given number to get a new sum => S = S - node.value Make two
recursive calls for both the children of the current node with the new number calculated in the
previous step. At every step, see if the current node being visited is a leaf node and if its value is
equal to the given number ‘S’. If both these conditions are true, we have found the required
root-to-leaf path, therefore return true. If the current node is a leaf but its value is not equal to
the given number ‘S’, return false. Let’s take the example-2 mentioned above to visually see our
algorithm:

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: TreeNode, path_sum: int) -> bool:
    if root is None:
        return False

    if root.val == path_sum and root.left is None and root.right is None:
        return True

    # subtract path sum with node value at each level and call the function recursively until we reach
    # a leaf node
    return has_path_sum(root.left, path_sum - root.val) or has_path_sum(root.right, path_sum - root.val)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path_sum(root, 23)))
    print("Tree has path: " + str(has_path_sum(root, 16)))


main()
