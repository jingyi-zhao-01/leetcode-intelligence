# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-adjacent-elements-with-the-same-color
# source_path: LeetCode-Solutions-master/Python/number-of-adjacent-elements-with-the-same-color.py
# solution_class: Solution
# submission_id: b3b3c6bfe68c5498924a544915135d9655032994
# seed: 2651829801

# Time:  O(n + q)
# Space: O(n)

# array

class Solution(object):
    def colorTheArray(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def update(i):
            if not nums[i]:
                return 0
            cnt = 0
            if i-1 >= 0 and nums[i-1] == nums[i]:
                cnt += 1
            if i+1 < n and nums[i+1] == nums[i]:
                cnt += 1
            return cnt

        nums = [0]*n
        result = [0]*len(queries)
        curr = 0
        for idx, (i, c) in enumerate(queries):
            curr -= update(i)
            nums[i] = c
            curr += update(i)
            result[idx] = curr
        return result