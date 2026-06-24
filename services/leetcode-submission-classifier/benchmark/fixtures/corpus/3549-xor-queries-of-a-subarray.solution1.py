# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: xor-queries-of-a-subarray
# source_path: LeetCode-Solutions-master/Python/xor-queries-of-a-subarray.py
# solution_class: Solution
# submission_id: a7bc9ad413c33e3ac38fd7c7f6ec18f9717cef0a
# seed: 153869186

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        for i in xrange(1, len(arr)):
            arr[i] ^= arr[i-1]
        return [arr[right] ^ arr[left-1] if left else arr[right] for left, right in queries]