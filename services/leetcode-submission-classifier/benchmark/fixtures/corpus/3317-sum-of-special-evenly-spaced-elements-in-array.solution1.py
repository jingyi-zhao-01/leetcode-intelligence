# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-special-evenly-spaced-elements-in-array
# source_path: LeetCode-Solutions-master/Python/sum-of-special-evenly-spaced-elements-in-array.py
# solution_class: Solution
# submission_id: 52e595b6d8a040cfa7f9593b7daf5ab937dc086a
# seed: 2847360912

# Time:  O(n * sqrt(n))
# Space: O(n * sqrt(n))

class Solution(object):
    def solve(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9+7

        prefix = {}          
        result = []
        for x, y in queries:
            if y*y > len(nums):
                total = 0
                for i in xrange(x, len(nums), y):
                    total += nums[i]
                    total %= MOD
                result.append(total)
            else:
                begin = x%y
                if (begin, y) not in prefix:
                    prefix[(begin, y)] = [0]
                    for i in xrange(begin, len(nums), y):
                        prefix[(begin, y)].append((prefix[(begin, y)][-1] + nums[i]) % MOD)
                result.append((prefix[(begin, y)][-1]-prefix[(begin, y)][x//y]) % MOD)
        return result