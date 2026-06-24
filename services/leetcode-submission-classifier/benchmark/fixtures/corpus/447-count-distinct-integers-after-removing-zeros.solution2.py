# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-distinct-integers-after-removing-zeros
# source_path: LeetCode-Solutions-master/Python/count-distinct-integers-after-removing-zeros.py
# solution_class: Solution2
# submission_id: 43fc77511601c832342d26ac3a07250a24337043
# seed: 2034022017

# Time:  O(logn)
# Space: O(1)

# combinatorics

class Solution2(object):
    def countDistinct(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        base = pow(9, len(s))
        result = (base-9)//(9-1)
        base //= 9
        for x in s:
            if x == '0':
                break
            result += ((ord(x)-ord('0'))-1)*base
            base //= 9
        if base == 0:
            result += 1
        return result