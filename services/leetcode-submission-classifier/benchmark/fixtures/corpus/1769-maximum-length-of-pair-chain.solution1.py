# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-length-of-pair-chain
# source_path: LeetCode-Solutions-master/Python/maximum-length-of-pair-chain.py
# solution_class: Solution
# submission_id: 8bbcc24a9893291a51ca564d547e84fbad4d119a
# seed: 3623051003

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        cnt, i = 0, 0
        for j in xrange(len(pairs)):
            if j == 0 or pairs[i][1] < pairs[j][0]:
                cnt += 1
                i = j
        return cnt