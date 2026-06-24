# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: generate-binary-strings-without-adjacent-zeros
# source_path: LeetCode-Solutions-master/Python/generate-binary-strings-without-adjacent-zeros.py
# solution_class: Solution2
# submission_id: 8970b51e1baaaa3a76b36df433d6dd059be10c38
# seed: 1720201634

# Time:  O(n * 2^n)
# Space: O(n)

# backtracking

class Solution2(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        q = [[]]
        for _ in xrange(n):
            new_q = []
            for x in q:
                if not x or x[-1] == '1':
                    new_q.append(x+['0'])
                new_q.append(x+['1'])
            q = new_q
        return ["".join(x) for x in q]