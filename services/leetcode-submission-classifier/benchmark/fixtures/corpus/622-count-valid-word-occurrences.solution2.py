# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-valid-word-occurrences
# source_path: LeetCode-Solutions-master/Python/count-valid-word-occurrences.py
# solution_class: Solution2
# submission_id: 70f05f6bf2076f3251a94e33a9edf2d6f2974e30
# seed: 137246612

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution2(object):
    def countWordOccurrences(self, chunks, queries):
        """
        :type chunks: List[str]
        :type queries: List[str]
        :rtype: List[int]
        """
        def check(i):
            return (
                s[i].islower() or
                (s[i] == '-' and
                 (i-1 >= 0 and s[i-1].islower()) and
                 (i+1 < len(s) and s[i+1].islower())
                )
            )

        s = "".join(chunks)
        curr = []
        cnt = collections.defaultdict(int)
        for i in xrange(len(s)):
            if check(i):
                curr.append(s[i])
                continue
            if curr:
                cnt["".join(curr)] += 1
                curr = []
        if curr:
            cnt["".join(curr)] += 1
            curr = []
        return [cnt[x] if x in cnt else 0 for x in queries]