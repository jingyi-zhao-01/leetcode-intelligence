# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-common-subpath
# source_path: LeetCode-Solutions-master/Python/longest-common-subpath.py
# solution_class: Solution
# submission_id: 439c9a87ff65a9f276c96a4bb228f2e23ef6d382
# seed: 3052102143

# Time:  O(m * nlogn)
# Space: O(n)

class Solution(object):
    def longestCommonSubpath(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: int
        """
        def RabinKarp(arr, x):  # double hashing
            hashes = tuple([reduce(lambda h,x: (h*p+x)%MOD, (arr[i] for i in xrange(x)), 0) for p in P])
            powers = [pow(p, x, MOD) for p in P]
            lookup = {hashes}
            for i in xrange(x, len(arr)):
                hashes = tuple([(hashes[j]*P[j] - arr[i-x]*powers[j] + arr[i])%MOD for j in xrange(len(P))])  # in smaller datasets, tuple from list is much faster than tuple from generator, see https://stackoverflow.com/questions/16940293/why-is-there-no-tuple-comprehension-in-python
                lookup.add(hashes)
            return lookup
        
        def check(paths, x):
            intersect = RabinKarp(paths[0], x)
            for i in xrange(1, len(paths)):
                intersect = set.intersection(intersect, RabinKarp(paths[i], x))
                if not intersect:
                    return False
            return True

        MOD, P = 10**9+7, (113, 109)  # MOD could be the min prime of 7-digit number (10**6+3), P could be (2, 3)
        left, right = 1, min(len(p) for p in paths)
        while left <= right:
            mid = left + (right-left)//2
            if not check(paths, mid):
                right = mid-1
            else:
                left = mid+1
        return right