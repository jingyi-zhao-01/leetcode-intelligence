# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: daily-temperatures
# source_path: LeetCode-Solutions-master/Python/daily-temperatures.py
# solution_class: Solution
# submission_id: 372945eed24955093ce667a545059d182c744be9
# seed: 3263415329

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stk = []
        for i in xrange(len(temperatures)):
            while stk and \
                  temperatures[stk[-1]] < temperatures[i]:
                idx = stk.pop()
                result[idx] = i-idx
            stk.append(i)
        return result