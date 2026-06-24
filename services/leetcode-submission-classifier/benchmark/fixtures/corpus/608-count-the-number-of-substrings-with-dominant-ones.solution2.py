# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-substrings-with-dominant-ones
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-substrings-with-dominant-ones.py
# solution_class: Solution2
# submission_id: e37a388f8f430987fc0b92a14a2075a6c94b88f1
# seed: 3313556233

# Time:  O(n * sqrt(n)) = O(n^(3/2))
# Space: O(n)

# two pointers, sliding window

class Solution2(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        idxs = [-1]+[i for i, x in enumerate(s) if x == '0']+[len(s)]
        for c in xrange(int((-1+(1+4*len(s))**0.5)/2)+1):  # since c^2 <= n-c, thus c <= (-1+(1+4*n)**0.5)/2
            left = right = 1
            for i in xrange(len(s)):
                if idxs[right] == i:
                    right += 1
                if right-left == c+1:
                    left += 1
                if not (right-left == c and ((i-idxs[left-1])-c) >= c**2):
                    continue
                result += min(min(idxs[left], i)-idxs[left-1], ((i-idxs[left-1])-c)-c**2+1)
        return result