# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 3sum
# source_path: LeetCode-Solutions-master/Python/3sum.py
# solution_class: Solution2
# submission_id: d2915439ab781dfde3c59c278a2ca23622255231
# seed: 2988709998

# Time:  O(n^2)
# Space: O(1)

class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return result