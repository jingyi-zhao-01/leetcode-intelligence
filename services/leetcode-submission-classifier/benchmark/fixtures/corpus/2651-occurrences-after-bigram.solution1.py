# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: occurrences-after-bigram
# source_path: LeetCode-Solutions-master/Python/occurrences-after-bigram.py
# solution_class: Solution
# submission_id: 1310591f9fcb9f8b5422015e939d7a5c5afa52ca
# seed: 3107005697

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        result = []
        first += ' '
        second += ' '
        third = []
        i, j, k = 0, 0, 0
        while k < len(text):
            c = text[k]
            k += 1
            if i != len(first):
                if c == first[i]:
                    i += 1
                else:
                    i = 0
                continue
            if j != len(second):
                if c == second[j]:
                    j += 1
                else:
                    k -= j+1
                    i, j = 0, 0
                continue
            if c != ' ':
                third.append(c)
                continue
            k -= len(second) + len(third) + 1
            i, j = 0, 0
            result.append("".join(third))
            third = []
        if third:
            result.append("".join(third))
        return result