# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-all-lonely-numbers-in-the-array
# source_path: LeetCode-Solutions-master/Python/find-all-lonely-numbers-in-the-array.py
# solution_class: Solution
# submission_id: 71271d1eed5226f951351ee924f1587ee9e108f3
# seed: 2379451399

# Time:  O(n)
# Space: O(n)

# freq table

class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = collections.Counter(nums)
        return [x for x in nums if cnt[x] == 1 and x-1 not in cnt and x+1 not in cnt]