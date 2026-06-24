# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k
# source_path: LeetCode-Solutions-master/Python/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k.py
# solution_class: Solution
# submission_id: 260a9f95d63383c133bf4c696c70ac0ed5d5f2aa
# seed: 3592784231

# Time:  O(max(logk, x) * log((logk) / x))
# Space: O((logk) / x)

# bit manipulation, binary search, combinatorics

class Solution(object):
    def findMaximumNumber(self, k, x):
        """
        :type k: int
        :type x: int
        :rtype: int
        """
        def floor_log2(x):
            return x.bit_length()-1

        def binary_search_right(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right
    
        def count(l):
            return (prefix_cnt<<(x*l))+lookup[l]

        result = prefix_cnt = 0
        lookup = [0]
        i = 0
        while (lookup[-1]<<x)+(1<<(i+x-1)) <= k:
            lookup.append((lookup[-1]<<x)+(1<<(i+x-1)))
            i += x
        while k >= prefix_cnt:
            # l = result.bit_length()
            # assert(prefix_cnt == sum(c == '1' and (l-i)%x == 0 for i, c in enumerate(bin(result)[2:])))
            l = binary_search_right(1, len(lookup)-1, lambda l: count(l) <= k)
            cnt, i = count(l), x*l
            c = min(floor_log2(k//cnt) if cnt else float("inf"), x-1)
            cnt <<= c
            i += c
            k -= cnt
            result += 1<<i
            prefix_cnt += int((i+1)%x == 0)
        return result-1