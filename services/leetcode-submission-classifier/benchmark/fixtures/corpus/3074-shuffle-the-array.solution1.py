# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shuffle-the-array
# source_path: LeetCode-Solutions-master/Python/shuffle-the-array.py
# solution_class: Solution
# submission_id: 1b572d851e4dae339d635a59e7e9f4f25a306842
# seed: 4101858863

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        def index(i):
            return 2*i if i < n else 2*(i-n)+1
    
        for i in xrange(len(nums)):
            j = i
            while nums[i] >= 0:
                j = index(j)
                nums[i], nums[j] = nums[j], ~nums[i]  # processed
        for i in xrange(len(nums)):
            nums[i] = ~nums[i]
        return nums