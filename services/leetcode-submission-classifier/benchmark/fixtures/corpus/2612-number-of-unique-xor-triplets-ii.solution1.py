# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-unique-xor-triplets-ii
# source_path: LeetCode-Solutions-master/Python/number-of-unique-xor-triplets-ii.py
# solution_class: Solution
# submission_id: 2c552e7d63dbca41d2c789f9cbe9044dc9c6276a
# seed: 1709584968

# Time:  O(nlogn)
# Space: O(n)

# FWHT, fst

class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Template: https://github.com/kth-competitive-programming/kactl/blob/main/content/numerical/FastSubsetTransform.h
        def fst(a, inverse):
            n = len(a)
            step = 1
            while step < n:
                for i in xrange(0, n, step<<1):
                    for j in xrange(i, i+step):
                        u, v = a[j], a[j+step]
                        a[j], a[j+step] = u+v, u-v
                step <<= 1
            if inverse:
                for i in xrange(n):
                    a[i] //= n
        
        a = [0]*(1<<max(nums).bit_length())
        for x in nums:
            a[x] += 1
        fst(a, False)
        for i in xrange(len(a)):
            a[i] = a[i]**3
        fst(a, True)
        return sum(x != 0 for x in a)