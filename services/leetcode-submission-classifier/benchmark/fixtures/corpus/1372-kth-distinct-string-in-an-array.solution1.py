# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kth-distinct-string-in-an-array
# source_path: LeetCode-Solutions-master/Python/kth-distinct-string-in-an-array.py
# solution_class: Solution
# submission_id: ce5b56c809ddc2f9dbc0f0c14ba52ceafb768139
# seed: 1049687047

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        count = collections.Counter(arr)
        arr = [x for x in arr if count[x] == 1]
        return arr[k-1] if k-1 < len(arr) else ""