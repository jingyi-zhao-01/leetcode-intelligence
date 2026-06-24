# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-divisible-digit-product-ii
# source_path: LeetCode-Solutions-master/Python/smallest-divisible-digit-product-ii.py
# solution_class: Solution
# submission_id: 9b1fdb7115c20fe9a8d06dadd3498fdd6ca89e78
# seed: 1549361011

# Time:  O(n + logt)
# Space: O(1)

# freq table, greedy, prefix sum, number theory

class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        LOOKUP = [[(0, 0, 0, 0), (0, 1, 0, 0)],
                  [(1, 0, 0, 0), (0, 0, 0, 1)],
                  [(0, 0, 1, 0), (1, 0, 0, 1)]]
        def count(x):
            cnt = [0]*10
            for i in xrange(2, 9+1):
                while x%i == 0:
                    x //= i
                    cnt[i] += 1
                if x == 1:
                    return cnt
            return []
    
        def update(total, cnt, d):
            for i, x in enumerate(cnt):
                total[i] += d*x

        def diff(expect, total):
            return [max(expect[i]-total[i], 0) for i in xrange(len(expect))]

        def min_factors(cnt):
            cnt8, r2 = divmod(cnt[2], 3)
            cnt9, r3 = divmod(cnt[3], 2)
            cnt2, cnt3, cnt4, cnt6 = LOOKUP[r2][r3]
            return (cnt2, cnt3, cnt4, cnt[5], cnt6, cnt[7], cnt8, cnt9)
    
        def format(cnt, l):
            return '1'*(l-sum(cnt))+"".join(str(x)*cnt[x-2] for x in xrange(2, 9+1))
    
        expect = count(t)
        if not expect:
            return "-1"
        nums = map(int, num)
        i = next((i for i in xrange(len(nums)) if not nums[i]), len(nums))
        for j in xrange(i, len(nums)):
            nums[j] = 1
        total = [0]*10
        for x in nums:
            update(total, count(x), +1)
        if all(d == 0 for d in diff(expect, total)):
            return "".join(map(str, nums))
        for i in reversed(xrange(len(nums))):
            update(total, count(nums[i]), -1)
            for x in xrange(nums[i]+1, 9+1):
                update(total, count(x), +1)
                tmp = min_factors(diff(expect, total))
                update(total, count(x), -1)
                if sum(tmp) > len(nums)-1-i:
                    continue
                return "".join(map(str, nums[:i]))+str(x)+format(tmp, len(nums)-1-i)
        return format(min_factors(diff(expect, total)), len(nums)+1)