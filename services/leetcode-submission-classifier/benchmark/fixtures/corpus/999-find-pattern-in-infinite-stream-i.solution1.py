# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-pattern-in-infinite-stream-i
# source_path: LeetCode-Solutions-master/Python/find-pattern-in-infinite-stream-i.py
# solution_class: Solution
# submission_id: a4357d606e04c6d4aef8141881e471d2896437f2
# seed: 2323501977

# Time:  O(p + n)
# Space: O(p)

class InfiniteStream:
    def next(self):
        pass


# kmp

class Solution(object):
    def findPattern(self, stream, pattern):
        """
        :type stream: InfiniteStream
        :type pattern: List[int]
        :rtype: int
        """
        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in xrange(1, len(pattern)):
                while j+1 > 0 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        prefix = getPrefix(pattern)
        i = j = -1
        while True:
            d = stream.next()
            i += 1
            while j+1 > 0 and pattern[j+1] != d:
                j = prefix[j]
            if pattern[j+1] == d:
                j += 1
            if j+1 == len(pattern):
                return i-j
        return -1