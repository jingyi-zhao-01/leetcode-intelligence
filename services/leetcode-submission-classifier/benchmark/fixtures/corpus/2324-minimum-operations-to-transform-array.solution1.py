# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-transform-array
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-transform-array.py
# solution_class: Solution
# submission_id: 1ce1f13ad87b5e8e1bf3bf54ceb6ceccd1a65875
# seed: 448238613

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        result = 0
        cnt = float("inf")
        for i in xrange(len(nums1)):
            result += abs(nums1[i]-nums2[i])
            if (nums2[-1]-nums1[i])*(nums2[-1]-nums2[i]) <= 0:
                cnt = 0
            cnt = min(cnt, abs(nums2[-1]-nums1[i]), abs(nums2[-1]-nums2[i]))
        result += 1+cnt
        return result