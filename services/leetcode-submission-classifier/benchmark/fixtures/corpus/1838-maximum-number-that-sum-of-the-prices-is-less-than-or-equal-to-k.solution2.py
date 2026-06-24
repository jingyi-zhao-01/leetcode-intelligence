# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k
# source_path: LeetCode-Solutions-master/Python/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k.py
# solution_class: Solution2
# submission_id: 8a0abb0668efed7271d1a7db99d0f3a5375896c8
# seed: 2641728497

# Time:  O(max(logk, x) * log((logk) / x))
# Space: O((logk) / x)

# bit manipulation, binary search, combinatorics

class Solution2(object):
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
            while (cnt<<x)+(1<<(i+x-1)) <= k:
                cnt = (cnt<<x)+(1<<(i+x-1))
                i += x
            c = min(floor_log2(k//cnt) if cnt else float("inf"), x-1)
            cnt <<= c
            i += c
            k -= cnt
            result += 1<<i
            prefix_cnt += int((i+1)%x == 0)
        return result-1