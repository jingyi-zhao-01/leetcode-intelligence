# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-only-letters
# source_path: LeetCode-Solutions-master/Python/reverse-only-letters.py
# solution_class: Solution
# submission_id: 3a5918af8245c6bcdb1e8c24d036ca0933525804
# seed: 4287124341

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        def getNext(S):
            for i in reversed(xrange(len(S))):
                if S[i].isalpha():
                    yield S[i]

        result = []
        letter = getNext(S)
        for i in xrange(len(S)):
            if S[i].isalpha():
                result.append(letter.next())
            else:
                result.append(S[i])
        return "".join(result)