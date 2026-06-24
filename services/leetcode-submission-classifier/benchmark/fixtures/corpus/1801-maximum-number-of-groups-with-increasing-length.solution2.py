# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-groups-with-increasing-length
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-groups-with-increasing-length.py
# solution_class: Solution2
# submission_id: 90b1a0221c5a28c16c2e2e318c222644ddb01732
# seed: 3966630944

# Time:  O(n)
# Space: O(n)

# constructive algorithms, counting sort, greedy

class Solution2(object):
    def maxIncreasingGroups(self, usageLimits):
        """
        :type usageLimits: List[int]
        :rtype: int
        """
        usageLimits.sort()
        result = curr = 0
        for x in usageLimits:
            curr += x
            if curr >= result+1:
                curr -= result+1
                result += 1
        return result