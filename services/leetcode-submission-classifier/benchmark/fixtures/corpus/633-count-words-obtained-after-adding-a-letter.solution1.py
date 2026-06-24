# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-words-obtained-after-adding-a-letter
# source_path: LeetCode-Solutions-master/Python/count-words-obtained-after-adding-a-letter.py
# solution_class: Solution
# submission_id: 54431bcbee3a1a71fdaacee79e6b9ab2478a7601
# seed: 1042838399

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        """
        def bitmask(w):
            return reduce(lambda x, y: x|y, (1 << (ord(c)-ord('a')) for i, c in enumerate(w)))

        lookup = set(bitmask(w) for w in startWords)
        result = 0 
        for w in targetWords: 
            mask = bitmask(w)
            result += any(mask ^ (1 << ord(c)-ord('a')) in lookup for c in w)
        return result 