# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: replace-non-coprime-numbers-in-array
# source_path: LeetCode-Solutions-master/Python/replace-non-coprime-numbers-in-array.py
# solution_class: Solution
# submission_id: c82a10072eccf0f1311d8bbb1faf6c028c963836
# seed: 2633050917

# Time:  O(nlogm), m is the max of nums
# Space: O(1)

# math, stack

class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def gcd(a, b):  # Time: O(log(min(a, b)))
            while b:
                a, b = b, a%b
            return a

        result = []
        for x in nums:
            while True:
                g = gcd(result[-1] if result else 1, x)
                if g == 1:
                    break
                x *= result.pop()//g
            result.append(x)
        return result