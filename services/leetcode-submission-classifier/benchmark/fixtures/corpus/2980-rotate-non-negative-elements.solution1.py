# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-non-negative-elements
# source_path: LeetCode-Solutions-master/Python/rotate-non-negative-elements.py
# solution_class: Solution
# submission_id: 17e22ea9c61f891fee8d1c833e9d7719c0e59023
# seed: 729122917

# Time:  O(n)
# Space: O(n)

# array

class Solution(object):
    def rotateElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def rotate(nums, k):
            k %= len(nums)
            c = gcd(len(nums), k)
            for i in xrange(c):
                for j in xrange(1, len(nums)//c):
                    nums[i], nums[(i-j*k)%len(nums)] = nums[(i-j*k)%len(nums)], nums[i]

        result = [x for x in nums if x >= 0]
        if not result:
            return nums
        rotate(result, k)
        j = 0
        for i in xrange(len(nums)):
            if nums[i] < 0:
                continue
            nums[i] = result[j]
            j += 1
        return nums