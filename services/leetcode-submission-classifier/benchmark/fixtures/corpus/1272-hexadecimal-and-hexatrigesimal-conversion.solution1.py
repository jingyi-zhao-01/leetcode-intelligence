# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: hexadecimal-and-hexatrigesimal-conversion
# source_path: LeetCode-Solutions-master/Python/hexadecimal-and-hexatrigesimal-conversion.py
# solution_class: Solution
# submission_id: 4eb649dda98843d831142ff1fa3c992da4a4ad7d
# seed: 2858300318

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def concatHex36(self, n):
        """
        :type n: int
        :rtype: str
        """
        LOOKUP = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        def convert(n, l):
            result = []
            while n:
                n, r = divmod(n, l)
                result.append(LOOKUP[r])
            result.reverse()
            return "".join(result)
        
        return convert(n**2, 16)+convert(n**3, 36)