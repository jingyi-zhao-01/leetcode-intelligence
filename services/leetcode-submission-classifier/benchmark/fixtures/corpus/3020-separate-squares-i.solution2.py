# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: separate-squares-i
# source_path: LeetCode-Solutions-master/Python/separate-squares-i.py
# solution_class: Solution2
# submission_id: e80ad7fae5aa68e545b8ee2db89489c57f672e51
# seed: 310838205

# Time:  O(nlogn)
# Space: O(n)

# sort, line sweep

class Solution2(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        EPS = 1e-5
        def binary_search(left, right, check):
            while right-left > EPS:
                mid = left+(right-left)/2.0
                if check(mid):
                    right = mid
                else:
                    left = mid
            return left
    
        def check(k):
            result = 0
            for x, y, l in squares:
                if y >= k:
                    result += l**2
                elif y+l <= k:
                    result -= l**2
                else:
                    result += l*(((y+l)-k)-(k-y))
            return result <= 0
    
        return binary_search(min(y for _, y, _ in squares), max(y+l for _, y, l in squares), check)