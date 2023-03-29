"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict

class Solution(object):
    def cloneNode(self, node, nodeMap):
        if node is None:
            return None

        if node in nodeMap:
            return nodeMap[node]
        
        addNode = Node(node.val, [])
        nodeMap[node] = addNode
        for neighbor in node.neighbors:
            addNode.neighbors.append(self.cloneNode(neighbor, nodeMap))
        

        return addNode
            

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        return self.cloneNode(node, nodeMap={})
