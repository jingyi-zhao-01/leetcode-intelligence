# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-common-subpath
# source_path: LeetCode-Solutions-master/Python/longest-common-subpath.py
# solution_class: Solution2
# submission_id: 2e04bb8ad2d2e741fb03e11371d557cb1746fe50
# seed: 3110414920

# Time:  O(m * nlogn)
# Space: O(n)

class Solution2(object):
    def longestCommonSubpath(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: int
        """
        def RabinKarp(arr, x):
            h = reduce(lambda h,x: (h*P+x)%MOD, (arr[i] for i in xrange(x)), 0)
            power = pow(P, x, MOD)
            lookup = {h}
            for i in xrange(x, len(arr)):
                h = (h*P - arr[i-x]*power + arr[i])%MOD
                lookup.add(h)
            return lookup
        
        def check(paths, x):
            intersect = RabinKarp(paths[0], x)
            for i in xrange(1, len(paths)):
                intersect = set.intersection(intersect, RabinKarp(paths[i], x))
                if not intersect:
                    return False
            return True

        MOD, P = 10**11+19, max(x for p in paths for x in p)+1  # MOD is the min prime of 12-digit number
        left, right = 1, min(len(p) for p in paths)
        while left <= right:
            mid = left + (right-left)//2
            if not check(paths, mid):
                right = mid-1
            else:
                left = mid+1
        return right