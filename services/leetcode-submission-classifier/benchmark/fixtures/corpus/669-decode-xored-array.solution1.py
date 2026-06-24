# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: decode-xored-array
# source_path: LeetCode-Solutions-master/Python/decode-xored-array.py
# solution_class: Solution
# submission_id: 192356e6d8de139ce5aad3645e781283006436bd
# seed: 1792624223

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        result = [first]
        for x in encoded:
            result.append(result[-1]^x)
        return result