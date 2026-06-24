# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-garden-perimeter-to-collect-enough-apples
# source_path: LeetCode-Solutions-master/Python/minimum-garden-perimeter-to-collect-enough-apples.py
# solution_class: Solution3
# submission_id: b9b854d4b50ffbe8742fa8b2e5f90a25ccee989a
# seed: 2561246913

# Time:  O(1)
# Space: O(1)

import math

class Solution3(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        # 2r  , 2r-1, ..., r+1, r  , r+1, ..., 2*r-1, 2*r
        # 2r-1,                 r-1,                  2r-1
        # .                     .                     .    
        # .                     .                     .    
        # .                     .                     .    
        # r+1 ,    r, ...,   2, 1  ,   2, ...,   r  , r+1
        # r   ,  r-1, ...,   1, 0  ,   1, ...,   r-1, r
        # r+1 ,    r, ...,   2, 1  ,   2, ...,   r  , r+1
        # .                     .                     .    
        # .                     .                     .    
        # .                     .                     .    
        # 2r-1,                 r-1,                  2r-1
        # 2r  , 2r-1, ..., r+1, r  , r+1, ..., 2*r-1, 2*r
        #
        # the sum of each row/col forms an arithmetic sequence
        # => let ai = (((r + (r-1) + ... + r + 0) + (0 + 1 + 2 + ... + r)) - 0) + i*(2r+1)
        #           = (2*(0+r)*(r+1)/2-0) + i*(2r+1)
        #           = r*(r+1) + i*(2r+1)
        # => total  = 2*(a0 + a1 + ... ar) - a0
        #           = 2*(r*(r+1) + r*(r+1) + r*(2r+1)))*(r+1)/2 - r*(r+1)
        #           = r*(4r+3)*(r+1)-r*(r+1)
        #           = 4r^3+6r^2+2r
        # => find min r, s.t. 4r^3+6r^2+2r >= neededApples

        def check(neededApples, x):
            return r*(2*r+1)*(2*r+2) >= neededApples

        left, right = 1, int((neededApples/4.0)**(1.0/3))
        while left <= right:
            mid = left + (right-left)//2
            if check(neededApples, mid):
                right = mid-1
            else:
                left = mid+1
        return 8*left