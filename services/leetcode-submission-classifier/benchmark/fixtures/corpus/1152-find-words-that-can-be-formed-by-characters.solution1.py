# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-words-that-can-be-formed-by-characters
# source_path: LeetCode-Solutions-master/Python/find-words-that-can-be-formed-by-characters.py
# solution_class: Solution
# submission_id: c543f45711253dc4d480638fff0e52b53031ff77
# seed: 1137540894

# Time:  O(m * n), m is the length of chars, n is the number of words
# Space: O(1)

import collections

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        def check(word, chars, count):
            if len(word) > len(chars):
                return False
            curr_count = collections.Counter()
            for c in word:
                curr_count[c] += 1
                if c not in count or count[c] < curr_count[c]:
                    return False
            return True
        
        count = collections.Counter(chars)
        return sum(len(word) for word in words if check(word, chars, count))