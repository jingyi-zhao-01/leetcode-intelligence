# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: strobogrammatic-number-ii
# source_path: LeetCode-Solutions-master/Python/strobogrammatic-number-ii.py
# solution_class: Solution
# submission_id: dfad6a91cdcfbf624b8054a8b6226bea3e43cb6a
# seed: 3523529574

# Time:  O(n * 5^(n/2))
# Space: O(n)

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        result = ['0', '1', '8'] if n%2 else ['']
        for i in xrange(n%2, n, 2):
            result = [a + num + b for a, b in lookup.iteritems() if i != n-2 or a != '0' for num in result]
        return result