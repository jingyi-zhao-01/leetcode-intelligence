# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 3sum-smaller
# source_path: LeetCode-Solutions-master/Python/3sum-smaller.py
# solution_class: Solution
# submission_id: 2522f08272f25c5f201b15c34fd435975a594462
# seed: 3611447911

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n = len(nums)

        count, k = 0, 2
        while k < n:
            i, j = 0, k - 1
            while i < j:  # Two Pointers, linear time.
                if nums[i] + nums[j] + nums[k] >= target:
                    j -= 1
                else:
                    count += j - i
                    i += 1
            k += 1

        return count