# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: special-array-with-x-elements-greater-than-or-equal-x
# source_path: LeetCode-Solutions-master/Python/special-array-with-x-elements-greater-than-or-equal-x.py
# solution_class: Solution3
# submission_id: 111040bbb35ea76e96b1066560f2f71977837fc3
# seed: 997643098

# Time:  O(n)
# Space: O(1)

# counting sort solution

class Solution3(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX_NUM = 1000
        def counting_sort(nums, reverse=False):  # Time: O(n), Space: O(n)
            count = [0]*(MAX_NUM+1)
            for num in nums:
                count[num] += 1
            for i in xrange(1, len(count)):
                count[i] += count[i-1]
            result = [0]*len(nums)
            if not reverse:
                for num in reversed(nums):  # stable sort
                    count[num] -= 1
                    result[count[num]] = num
            else:
                for num in nums:  # stable sort
                    count[num] -= 1
                    result[count[num]] = num
                result.reverse()
            return result
    
        nums = counting_sort(nums, reverse=True)  # extra O(n) space for stable sort
        left, right = 0, len(nums)-1
        while left <= right:  # Time: O(logn)
            mid = left + (right-left)//2
            if nums[mid] <= mid:
                right = mid-1
            else:
                left = mid+1
        return -1 if left < len(nums) and nums[left] == left else left