# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: building-boxes
# source_path: LeetCode-Solutions-master/Python/building-boxes.py
# solution_class: Solution
# submission_id: 19965c3907def66f234564072f64f3df18aaceaa
# seed: 682078609

# Time:  O(1)
# Space: O(1)

import math

class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # find max h s.t. sum(k*(k+1)//2 for k in xrange(1, h+1)) <= n
        # => find max h s.t. h*(h+1)*(h+2)//6 <= n
        h = int((6*n)**(1.0/3))  
        if h*(h+1)*(h+2) > 6*n:
            # (h-1)*h*(h+1) < h^3 <= 6n < h*(h+1)*(h+2) < (h+1)^3
            h -= 1
        n -= h*(h+1)*(h+2)//6
        d = int(math.ceil((-1+(1+8*n)**0.5)/2))  # find min d s.t. d*(d+1)//2 >= n
        return h*(h+1)//2 + d