# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: intersection-of-three-sorted-arrays
# source_path: LeetCode-Solutions-master/Python/intersection-of-three-sorted-arrays.py
# solution_class: Solution2
# submission_id: a673662c16a184b727832018743d2292fae79188
# seed: 1524491881

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        intersect = reduce(set.intersection, map(set, [arr2, arr3]))
        return [x for x in arr1 if x in intersect]