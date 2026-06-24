# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subsets-ii
# source_path: LeetCode-Solutions-master/Python/subsets-ii.py
# solution_class: Solution3
# submission_id: 62d2af4504367903517c5d780be46ae8b24bca1c
# seed: 3558204381

# Time:  O(n * 2^n)
# Space: O(1)

class Solution3(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.subsetsWithDupRecu(result, [], sorted(nums))
        return result

    def subsetsWithDupRecu(self, result, cur, nums):
        if not nums:
            if cur not in result:
                result.append(cur)
        else:
            self.subsetsWithDupRecu(result, cur, nums[1:])
            self.subsetsWithDupRecu(result, cur + [nums[0]], nums[1:])