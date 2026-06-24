# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-happy-string
# source_path: LeetCode-Solutions-master/Python/longest-happy-string.py
# solution_class: Solution2
# submission_id: df11bbd454b07a8c553d34659c08ab914cb5996d
# seed: 1312906694

# Time:  O(n)
# Space: O(1)

import heapq

class Solution2(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        choices = [[a, 'a'], [b, 'b'], [c, 'c']]
        result = []
        for _ in xrange(a+b+c):
            choices.sort(reverse=True)
            for i, (x, c) in enumerate(choices):
                if x and result[-2:] != [c, c]:
                    result.append(c)
                    choices[i][0] -= 1
                    break
            else:
                break
        return "".join(result)