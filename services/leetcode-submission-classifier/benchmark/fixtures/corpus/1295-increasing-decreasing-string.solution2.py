# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: increasing-decreasing-string
# source_path: LeetCode-Solutions-master/Python/increasing-decreasing-string.py
# solution_class: Solution2
# submission_id: 233bac3c05cc630e069f1b626dc00f0ea2e002eb
# seed: 3320295940

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result, count, desc = [], collections.Counter(s), False
        while count:
            for c in sorted(count.keys(), reverse=desc):
                result.append(c)
                count[c] -= 1
                if not count[c]:
                    del count[c]
            desc = not desc
        return "".join(result)