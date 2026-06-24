# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-substrings-with-dominant-ones
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-substrings-with-dominant-ones.py
# solution_class: Solution
# submission_id: ffe7087fed003d6a5d6d79ddf5968e67dbe257ff
# seed: 2464662454

# Time:  O(n * sqrt(n)) = O(n^(3/2))
# Space: O(n)

# two pointers, sliding window

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        idxs = [-1]+[i for i, x in enumerate(s) if x == '0']+[len(s)]
        curr = 1
        for i in xrange(len(s)):
            if idxs[curr] == i:
                curr += 1
            for c in xrange(min(int((-1+(1+4*(i+1))**0.5)/2)+1, curr)):  # since c^2 <= (i+1)-c, thus c <= (-1+(1+4*(i+1))**0.5)/2
                if c**2 <= (i-idxs[(curr-c)-1])-c:
                    result += min(min(idxs[curr-c], i)-idxs[(curr-c)-1], ((i-idxs[(curr-c)-1])-c)-c**2+1)
        return result