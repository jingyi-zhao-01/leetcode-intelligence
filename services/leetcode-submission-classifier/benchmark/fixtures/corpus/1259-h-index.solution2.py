# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: h-index
# source_path: LeetCode-Solutions-master/Python/h-index.py
# solution_class: Solution2
# submission_id: 5fad5dbb3b904ac844604be0cabadcc1d4d772bb
# seed: 3496207684

# Time:  O(n)
# Space: O(n)

class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        for x in citations:
            if x >= h + 1:
                h += 1
            else:
                break
        return h