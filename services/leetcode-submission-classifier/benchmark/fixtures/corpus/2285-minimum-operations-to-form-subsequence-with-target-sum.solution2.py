# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-form-subsequence-with-target-sum
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-form-subsequence-with-target-sum.py
# solution_class: Solution2
# submission_id: 50cdbef1600f0e24631edb022d7e4ef2b5cc539d
# seed: 368398626

# Time:  O(n)
# Space: O(logn)

# codeforces, https://codeforces.com/problemset/problem/1303/D
# counting sort, greedy

class Solution2(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums)
        if total < target:
            return -1

        nums.sort()
        result = 0
        while target:
            x = nums.pop()
            if x <= target:
                target -= x
                total -= x
            elif total-x >= target:
                total -= x
            else:
                nums.append(x//2)
                nums.append(x//2)
                result += 1
        return result