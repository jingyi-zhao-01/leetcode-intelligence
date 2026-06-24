# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-chunks-to-make-sorted-ii
# source_path: LeetCode-Solutions-master/Python/max-chunks-to-make-sorted-ii.py
# solution_class: Solution2
# submission_id: da8b1d4b6dede82f36d7de3da6fd425814b04afd
# seed: 3396245022

# Time:  O(n)
# Space: O(n)

# mono stack solution

class Solution2(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def compare(i1, i2):
            return arr[i1]-arr[i2] if arr[i1] != arr[i2] else i1-i2

        idxs = [i for i in xrange(len(arr))]
        result, max_i = 0, 0
        for i, v in enumerate(sorted(idxs, cmp=compare)):
            max_i = max(max_i, v)
            if max_i == i:
                result += 1
        return result