# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-partition-a-binary-string
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-partition-a-binary-string.py
# solution_class: Solution
# submission_id: 6994b524405071b8871b3e244ff4532d59f946cd
# seed: 2130864616

# Time:  O(n)
# Space: O(n)

# prefix sum, divide and conquer

class Solution(object):
    def minCost(self, s, encCost, flatCost):
        """
        :type s: str
        :type encCost: int
        :type flatCost: int
        :rtype: int
        """
        def divide_and_conquer(left, right):
            l = right-left+1
            x = prefix[right+1]-prefix[left]
            result = l*x*encCost if x else flatCost
            if x and l%2 == 0:
                result = min(result, divide_and_conquer(left, (left+l//2)-1)+divide_and_conquer(left+l//2, right))
            return result
    
        prefix = [0]*(len(s)+1)
        for i in xrange(len(s)):
            prefix[i+1] = prefix[i]+(1 if s[i] == '1' else 0)
        return divide_and_conquer(0, len(s)-1)