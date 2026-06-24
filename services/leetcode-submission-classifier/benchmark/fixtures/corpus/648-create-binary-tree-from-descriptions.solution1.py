# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: create-binary-tree-from-descriptions
# source_path: LeetCode-Solutions-master/Python/create-binary-tree-from-descriptions.py
# solution_class: Solution
# submission_id: 96b94171d461cdb8cc599f9013e2deb875f8feec
# seed: 888112324

# Time:  O(n)
# Space: O(n)

# tree

class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        nodes = {}
        children = set()
        for p, c, l in descriptions:
            parent = nodes.setdefault(p, TreeNode(p))
            child = nodes.setdefault(c, TreeNode(c))
            if l:
                parent.left = child
            else:
                parent.right = child
            children.add(c)
        return nodes[next(p for p in nodes.iterkeys() if p not in children)]