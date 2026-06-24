# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cracking-the-safe
# source_path: LeetCode-Solutions-master/Python/cracking-the-safe.py
# solution_class: Solution2
# submission_id: 76266086774ce7b1c7099e7185005196f98f8e41
# seed: 4187094348

# Time:  O(k^n)
# Space: O(k^n)

class Solution2(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        total = k**n
        M = total//k
        unique_rolling_hash = 0
        result = [str(0)]*(n-1)
        lookup = set()
        while len(lookup) < total:
            for i in reversed(xrange(k)):  # preorder like traversal relative to initial result to avoid getting stuck, i.e. don't use 0 until there is no other choice
                new_unique_rolling_hash = unique_rolling_hash*k + i
                if new_unique_rolling_hash not in lookup:
                    lookup.add(new_unique_rolling_hash)
                    result.append(str(i))
                    unique_rolling_hash = new_unique_rolling_hash%M
                    break
        return "".join(result)