# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: median-of-a-binary-search-tree-level
# source_path: LeetCode-Solutions-master/Python/median-of-a-binary-search-tree-level.py
# solution_class: Solution
# submission_id: 872b79cc2186f8bfe5b7631a3ff4a284ba597640
# seed: 2928893477

# Time:  O(n)
# Space: O(n)

# bfs

class Solution(object):
    def levelMedian(self, root, level):
        """
        :type root: Optional[TreeNode]
        :type level: int
        :rtype: int
        """
        def bfs(root, level):
            q = [root]
            d = 0
            while q:
                if d == level:
                    return q
                new_q = []
                for u in q:
                    if u.left:
                        new_q.append(u.left)
                    if u.right:
                        new_q.append(u.right)
                q = new_q
                d += 1
            return []
    
        arr = bfs(root, level)
        return arr[len(arr)//2].val if arr else -1