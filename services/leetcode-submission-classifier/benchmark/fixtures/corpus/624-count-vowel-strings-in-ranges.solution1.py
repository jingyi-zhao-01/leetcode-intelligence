# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-vowel-strings-in-ranges
# source_path: LeetCode-Solutions-master/Python/count-vowel-strings-in-ranges.py
# solution_class: Solution
# submission_id: a025d4c148b90d745c698035650e424b9b41c292
# seed: 712632411

# Time:  O(n + q)
# Space: O(n)

# prefix sum

class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        VOWELS = {'a', 'e', 'i', 'o', 'u'}
        prefix = [0]*(len(words)+1)
        for i, w in enumerate(words):
            prefix[i+1] = prefix[i]+int(w[0] in VOWELS and w[-1] in VOWELS)
        return [prefix[r+1]-prefix[l] for l, r in queries]