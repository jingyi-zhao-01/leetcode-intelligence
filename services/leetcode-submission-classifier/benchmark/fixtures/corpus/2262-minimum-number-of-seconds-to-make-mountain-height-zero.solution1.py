# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-seconds-to-make-mountain-height-zero
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-seconds-to-make-mountain-height-zero.py
# solution_class: Solution
# submission_id: 1745494b671b0f22d2758ff5b54ab04c5f60f238
# seed: 2775252770

# Time:  O(nlogr), r = min(workerTimes) * (mountainHeight + 1) * mountainHeight / 2
# Space: O(1)

# binary search, quadratic equation

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        def binary_search(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left

        def check(target):
            # t * (1 + 2 + 3 + ... + x) <= target
            # t * (x+1)*x/2 <= target
            # x^2+x-2*target/t <= 0
            # x <= (-1+(1+8*target/t)**0.5)/2
            return sum(int((-1+(1+8*target/t)**0.5)/2) for t in workerTimes) >= mountainHeight
    
        mn = min(workerTimes)
        left, right = mn, mn*(mountainHeight+1)*mountainHeight//2
        return binary_search(left, right, check)