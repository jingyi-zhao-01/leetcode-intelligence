# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-number-after-digit-swaps-by-parity
# source_path: LeetCode-Solutions-master/Python/largest-number-after-digit-swaps-by-parity.py
# solution_class: Solution
# submission_id: 2d8c9f4002481e700d7a91993805433da2869eef
# seed: 3731293691

# Time:  O(logn)
# Space: O(1)

# counting sort

class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        def count(num):
            cnt = [0]*10
            while num:
                num, d = divmod(num, 10)
                cnt[d] += 1
            return cnt

        cnt = count(num)
        result = 0
        digit = [0, 1]
        base = 1
        while num:
            num, d = divmod(num, 10)
            while not cnt[digit[d%2]]:
                digit[d%2] += 2
            cnt[digit[d%2]] -= 1
            result += digit[d%2]*base
            base *= 10
        return result