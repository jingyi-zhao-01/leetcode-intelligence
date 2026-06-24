# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: add-binary
# source_path: LeetCode-Solutions-master/Python/add-binary.py
# solution_class: Solution2
# submission_id: 47d395630e5aa044c1e91efcbbc5b7075fa2f1c4
# seed: 1880148569

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = 0
        for x, y in izip_longest(reversed(a), reversed(b), fillvalue="0"):
            carry, remainder = divmod(int(x)+int(y)+carry, 2)
            result += str(remainder)
        
        if carry:
            result += str(carry)
        
        return result[::-1]