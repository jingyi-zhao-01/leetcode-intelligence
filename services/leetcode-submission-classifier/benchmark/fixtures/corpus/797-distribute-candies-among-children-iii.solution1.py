# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distribute-candies-among-children-iii
# source_path: LeetCode-Solutions-master/Python/distribute-candies-among-children-iii.py
# solution_class: Solution
# submission_id: 989d7f2dcb9f3eaf87cb7361adeff0ac66417a4e
# seed: 3115804408

# Time:  O(1)
# Space: O(1)

# stars and bars, combinatorics, principle of inclusion and exclusion

class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        def nCr(n, r):  # Time: O(n), Space: O(1)
            if not 0 <= r <= n:
                return 0
            if n-r < r:
                r = n-r
            c = 1
            for k in xrange(1, r+1):
                c *= n-k+1
                c //= k
            return c
        
        def nHr(n, r):
            return nCr(n+(r-1), r-1)
    
        R = 3
        return sum((-1 if r%2 else 1) * nCr(R, r) * nHr(n-r*(limit+1), R) for r in xrange(R+1))