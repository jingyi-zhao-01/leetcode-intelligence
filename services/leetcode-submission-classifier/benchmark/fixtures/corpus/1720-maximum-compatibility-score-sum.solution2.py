# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-compatibility-score-sum
# source_path: LeetCode-Solutions-master/Python/maximum-compatibility-score-sum.py
# solution_class: Solution2
# submission_id: 9256a560cb0a8481a258c2bc8d6e916ee6b884ef
# seed: 2278931133

# Time:  O(m^2 * (n + m))
# Space: O(m^2)

import itertools


# weighted bipartite matching solution

class Solution2(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        def popcount(n):  # Time: O(logn) ~= O(1) if n is a 32-bit number
            result = 0
            while n:
                n &= n-1
                result += 1
            return result

        def masks(vvi):
            result = []
            for vi in vvi:
                mask, bit = 0, 1
                for i in xrange(len(vi)):
                    if vi[i]:
                        mask |= bit
                    bit <<= 1
                result.append(mask)
            return result

        nums1, nums2 = masks(students), masks(mentors)
        dp = [(0, 0)]*(2**len(nums2))
        for mask in xrange(len(dp)):
            bit = 1
            for i in xrange(len(nums2)):
                if (mask&bit) == 0:
                    dp[mask|bit] = max(dp[mask|bit], (dp[mask][0]+(len(students[0])-popcount(nums1[dp[mask][1]]^nums2[i])), dp[mask][1]+1))
                bit <<= 1
        return dp[-1][0]