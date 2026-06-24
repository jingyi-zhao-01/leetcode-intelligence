# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-points-in-an-archery-competition
# source_path: LeetCode-Solutions-master/Python/maximum-points-in-an-archery-competition.py
# solution_class: Solution
# submission_id: c54b9b0c7eafd9415d62f7ea9743e4f3f1de9c27
# seed: 2936514608

# Time:  O(n * 2^n)
# Space: O(n)

# bitmasks

class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        """
        :type numArrows: int
        :type aliceArrows: List[int]
        :rtype: List[int]
        """
        def check(mask, numArrows):
            score = 0
            cnt = [0]*len(aliceArrows)
            i, base = 0, 1
            for k, a in enumerate(aliceArrows):
                if mask&1:
                    need = a+1
                    if need > numArrows:
                        return 0, [0]*len(aliceArrows)
                    numArrows -= need
                    cnt[k] = need
                    score += k
                mask >>= 1
            cnt[-1] += numArrows
            return score, cnt
        
        result = [0]*len(aliceArrows)
        best = 0
        for mask in xrange(1, 2**len(aliceArrows)):
            score, cnt = check(mask, numArrows)
            if score > best:
                best = score
                result = cnt
        return result