# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-paint-sheets
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-paint-sheets.py
# solution_class: Solution
# submission_id: d7a172e38e0d75283aa5ae863bb5236f5804be53
# seed: 4122472192

# Time:  O(mlogm)
# Space: O(m)

# sort, prefix sum, two pointers

class Solution(object):
    def numberOfWays(self, n, limit):
        """
        :type n: int
        :type limit: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        limit.sort()
        suffix = [0]*(len(limit)+1)
        for i in reversed(xrange(len(suffix)-1)):
            limit[i] = min(limit[i], n-1)
            suffix[i] = suffix[i+1]+limit[i]
        result = j = 0
        for i in reversed(xrange(len(limit))):
            while j < len(limit):
                if limit[i]+limit[j] >= n:
                    break
                j += 1
            cnt = (limit[i]-n+1)*(len(limit)-j)+suffix[j]
            if i >= j:
                cnt -= limit[i]+limit[i]-n+1
            result = (result+cnt)%MOD
        return result