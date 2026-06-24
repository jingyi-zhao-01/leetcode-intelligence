# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: earliest-possible-day-of-full-bloom
# source_path: LeetCode-Solutions-master/Python/earliest-possible-day-of-full-bloom.py
# solution_class: Solution
# submission_id: db7fb4c8b2c878c743337895004b3a812130b477
# seed: 2863741266

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        order = range(len(growTime))
        order.sort(key=lambda x: growTime[x], reverse=True)
        result = curr = 0
        for i in order:
            curr += plantTime[i]
            result = max(result, curr+growTime[i])
        return result