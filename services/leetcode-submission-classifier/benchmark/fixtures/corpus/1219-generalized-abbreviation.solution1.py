# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: generalized-abbreviation
# source_path: LeetCode-Solutions-master/Python/generalized-abbreviation.py
# solution_class: Solution
# submission_id: fe0738c700f793a66bcd6d24ca795bc29ec3299c
# seed: 1331791882

# Time:  O(n * 2^n)
# Space: O(n)

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def generateAbbreviationsHelper(word, i, cur, res):
            if i == len(word):
                res.append("".join(cur))
                return
            cur.append(word[i])
            generateAbbreviationsHelper(word, i + 1, cur, res)
            cur.pop()
            if not cur or not cur[-1][-1].isdigit():
                for l in xrange(1, len(word) - i + 1):
                    cur.append(str(l))
                    generateAbbreviationsHelper(word, i + l, cur, res)
                    cur.pop()

        res, cur = [], []
        generateAbbreviationsHelper(word, 0, cur, res)
        return res