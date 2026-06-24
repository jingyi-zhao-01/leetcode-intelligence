# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k
# source_path: LeetCode-Solutions-master/Python/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k.py
# solution_class: Solution3
# submission_id: 9f36df5898df454fb2708b85bade5353c24e1b97
# seed: 1003718610

# Time:  O(max(logk, x) * log((logk) / x))
# Space: O((logk) / x)

# bit manipulation, binary search, combinatorics

class Solution3(object):
    def findMaximumNumber(self, k, x):
        """
        :type k: int
        :type x: int
        :rtype: int
        """
        def floor_log2(x):
            return x.bit_length()-1

        result = prefix_cnt = 0
        while k >= prefix_cnt:
            # l = result.bit_length()
            # assert(prefix_cnt == sum(c == '1' and (l-i)%x == 0 for i, c in enumerate(bin(result)[2:])))
            cnt, i = prefix_cnt, 0
            while (cnt<<1)+(1<<i if (i+1)%x == 0 else 0) <= k:
                cnt = (cnt<<1)+(1<<i if (i+1)%x == 0 else 0)
                i += 1
            k -= cnt
            result += 1<<i
            prefix_cnt += int((i+1)%x == 0)
        return result-1