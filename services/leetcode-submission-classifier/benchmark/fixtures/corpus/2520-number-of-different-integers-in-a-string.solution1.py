# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-different-integers-in-a-string
# source_path: LeetCode-Solutions-master/Python/number-of-different-integers-in-a-string.py
# solution_class: Solution
# submission_id: bc350a91159c2c68729c4c5cd4e4f666f4fdbde3
# seed: 3691564671

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        result, num = set(), None
        for i in xrange(len(word)+1):
            c = word[i] if i < len(word) else ' '
            if c.isdigit():
                num = 10*num+int(c) if num is not None else int(c)
            elif num is not None:
                result.add(num)
                num = None
        return len(result)