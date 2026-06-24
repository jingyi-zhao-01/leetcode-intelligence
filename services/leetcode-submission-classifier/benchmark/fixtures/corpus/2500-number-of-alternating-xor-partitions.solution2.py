# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-alternating-xor-partitions
# source_path: LeetCode-Solutions-master/Python/number-of-alternating-xor-partitions.py
# solution_class: Solution2
# submission_id: 1a4e29cd05d8e2d13fb90c23c73a9c1b8f95a4d7
# seed: 3128011013

# Time:  O(n)
# Space: O(1)

# dp

class Solution2(object):
    def alternatingXOR(self, nums, target1, target2):
        """
        :type nums: List[int]
        :type target1: int
        :type target2: int
        :rtype: int
        """
        MOD = 10**9+7
        cnt1 = collections.defaultdict(int)
        cnt2 = collections.defaultdict(int)
        cnt2[0] = 1
        result = prefix = 0
        for x in nums:
            prefix ^= x
            c1 = cnt2[prefix^target1]
            c2 = cnt1[prefix^target2]
            cnt1[prefix] = (cnt1[prefix]+c1)%MOD
            cnt2[prefix] = (cnt2[prefix]+c2)%MOD
        return (c1+c2)%MOD