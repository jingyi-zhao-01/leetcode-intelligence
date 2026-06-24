# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-vowels-in-a-string
# source_path: LeetCode-Solutions-master/Python/sort-vowels-in-a-string.py
# solution_class: Solution2
# submission_id: 0160186e10b049f7132ba01d99afd2a86aee3b4e
# seed: 1899667481

# Time:  O(n)
# Space: O(1)

# counting sort

class Solution2(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = "AEIOUaeiou"
        LOOKUP = set(VOWELS)
        vowels = [x for x in s if x in LOOKUP]
        vowels.sort(reverse=True)
        return "".join(vowels.pop() if x in LOOKUP else x for x in s)