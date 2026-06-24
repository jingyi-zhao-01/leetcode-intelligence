# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: plus-one
# source_path: LeetCode-Solutions-master/Python/plus-one.py
# solution_class: Solution2
# submission_id: 8e6ee700f98eb7ac4b5546cd891a206e1125f805
# seed: 3507127995

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = digits[::-1]
        carry = 1
        for i in xrange(len(result)):
            result[i] += carry
            carry, result[i] = divmod(result[i], 10)
        if carry:
            result.append(carry)
        return result[::-1]