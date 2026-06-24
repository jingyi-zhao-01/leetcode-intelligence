# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: majority-element
# source_path: LeetCode-Solutions-master/Python/majority-element.py
# solution_class: Solution3
# submission_id: 1e34c06bdc7a82bc44d26ba042ae4336e414229d
# seed: 1267920173

# Time:  O(n)
# Space: O(1)

import collections

class Solution3(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(collections.Counter(nums).items(), key=lambda a: a[1], reverse=True)[0][0]