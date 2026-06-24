# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: keyboard-row
# source_path: LeetCode-Solutions-master/Python/keyboard-row.py
# solution_class: Solution
# submission_id: a7fff3ef44d7f03f3f3be06bd42717fd886d839e
# seed: 3561174482

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [set(['q', 'w', 'e', 'r', 't', 'y','u', 'i', 'o', 'p']),
                set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']),
                set(['z', 'x', 'c', 'v', 'b' ,'n', 'm'])]

        result = []
        for word in words:
            k = 0
            for i in xrange(len(rows)):
                if word[0].lower() in rows[i]:
                    k = i
                    break
            for c in word:
                if c.lower() not in rows[k]:
                    break
            else:
                result.append(word)
        return result