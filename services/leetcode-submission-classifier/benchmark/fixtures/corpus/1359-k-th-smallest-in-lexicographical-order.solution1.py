# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-th-smallest-in-lexicographical-order
# source_path: LeetCode-Solutions-master/Python/k-th-smallest-in-lexicographical-order.py
# solution_class: Solution
# submission_id: 82aae44864a82ad10c3a6e4e14e36e794f85a349
# seed: 1493217610

# Time:  O(logn)
# Space: O(logn)

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result = 0

        cnts = [0] * 10
        for i in xrange(1, 10):
            cnts[i] = cnts[i - 1] * 10 + 1

        nums = []
        i = n
        while i:
            nums.append(i % 10)
            i /= 10

        total, target = n, 0
        i = len(nums) - 1
        while i >= 0 and k > 0:
            target = target*10 + nums[i]
            start = int(i == len(nums)-1)
            for j in xrange(start, 10):
                candidate = result*10 + j
                if candidate < target:
                    num = cnts[i+1]
                elif candidate > target:
                    num = cnts[i]
                else:
                    num = total - cnts[i + 1]*(j-start) - cnts[i]*(9-j)
                if k > num:
                    k -= num
                else:
                    result = candidate
                    k -= 1
                    total = num-1
                    break
            i -= 1

        return result