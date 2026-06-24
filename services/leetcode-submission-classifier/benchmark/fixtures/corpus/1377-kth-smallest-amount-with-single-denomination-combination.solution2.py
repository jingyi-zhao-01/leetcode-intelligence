# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kth-smallest-amount-with-single-denomination-combination
# source_path: LeetCode-Solutions-master/Python/kth-smallest-amount-with-single-denomination-combination.py
# solution_class: Solution2
# submission_id: 5906f925657f558b744ffdd8576f788ce181d2c3
# seed: 624953165

# Time:  O(n * 2^n * (log(mx) + log(k * mn))) = O(n * 2^n * logk), mn = min(coins), mx = max(coins)
# Space: O(2^n)

import itertools


# binary search, principle of inclusion and exclusion, number theory

class Solution2(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        def popcount(x):
            return bin(x).count('1')

        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        
        def lcm(a, b):
            return a//gcd(a, b)*b
    
        def check(target):
            return sum((-1 if (i+1)&1 else +1)*(target//l) for i in xrange(1, len(coins)+1) for l in lookup[i]) >= k

        def binary_search(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left
    
        lookup = [[] for _ in xrange(len(coins)+1)]
        for mask in xrange(1, 1<<len(coins)):
            lookup[popcount(mask)].append(reduce(lcm, (coins[i] for i in xrange(len(coins)) if mask&(1<<i))))
        mn = min(coins)
        return binary_search(mn, k*mn, check)