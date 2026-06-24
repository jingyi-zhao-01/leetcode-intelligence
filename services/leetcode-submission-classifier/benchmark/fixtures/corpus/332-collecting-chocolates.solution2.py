# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: collecting-chocolates
# source_path: LeetCode-Solutions-master/Python/collecting-chocolates.py
# solution_class: Solution2
# submission_id: 7ad5252d48c7070d56987a0f021e3b3081dff962
# seed: 593570012

# Time:  O(n)
# Space: O(n)

# mono stack, difference array, prefix sum

class Solution2(object):
    def minCost(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        def cost(k):
            w = k+1
            result = x*k
            dq = collections.deque()
            for i in xrange(len(nums)+w-1):
                if dq and i-dq[0] == w:
                    dq.popleft()
                while dq and nums[dq[-1]%len(nums)] >= nums[i%len(nums)]:
                    dq.pop()
                dq.append(i)
                if i >= w-1:
                    result += nums[dq[0]%len(nums)]
            return result

        def check(x):
            return cost(x) <= cost(x+1)

        left, right = 0, len(nums)
        while left <= right:
            mid = left + (right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return cost(left)