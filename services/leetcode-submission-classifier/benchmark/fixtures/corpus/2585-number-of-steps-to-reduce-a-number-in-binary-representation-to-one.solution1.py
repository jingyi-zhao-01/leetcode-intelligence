# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-steps-to-reduce-a-number-in-binary-representation-to-one
# source_path: LeetCode-Solutions-master/Python/number-of-steps-to-reduce-a-number-in-binary-representation-to-one.py
# solution_class: Solution
# submission_id: f379394c8becbb83762967681a0d5f8f961436f8
# seed: 2566599993

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, carry = 0, 0
        for i in reversed(xrange(1, len(s))):
            if int(s[i]) + carry == 1:
                carry = 1  # once it was set, it would keep carrying forever
                result += 2
            else:
                result += 1
        return result+carry