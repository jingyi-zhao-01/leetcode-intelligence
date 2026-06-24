# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kth-smallest-instructions
# source_path: LeetCode-Solutions-master/Python/kth-smallest-instructions.py
# solution_class: Solution
# submission_id: 4c0587e4a850b06a95fd95229f93478f699ce00b
# seed: 3753769082

# Time:  O((m + n)^2)
# Space: O(1)

class Solution(object):
    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        def nCr(n, r):  # Time: O(n), Space: O(1)
            if n < r:
                return 0
            if n-r < r:
                return nCr(n, n-r)
            c = 1
            for k in xrange(1, r+1):
                c *= n-k+1
                c //= k
            return c

        r, c = destination        
        result = []
        while r+c:
            count = nCr(r+(c-1), r)  # the number of HX..X combinations
            if k <= count:  # the kth instruction is one of HX..X combinations, so go right
                c -= 1
                result.append('H')
            else:  # the kth instruction is one of VX..X combinations, so go down
                k -= count  # the kth one of XX..X combinations is the (k-count)th one of VX..X combinations
                r -= 1
                result.append('V')
        return "".join(result)