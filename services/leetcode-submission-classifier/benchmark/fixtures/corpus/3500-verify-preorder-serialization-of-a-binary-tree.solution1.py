# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: verify-preorder-serialization-of-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/verify-preorder-serialization-of-a-binary-tree.py
# solution_class: Solution
# submission_id: 55d3bf9ef25cd76c71c1fdd9dfb7f1f334951789
# seed: 767425877

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        def split_iter(s, tok):
            start = 0
            for i in xrange(len(s)):
                if s[i] == tok:
                    yield s[start:i]
                    start = i + 1
            yield s[start:]

        if not preorder:
            return False

        depth, cnt = 0, preorder.count(',') + 1
        for tok in split_iter(preorder, ','):
            cnt -= 1
            if tok == "#":
                depth -= 1
                if depth < 0:
                    break
            else:
                depth += 1
        return cnt == 0 and depth < 0