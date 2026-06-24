# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-smallest-string-after-substring-operation
# source_path: LeetCode-Solutions-master/Python/lexicographically-smallest-string-after-substring-operation.py
# solution_class: Solution
# submission_id: 832c77f92c132d29d0d0acad464e5ef4933d731f
# seed: 2480611089

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def smallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        i = next((i for i in xrange(len(s)) if s[i] != 'a'), len(s))
        if i == len(s):
            result[-1] = 'z'
        else:
            for i in xrange(i, len(s)):
                if result[i] == 'a':
                    break
                result[i] = chr(ord(result[i])-1)
        return "".join(result)