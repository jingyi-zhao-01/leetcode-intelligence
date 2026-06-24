# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotated-digits
# source_path: LeetCode-Solutions-master/Python/rotated-digits.py
# solution_class: Solution3
# submission_id: 131f40d16a35feb12fba33c9286bc431a58ec973
# seed: 2172355117

# Time:  O(logn)
# Space: O(logn)

class Solution3(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        invalid, diff = set(['3', '4', '7']), set(['2', '5', '6', '9'])
        result = 0
        for i in xrange(N+1):
            lookup = set(list(str(i)))
            if invalid & lookup:
                continue
            if diff & lookup:
                result += 1
        return result