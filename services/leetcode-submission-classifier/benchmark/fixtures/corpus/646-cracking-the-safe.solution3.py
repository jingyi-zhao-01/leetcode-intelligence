# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cracking-the-safe
# source_path: LeetCode-Solutions-master/Python/cracking-the-safe.py
# solution_class: Solution3
# submission_id: ee8d5fd030622e295401a5313d02d81a5ab5629c
# seed: 417683947

# Time:  O(k^n)
# Space: O(k^n)

class Solution3(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        M = k**(n-1)
        def dfs(k, unique_rolling_hash, lookup, result):
            for i in reversed(xrange(k)):  # preorder like traversal relative to initial result to avoid getting stuck, i.e. don't use 0 until there is no other choice
                new_unique_rolling_hash = unique_rolling_hash*k + i
                if new_unique_rolling_hash not in lookup:
                    lookup.add(new_unique_rolling_hash)
                    result.append(str(i))
                    dfs(k, new_unique_rolling_hash%M, lookup, result)
                    break

        unique_rolling_hash = 0
        result = [str(0)]*(n-1)
        lookup = set()
        dfs(k, unique_rolling_hash, lookup, result)
        return "".join(result)