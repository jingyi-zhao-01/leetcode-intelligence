# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: good-indices-in-a-digit-string
# source_path: LeetCode-Solutions-master/Python/good-indices-in-a-digit-string.py
# solution_class: Solution
# submission_id: a296d6b1ff4dc714ed44d79eaa704fa80dadc3c2
# seed: 2343658761

# Time:  O(n)
# Space: O(1)

# math, sliding window

class Solution(object):
    def goodIndices(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        result = []
        curr, base = 0, 1
        for i in xrange(len(s)):
            if i == base*10:
                base *= 10
            curr = (curr%base)*10+(ord(s[i])-ord('0'))
            if curr == i:
                result.append(i)
        return result