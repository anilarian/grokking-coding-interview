class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root: TreeNode, path_sum: int) -> int:
    if not root:
        return  path_sum == 0

    return find_paths_recursive(root, path_sum, 0)

def find_paths_recursive(current_node: TreeNode, current_sum: int, paths: int):
    if current_node is None:
        return 0

    if