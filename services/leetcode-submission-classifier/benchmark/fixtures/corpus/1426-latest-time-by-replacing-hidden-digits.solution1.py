# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: latest-time-by-replacing-hidden-digits
# source_path: LeetCode-Solutions-master/Python/latest-time-by-replacing-hidden-digits.py
# solution_class: Solution
# submission_id: 168880e933d51ecb40a9b4d2f616c73ec6a34117
# seed: 2049216845

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        result = list(time)
        for i, c in enumerate(time): 
            if c != "?":
                continue
            if i == 0:
                result[i] = '2' if result[i+1] in "?0123" else '1'
            elif i == 1:
                result[i] = '3' if result[0] == '2' else '9'
            elif i == 3:
                result[i] = '5'
            elif i == 4:
                result[i] = '9'
        return "".join(result)