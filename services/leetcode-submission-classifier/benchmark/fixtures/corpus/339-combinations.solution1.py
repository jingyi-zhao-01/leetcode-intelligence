# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: combinations
# source_path: LeetCode-Solutions-master/Python/combinations.py
# solution_class: Solution
# submission_id: 6529794a5d81563aec89718baafa3ebaf05c3c8f
# seed: 102365188

# Time:  O(k * C(n, k))
# Space: O(k)

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        nums, idxs = range(1, n+1), range(k)
        result = [[nums[i] for i in idxs]]
        while True:
            for i in reversed(xrange(k)):
                if idxs[i] != i+n-k:
                    break
            else:
                break
            idxs[i] += 1
            for j in xrange(i+1, k):
                idxs[j] = idxs[j-1]+1
            result.append([nums[i] for i in idxs])
        return result