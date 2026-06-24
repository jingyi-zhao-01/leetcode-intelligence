# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-price-to-fill-a-bag
# source_path: LeetCode-Solutions-master/Python/maximum-price-to-fill-a-bag.py
# solution_class: Solution
# submission_id: c4408105bf6916abeede8fd4600f89af38bfe9f2
# seed: 2184959466

# Time:  O(nlogn)
# Space: O(1)

# greedy, sort

class Solution(object):
    def maxPrice(self, items, capacity):
        """
        :type items: List[List[int]]
        :type capacity: int
        :rtype: float
        """
        result = 0
        items.sort(key=lambda x: float(x[0])/x[1], reverse=True)
        for p, c in items:
            cnt = min(c, capacity)
            capacity -= cnt
            result += (float(p)/c)*cnt
        return result if capacity == 0 else -1