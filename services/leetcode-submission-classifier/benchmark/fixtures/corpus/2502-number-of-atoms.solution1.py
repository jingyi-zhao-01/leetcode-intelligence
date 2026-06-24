# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-atoms
# source_path: LeetCode-Solutions-master/Python/number-of-atoms.py
# solution_class: Solution
# submission_id: 1a0d6518d7ca3e12f2b533cd7bf8e554b8aed07c
# seed: 592037403

# Time:  O(n)
# Space: O(n)

import collections
import re

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stk = [collections.Counter()]
        for name, m1, left_open, right_open, m2 in parse:
            if name:
              stk[-1][name] += int(m1 or 1)
            if left_open:
              stk.append(collections.Counter())
            if right_open:
                top = stk.pop()
                for k, v in top.iteritems():
                  stk[-1][k] += v * int(m2 or 1)

        return "".join(name + (str(stk[-1][name]) if stk[-1][name] > 1 else '') \
                       for name in sorted(stk[-1]))