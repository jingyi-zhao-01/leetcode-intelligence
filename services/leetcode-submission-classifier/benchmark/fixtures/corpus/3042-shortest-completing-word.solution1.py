# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-completing-word
# source_path: LeetCode-Solutions-master/Python/shortest-completing-word.py
# solution_class: Solution
# submission_id: bb81f4a18b52b0c156f6fdbea228882a5eeccf5d
# seed: 304472628

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def contains(counter1, w2):
            c2 = collections.Counter(w2.lower())
            c2.subtract(counter1)
            return all(map(lambda x: x >= 0, c2.values()))

        result = None
        counter = collections.Counter(c.lower() for c in licensePlate if c.isalpha())
        for word in words:
            if (result is None or (len(word) < len(result))) and \
               contains(counter, word):
                result = word
        return result