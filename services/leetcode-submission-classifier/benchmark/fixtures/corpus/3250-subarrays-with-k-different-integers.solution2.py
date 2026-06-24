# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subarrays-with-k-different-integers
# source_path: LeetCode-Solutions-master/Python/subarrays-with-k-different-integers.py
# solution_class: Solution2
# submission_id: 51c389e96fc9ebbd571f502b1d572b6fc3f31779
# seed: 383053756

# Time:  O(n)
# Space: O(k)

import collections

class Solution2(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        window1, window2 = Window(), Window()
        result, left1, left2 = 0, 0, 0
        for i in A:
            window1.add(i)
            while window1.size() > K:
                window1.remove(A[left1])
                left1 += 1
            window2.add(i)
            while window2.size() >= K:
                window2.remove(A[left2])
                left2 += 1
            result += left2-left1
        return result