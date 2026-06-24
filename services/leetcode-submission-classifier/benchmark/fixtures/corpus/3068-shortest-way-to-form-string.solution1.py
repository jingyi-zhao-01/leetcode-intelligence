# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-way-to-form-string
# source_path: LeetCode-Solutions-master/Python/shortest-way-to-form-string.py
# solution_class: Solution
# submission_id: 7debbba6198b439ac096b877c4fbae78132d119a
# seed: 1556290078

# Time:  O(m + n), m is the length of source
#                , n is the length of target
# Space: O(m)

# greedy solution

class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        lookup = [[None for _ in xrange(26)] for _ in xrange(len(source)+1)]
        find_char_next_pos = [None]*26
        for i in reversed(xrange(len(source))):
            find_char_next_pos[ord(source[i])-ord('a')] = i+1
            lookup[i] = list(find_char_next_pos)

        result, start = 1, 0
        for c in target:
            start = lookup[start][ord(c)-ord('a')]
            if start != None:
                continue
            result += 1
            start = lookup[0][ord(c)-ord('a')]
            if start == None:
                return -1
        return result