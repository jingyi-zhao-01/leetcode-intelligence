# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: taking-maximum-energy-from-the-mystic-dungeon
# source_path: LeetCode-Solutions-master/Python/taking-maximum-energy-from-the-mystic-dungeon.py
# solution_class: Solution
# submission_id: f5572c6de9da3cc5fdcfee559c9ca2ce78efe9b2
# seed: 1189815084

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        result = float("-inf")
        for i in xrange(k):
            curr = 0
            for j in reversed(xrange(((len(energy)-i)-1)%k, len(energy)-i, k)):  # xrange(len(energy)-1-i, -1, -k)
                curr += energy[j]
                result = max(result, curr)
        return result