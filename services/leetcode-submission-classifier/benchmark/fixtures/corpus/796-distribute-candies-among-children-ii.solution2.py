# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distribute-candies-among-children-ii
# source_path: LeetCode-Solutions-master/Python/distribute-candies-among-children-ii.py
# solution_class: Solution2
# submission_id: f405737e12a38f8dc484c50335e6292b21156e1c
# seed: 1046471171

# Time:  O(1)
# Space: O(1)

# stars and bars, combinatorics, principle of inclusion-exclusion 

class Solution2(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        return sum(min(limit, n-i)-max((n-i)-limit, 0)+1 for i in xrange(max(n-2*limit, 0), min(limit, n)+1))