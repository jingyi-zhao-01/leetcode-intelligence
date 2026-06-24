# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-smallest-string-after-applying-operations
# source_path: LeetCode-Solutions-master/Python/lexicographically-smallest-string-after-applying-operations.py
# solution_class: Solution
# submission_id: 56d8345faf9ad2a6cd43f4740143631c1704e19c
# seed: 1031548880

# Time:  O(100 * n^2) = O(n^2)
# Space: O(1)

class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        def less(s, i, j):
            for k in xrange(len(s)):
                if s[(k+i)%len(s)] != s[(k+j)%len(s)]:
                    return s[(k+i)%len(s)] < s[(k+j)%len(s)]
            return False

        s = list(s)
        result = s[:]
        even = [False]*10
        while not even[int(s[0])]:  # at most O(10) times
            even[int(s[0])] = True
            odd = [False]*10
            while not odd[int(s[1])]:  # at most O(10) times
                odd[int(s[1])] = True
                best_rotate = 0
                lookup = [False]*len(s)
                i = b
                while not lookup[i]:  # find best rotation, at most O(n) times
                    lookup[i] = True
                    if less(s, i, best_rotate):  # O(n) time
                        best_rotate = i
                    i = (i+b)%len(s)
                result = min(result, s[best_rotate:] + s[:best_rotate])
                for k in xrange(1, len(s), 2):  # flip odd index
                    s[k] = str((int(s[k])+a) % 10)
            if b%2:  # if rotate length is odd, even index could be also flipped
                for k in xrange(0, len(s), 2):  # flip even index
                    s[k] = str((int(s[k])+a) % 10)
        return "".join(result)