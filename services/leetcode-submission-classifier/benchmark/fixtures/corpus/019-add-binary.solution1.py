# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: add-binary
# source_path: LeetCode-Solutions-master/Python/add-binary.py
# solution_class: Solution
# submission_id: 6423963a9c5dca487013ec31d963df34fee9e0a0
# seed: 2332757332

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result, carry, val = "", 0, 0
        for i in xrange(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = divmod(val, 2)
            result += str(val)
        if carry:
            result += str(carry)
        return result[::-1]