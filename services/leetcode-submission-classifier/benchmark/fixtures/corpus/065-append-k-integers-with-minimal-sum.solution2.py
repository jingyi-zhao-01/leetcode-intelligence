# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: append-k-integers-with-minimal-sum
# source_path: LeetCode-Solutions-master/Python/append-k-integers-with-minimal-sum.py
# solution_class: Solution2
# submission_id: cf40af8216362fbf00d6ab7119a0cd9af0a7aaf7
# seed: 276246051

# Time:  O(nlogn)
# Space: O(n)

# greedy

class Solution2(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = prev = 0
        nums.append(float("inf"))
        for x in sorted(set(nums)):
            if not k:
                break
            cnt = min((x-1)-prev, k)
            k -= cnt
            result += ((prev+1)+(prev+cnt))*cnt//2
            prev = x
        return result