# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: decode-xored-permutation
# source_path: LeetCode-Solutions-master/Python/decode-xored-permutation.py
# solution_class: Solution
# submission_id: add0e526262292504c5437f0347e29968c9c229e
# seed: 3300586117

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        curr = 0
        for i in xrange(1, (len(encoded)+1) + 1):
            curr ^= i
            if i < len(encoded) and i%2 == 1:
                curr ^= encoded[i]
        result = [curr]
        for x in encoded:
            result.append(result[-1]^x)
        return result