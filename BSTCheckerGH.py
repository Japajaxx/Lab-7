# Returns None if root_node is the root of a valid BST.
# If a BST violation occurs, the node causing the violation is returned. Such a 
# node may be one of three things:
# 1. A node in the left subtree of an ancestor with a lesser key
# 2. A node in the right subtree of an ancestor with a greater key
# 3. A node with the left or right attribute referencing an ancestor
def check_bst_validity(root_node):
    if not root_node:
        return None

    node_stack = [root_node]
    distinct_node_set = set()

    # Check for loops
    while node_stack:
        node = node_stack.pop()
        if node:
            if node in distinct_node_set:
                return node
            distinct_node_set.add(node)
            if node.left in distinct_node_set or node.right in distinct_node_set:
                return node
            node_stack.append(node.left)
            node_stack.append(node.right)

    # Check for key violations
    node_stack = [root_node]
    while node_stack:
        node = node_stack.pop()
        if node:
            # Check left subtree
            if node.left and node.left.key > node.key:
                return node.left
            # Check right subtree
            if node.right and node.right.key < node.key:
                return node.right
            node_stack.append(node.left)
            node_stack.append(node.right)
    
    return None
