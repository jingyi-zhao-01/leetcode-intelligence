# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-triplets-that-can-form-two-arrays-of-equal-xor
# source_path: LeetCode-Solutions-master/Python/count-triplets-that-can-form-two-arrays-of-equal-xor.py
# solution_class: Solution
# submission_id: 668e9ad8abb5f6a3c900bba197d67871eacb5862
# seed: 1703083745

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count_sum = collections.defaultdict(lambda: [0, 0])
        count_sum[0] = [1, 0]
        result, prefix = 0, 0
        for i, x in enumerate(arr):
            prefix ^= x
            c, t = count_sum[prefix]
            # sum(i-(j+1) for j in index[prefix])
            # = len(index[prefix])*i - sum((j+1) for j in index[prefix])
            result += c*i - t
            count_sum[prefix] = [c+1, t+i+1]
        return result