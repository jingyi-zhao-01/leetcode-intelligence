# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: ugly-number
# source_path: LeetCode-Solutions-master/Python/ugly-number.py
# solution_class: Solution
# submission_id: ba5f7738eab3c63d11c7d61a58159e7f722e3515
# seed: 2260279837

# Time:  O(logn) = O(1)
# Space: O(1)

class Solution(object):
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1