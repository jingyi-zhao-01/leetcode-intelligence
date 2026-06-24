# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: strobogrammatic-number
# source_path: LeetCode-Solutions-master/Python/strobogrammatic-number.py
# solution_class: Solution
# submission_id: e1873feff4182f03de0d7258ebba20ee26525fe1
# seed: 55007307

# Time:  O(n)
# Space: O(1)

class Solution(object):
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    # @param {string} num
    # @return {boolean}
    def isStrobogrammatic(self, num):
        n = len(num)
        for i in xrange((n+1) / 2):
            if num[n-1-i] not in self.lookup or \
               num[i] != self.lookup[num[n-1-i]]:
                return False
        return True