# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-the-beauty-of-the-garden
# source_path: LeetCode-Solutions-master/Python/maximize-the-beauty-of-the-garden.py
# solution_class: Solution
# submission_id: 70d9a877b04ad947946b6f8d4cfd77b284d596c4
# seed: 74156508

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def maximumBeauty(self, flowers):
        """
        :type flowers: List[int]
        :rtype: int
        """
        lookup = {}
        prefix = [0]
        result = float("-inf")
        for i, f in enumerate(flowers):
            prefix.append(prefix[-1]+f if f > 0 else prefix[-1])
            if not f in lookup:
                lookup[f] = i
                continue
            result = max(result, 2*f+prefix[i+1]-prefix[lookup[f]] if f < 0 else prefix[i+1]-prefix[lookup[f]])
        return result