# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-array-sum
# source_path: LeetCode-Solutions-master/Python/minimum-array-sum.py
# solution_class: Solution
# submission_id: 6b44b44487f2c004fbeae00510ec670ba4e4c1b6
# seed: 2155580113

# Time:  O(nlogn)
# Space: O(n)

# greedy, case works
# Reference: https://leetcode.com/problems/minimum-array-sum/solutions/6078002/o-n-log-n-greedy/

class Solution(object):
    def minArraySum(self, nums, k, op1, op2):
        """
        :type nums: List[int]
        :type k: int
        :type op1: int
        :type op2: int
        :rtype: int
        """
        nums.sort()

        left = next((i for i in xrange(len(nums)) if nums[i] >= k), len(nums))
        right = next((i for i in xrange(len(nums)) if nums[i] >= 2*k-1), len(nums))

        lookup, cnt = [False]*len(nums), 0
        for j in reversed(xrange(right, len(nums))):
            if not op1:
                break
            op1 -= 1
            nums[j] = (nums[j]+1)//2
            if op2:
                op2 -= 1
                nums[j] -= k
        else:
            j = right-1

        for i in xrange(left, j+1):
            if not op2:
                break
            op2 -= 1
            if k%2 == 1 and nums[i]%2 == 0:
                lookup[i] = True
            nums[i] -= k
        else:
            i = j+1
    
        for j in reversed(xrange(i, j+1)):
            if not op1:
                break
            op1 -= 1
            if k%2 == 1 and nums[j]%2 == 1:
                cnt += 1
            nums[j] = (nums[j]+1)//2
        else:
            j = i-1

        arr = sorted((nums[idx], idx) for idx in xrange(i))
        for _ in xrange(op1):
            x, idx = arr.pop()
            nums[idx] = (x+1)//2
            if cnt and lookup[idx]:
                cnt -= 1
                nums[idx] -= 1
        return sum(nums)