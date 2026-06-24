# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: encode-number
# source_path: LeetCode-Solutions-master/Python/encode-number.py
# solution_class: Solution
# submission_id: a9b88dcdc06248c8e74f8997ec7eb9eaf3072e99
# seed: 554027336

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        while num:
            result.append('0' if num%2 else '1')
            num = (num-1)//2
        return "".join(reversed(result))