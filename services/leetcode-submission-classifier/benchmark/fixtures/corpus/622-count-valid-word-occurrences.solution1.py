# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-valid-word-occurrences
# source_path: LeetCode-Solutions-master/Python/count-valid-word-occurrences.py
# solution_class: Solution
# submission_id: cb9961de132560f01fffb0f7610cbcd7f3474774
# seed: 873352675

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def countWordOccurrences(self, chunks, queries):
        """
        :type chunks: List[str]
        :type queries: List[str]
        :rtype: List[int]
        """
        def check(i, j):
            return (
                chunks[i][j].islower() or
                (chunks[i][j] == '-' and
                 (curr and curr[-1].islower()) and
                 ((j+1 < len(chunks[i]) and chunks[i][j+1].islower()) or (j+1 == len(chunks[i]) and i+1 < len(chunks) and chunks[i+1][0].islower()))
                )
            )

        curr = []
        cnt = collections.defaultdict(int)
        for i in xrange(len(chunks)):
            for j in xrange(len(chunks[i])):
                if check(i, j):
                    curr.append(chunks[i][j])
                    continue
                if curr:
                    cnt["".join(curr)] += 1
                    curr = []
        if curr:
            cnt["".join(curr)] += 1
            curr = []
        return [cnt[x] if x in cnt else 0 for x in queries]