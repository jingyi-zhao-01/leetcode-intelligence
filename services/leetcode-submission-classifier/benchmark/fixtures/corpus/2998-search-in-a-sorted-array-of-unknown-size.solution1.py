# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: search-in-a-sorted-array-of-unknown-size
# source_path: LeetCode-Solutions-master/Python/search-in-a-sorted-array-of-unknown-size.py
# solution_class: Solution
# submission_id: bc176b1970443fa8ed94dd767edc1a8f56b825ab
# seed: 4001207881

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 19999
        while left <= right:
            mid = left + (right-left)//2
            response = reader.get(mid)
            if response > target:
                right = mid-1
            elif response < target:
                left = mid+1
            else:
                return mid
        return -1