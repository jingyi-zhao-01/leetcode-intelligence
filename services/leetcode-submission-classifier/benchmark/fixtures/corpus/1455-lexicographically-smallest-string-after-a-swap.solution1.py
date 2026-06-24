# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-smallest-string-after-a-swap
# source_path: LeetCode-Solutions-master/Python/lexicographically-smallest-string-after-a-swap.py
# solution_class: Solution
# submission_id: 387a04e1f27eeccbfd5e7d77acfdfac4fd291e21
# seed: 281372374

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = map(int, s)
        for i in xrange(len(s)-1):
            if result[i]%2 != result[i+1]%2:
                continue
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
                break
        return "".join(map(str, result))