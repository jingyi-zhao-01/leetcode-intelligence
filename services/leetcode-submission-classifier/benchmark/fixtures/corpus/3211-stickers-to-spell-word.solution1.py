# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: stickers-to-spell-word
# source_path: LeetCode-Solutions-master/Python/stickers-to-spell-word.py
# solution_class: Solution
# submission_id: de62b55ec7632210f658922f6b7a174e1afe9fae
# seed: 3767688936

# Time:  O(T * S^T)
# Space: O(T * S^T)

import collections

class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        def minStickersHelper(sticker_counts, target, dp):
            if "".join(target) in dp:
                return dp["".join(target)]
            target_count = collections.Counter(target)
            result = float("inf")
            for sticker_count in sticker_counts:
                if sticker_count[target[0]] == 0:
                    continue
                new_target = []
                for k in target_count.keys():
                    if target_count[k] > sticker_count[k]:
                       new_target += [k]*(target_count[k] - sticker_count[k])
                if len(new_target) != len(target):
                    num = minStickersHelper(sticker_counts, new_target, dp)
                    if num != -1:
                        result = min(result, 1+num)
            dp["".join(target)] = -1 if result == float("inf") else result
            return dp["".join(target)]

        sticker_counts = map(collections.Counter, stickers)
        dp = { "":0 }
        return minStickersHelper(sticker_counts, target, dp)