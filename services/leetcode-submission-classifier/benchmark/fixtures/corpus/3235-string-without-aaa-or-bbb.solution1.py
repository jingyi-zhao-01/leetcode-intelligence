# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: string-without-aaa-or-bbb
# source_path: LeetCode-Solutions-master/Python/string-without-aaa-or-bbb.py
# solution_class: Solution
# submission_id: 855789d4fe7faefcaeba3fe25b025730f20d65ab
# seed: 3896741866

# Time:  O(a + b)
# Space: O(1)

class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        result = []
        put_A = None
        while A or B:
            if len(result) >= 2 and result[-1] == result[-2]:
                put_A = result[-1] == 'b'
            else:
                put_A = A >= B

            if put_A:
                A -= 1
                result.append('a')
            else:
                B -= 1
                result.append('b')
        return "".join(result)