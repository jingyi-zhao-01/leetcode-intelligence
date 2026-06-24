# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: length-of-the-longest-increasing-path
# source_path: LeetCode-Solutions-master/Python/length-of-the-longest-increasing-path.py
# solution_class: Solution
# submission_id: d89461097cbf7e064bc05cb04f751a19c1d1f399
# seed: 3015103452

# Time:  O(nlogn)
# Space: O(n)

import bisect


# sort, binary search, longest increasing subsequence, lis

class Solution(object):
    def maxPathLength(self, coordinates, k):
        """
        :type coordinates: List[List[int]]
        :type k: int
        :rtype: int
        """
        def longest_increasing_subsequence(arr):
            result = []
            for x in arr:
                i = bisect.bisect_left(result, x)
                if i == len(result):
                    result.append(x)
                else:
                    result[i] = x
            return len(result)

        target = coordinates[k]
        coordinates.sort(key=lambda x: (x[0], -x[1]))
        left, right = [], []
        for x, y in coordinates:
            if x < target[0] and y < target[1]:
                left.append(y)
            elif x > target[0] and y > target[1]:
                right.append(y)
        return longest_increasing_subsequence(left)+1+longest_increasing_subsequence(right)