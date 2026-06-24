# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-arithmetic-triplets
# source_path: LeetCode-Solutions-master/Python/number-of-arithmetic-triplets.py
# solution_class: Solution2
# submission_id: 761583923854544782347a4dfa47768c0e376389
# seed: 2646635049

# Time:  O(n)
# Space: O(n)

# hash table

class Solution2(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        result = 0
        cnt1 = collections.Counter()
        cnt2 = collections.Counter()
        for x in nums:
            result += cnt2[x-diff]
            cnt2[x] += cnt1[x-diff]
            cnt1[x] += 1
        return result