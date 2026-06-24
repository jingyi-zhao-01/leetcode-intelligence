# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: apply-substitutions
# source_path: LeetCode-Solutions-master/Python/apply-substitutions.py
# solution_class: Solution2
# submission_id: 4cae64f6061b16a11a36571244a6e0a064d2f17b
# seed: 535149545

# Time:  O(r * 2^r)
# Space: O(r * 2^r)

import collections


# topological sort

class Solution2(object):
    def applySubstitutions(self, replacements, text):
        """
        :type replacements: List[List[str]]
        :type text: str
        :rtype: str
        """
        lookup = {k:v for k, v in replacements}
        memo = {}
        def replace(s):
            if s not in memo:
                result = []
                i = 0
                while i < len(s):
                    if s[i] != '%':
                        result.append(s[i])
                        i += 1
                        continue
                    j = next(j for j in xrange(i+1, len(s)) if s[j] == '%')
                    result.append(replace(lookup[s[i+1:j]]))
                    i = j+1
                memo[s] = "".join(result)
            return memo[s]

        return replace(text)