# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: frequency-balance-subarray
# source_path: LeetCode-Solutions-master/Python/frequency-balance-subarray.py
# solution_class: Solution2
# submission_id: 95ade1eca8ad815a1c877fd089d761c3347c075e
# seed: 1950991292

# Time:  O(n^2)
# Space: O(n)

# sort, coordinate compression, freq table

class Solution2(object):
    def getLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for left in xrange(len(nums)):
            cnt, cnt2 = collections.defaultdict(int), collections.defaultdict(int)
            distinct = total = c = 0
            for right in xrange(left, len(nums)):
                if cnt[nums[right]]:
                    cnt2[cnt[nums[right]]] -= 1
                    if cnt2[cnt[nums[right]]] == 0:
                        c -= 1
                        total -= cnt[nums[right]]
                cnt[nums[right]] += 1
                if cnt[nums[right]] == 1:
                    distinct += 1
                cnt2[cnt[nums[right]]] += 1
                if cnt2[cnt[nums[right]]] == 1:
                    total += cnt[nums[right]]
                    c += 1
                if distinct == 1 or (c == 2 and total%3 == 0 and cnt2[total//3]):
                    result = max(result, right-left+1)
        return result