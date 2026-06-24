# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: clone-graph
# source_path: LeetCode-Solutions-master/Python/clone-graph.py
# solution_class: Solution
# submission_id: 734d715eaf2de6ccc407c4a2aaa984850a2eaf2b
# seed: 2400305140

# Time:  O(n)
# Space: O(n)

class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        cloned_node = UndirectedGraphNode(node.label)
        cloned, queue = {node:cloned_node}, [node]

        while queue:
            current = queue.pop()
            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    queue.append(neighbor)
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    cloned[neighbor] = cloned_neighbor
                cloned[current].neighbors.append(cloned[neighbor])
        return cloned[node]