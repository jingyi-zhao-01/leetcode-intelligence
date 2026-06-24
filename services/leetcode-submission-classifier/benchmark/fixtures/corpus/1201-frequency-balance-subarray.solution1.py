# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: frequency-balance-subarray
# source_path: LeetCode-Solutions-master/Python/frequency-balance-subarray.py
# solution_class: Solution
# submission_id: 0b72e98c980d9bb6b1e0635c053e7d44faf1a0db
# seed: 2986194124

# Time:  O(n^2)
# Space: O(n)

# sort, coordinate compression, freq table

class Solution(object):
    def getLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val_to_idx = {x:i for i, x in enumerate(sorted(set(nums)))}
        arr = [val_to_idx[x] for x in nums]
        result = 0
        for left in xrange(len(arr)):
            cnt, cnt2 = [0]*len(arr), [0]*(len(arr)+1)
            distinct = total = c = 0
            for right in xrange(left, len(arr)):
                if cnt[arr[right]]:
                    cnt2[cnt[arr[right]]] -= 1
                    if cnt2[cnt[arr[right]]] == 0:
                        c -= 1
                        total -= cnt[arr[right]]
                cnt[arr[right]] += 1
                if cnt[arr[right]] == 1:
                    distinct += 1
                cnt2[cnt[arr[right]]] += 1
                if cnt2[cnt[arr[right]]] == 1:
                    total += cnt[arr[right]]
                    c += 1
                if distinct == 1 or (c == 2 and total%3 == 0 and cnt2[total//3]):
                    result = max(result, right-left+1)
        return result