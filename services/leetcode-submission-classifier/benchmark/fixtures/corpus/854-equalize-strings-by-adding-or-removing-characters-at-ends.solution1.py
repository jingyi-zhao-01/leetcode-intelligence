# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: equalize-strings-by-adding-or-removing-characters-at-ends
# source_path: LeetCode-Solutions-master/Python/equalize-strings-by-adding-or-removing-characters-at-ends.py
# solution_class: Solution
# submission_id: 06b8084bff085e285c8f3f2b630d6c7675e46cc0
# seed: 2363983379

# Time:  O((n + m) * log(min(n, m)))
# Space: O(min(n, m))

# binary search, rolling hash

class Solution(object):
    def minOperations(self, initial, target):
        """
        :type initial: str
        :type target: str
        :rtype: int
        """
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if not check( mid):
                    right = mid-1
                else:
                    left = mid+1
            return right
        
        def rolling_hash(s, l, lookup, check):
            MOD, P = 10**9+7, 113
            h = 0
            pw = pow(P, l-1, MOD)
            for i in xrange(len(s)):
                h = (h*P+(ord(s[i])-ord('a')))%MOD
                if i < l-1:
                    continue
                if not check:
                    lookup.add(h)
                elif h in lookup:
                    return True
                h = (h-(ord(s[i-(l-1)])-ord('a'))*pw)%MOD
            return False
                    
        def check(l):
            lookup = set()
            rolling_hash(target, l, lookup, False)
            return rolling_hash(initial, l, lookup, True)

        if len(initial) < len(target):
            initial, target = target, initial
        return len(initial)+len(target)-2*binary_search_right(1, min(len(initial), min(target)), check)