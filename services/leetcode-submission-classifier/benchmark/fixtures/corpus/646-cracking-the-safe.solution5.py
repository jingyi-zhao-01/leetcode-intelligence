# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cracking-the-safe
# source_path: LeetCode-Solutions-master/Python/cracking-the-safe.py
# solution_class: Solution5
# submission_id: a46bebf6174020469b751737f8e598c1ee62b348
# seed: 3822845832

# Time:  O(k^n)
# Space: O(k^n)

class Solution5(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def dfs(k, node, lookup, result):
            for i in xrange(k):  # preorder like traversal relative to initial result to avoid getting stuck, i.e. don't use k-1 until there is no other choice
                neighbor = node + str(i)
                if neighbor not in lookup:
                    lookup.add(neighbor)
                    result.append(str(i))
                    dfs(k, neighbor[1:], lookup, result)
                    break

        result = [str(k-1)]*(n-1)
        lookup = set()
        dfs(k, "".join(result), lookup, result)
        return "".join(result)