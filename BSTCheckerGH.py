# Returns None if root_node is the root of a valid BST.
# If a BST violation occurs, the node causing the violation is returned. Such a 
# node may be one of three things:
# 1. A node in the left subtree of an ancestor with a lesser key
# 2. A node in the right subtree of an ancestor with a greater key
# 3. A node with the left or right attribute referencing an ancestor
def check_bst_validity(root_node):
    # Make a node stack (Ex. nodeStack) populated with the root node
    
    # Check for loops first
    #create a set to hold distinct nodes (Ex. distinctNodeSet)
    
    # While the nodeStack is not empty

        # Pop a node from the stack

        # If the node is not None

            # Add the node to the set of distinct nodes visited

            #
            # If either of the node's children is in distinct_set then the node 
            # is invalid due to either:
            #   referencing an ancestor and thus causing a loop in the tree 
            #   or
            #   referencing a non-ancestor node from another part of the tree 
            #   and thus making a node have two parent nodes.
            # This lab's test cases only test the former and not the latter.

            # Append children to the list

    
    # Check for key violations second. First reset the stack to house the root node again

    # While the nodeStack is not empty

        # Pop a node from the stack

        # If the node is not None

            # Check for key-related violations on both children's subtrees
            # This is done by checking th eleft and right subtrees of the node
            # for key violations to ensure that all keys in the left subtree are 
            # **less** than or equal to the key of the current node, and the right 
            # subtree to ensure that all keys are **greater** than or equal to the 
            # key of the current node. If a violation is found, the bad_node is returned immediately.

            # If no violations are found in either subtree, the children of the current node 
            # (node.left and node.right) are appended to the nodeStack.
    
    # Arriving here implies that no violations were found, so return None

