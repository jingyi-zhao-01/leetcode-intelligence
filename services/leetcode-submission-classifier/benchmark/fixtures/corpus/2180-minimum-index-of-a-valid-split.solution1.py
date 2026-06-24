# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-index-of-a-valid-split
# source_path: LeetCode-Solutions-master/Python/minimum-index-of-a-valid-split.py
# solution_class: Solution
# submission_id: f5a74a1500ab9ffe08c8a0e41261dd8c77d2dcc9
# seed: 2177201780

# Time:  O(n)
# Space: O(1)

# Boyer–Moore majority vote algorithm, linear search

class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def boyer_moore_majority_vote():
            result, cnt = None, 0
            for x in nums:
                if not cnt:
                    result = x
                if x == result:
                    cnt += 1
                else:
                    cnt -= 1
            return result
        
        m = boyer_moore_majority_vote()
        total, cnt = nums.count(m), 0
        for i, x in enumerate(nums):
            if x == m:
                cnt += 1
            if cnt*2 > i+1 and (total-cnt)*2 > len(nums)-(i+1):
                return i
        return -1