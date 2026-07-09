"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Dictionary to map: {Old_Node: New_Clone_Node}
        old_to_new = {}

        def dfs(curr_node):
            # If we already cloned this node, return the existing clone
            if curr_node in old_to_new:
                return old_to_new[curr_node]

            # 1. Create the clone (copy the value)
            copy = Node(curr_node.val)
            old_to_new[curr_node] = copy

            # 2. Recursively clone all neighbors
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        return dfs(node)


                