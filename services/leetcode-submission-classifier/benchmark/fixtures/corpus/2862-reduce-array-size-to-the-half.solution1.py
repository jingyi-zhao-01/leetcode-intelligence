# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reduce-array-size-to-the-half
# source_path: LeetCode-Solutions-master/Python/reduce-array-size-to-the-half.py
# solution_class: Solution
# submission_id: f0630cea3e973e2dff5b2615975cf18d2ca8dd93
# seed: 543558729

# Time:  O(n)
# Space: O(n)

import collections

        

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counting_sort = [0]*len(arr)
        count = collections.Counter(arr)
        for c in count.itervalues():
            counting_sort[c-1] += 1
        result, total = 0, 0
        for c in reversed(xrange(len(arr))):
            if not counting_sort[c]:
                continue
            count = min(counting_sort[c],
                        ((len(arr)+1)//2 - total - 1)//(c+1) + 1)
            result += count
            total += count*(c+1)
            if total >= (len(arr)+1)//2:
                break
        return result