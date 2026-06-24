# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-after-k-increments
# source_path: LeetCode-Solutions-master/Python/maximum-product-after-k-increments.py
# solution_class: Solution2
# submission_id: cc09d6344ebf88d0fd2acdda8114f088795f7bc2
# seed: 3550173507

# Time:  O(nlogn)
# Space: O(1)

# math, sort

class Solution2(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        cnt = collections.Counter(nums)
        min_num = min(cnt.iterkeys())
        while k:
            c = min(cnt[min_num], k)
            cnt[min_num] -= c
            cnt[min_num+1] += c 
            if not cnt[min_num]:
                del cnt[min_num]
                min_num += 1
            k -= c
        return reduce(lambda total, x: total*pow(x[0], x[1], MOD)%MOD, cnt.iteritems(), 1)