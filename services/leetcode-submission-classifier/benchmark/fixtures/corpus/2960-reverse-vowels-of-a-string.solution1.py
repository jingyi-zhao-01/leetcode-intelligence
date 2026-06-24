# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-vowels-of-a-string
# source_path: LeetCode-Solutions-master/Python/reverse-vowels-of-a-string.py
# solution_class: Solution
# submission_id: 4701be0fc8149548e5c15c918cdd407e58439c7f
# seed: 1477722700

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiou"
        string = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if string[i].lower() not in vowels:
                i += 1
            elif string[j].lower() not in vowels:
                j -= 1
            else:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
        return "".join(string)