# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distribute-candies-among-children-i
# source_path: LeetCode-Solutions-master/Python/distribute-candies-among-children-i.py
# solution_class: Solution3
# submission_id: 99637439a5de2a9610e15248adeccdffc7f6a4ee
# seed: 2981989530

# Time:  O(1)
# Space: O(1)

# stars and bars, combinatorics, principle of inclusion-exclusion 

class Solution3(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        return sum(n-i-j <= limit for i in xrange(min(limit, n)+1) for j in xrange(min(limit, n-i)+1))