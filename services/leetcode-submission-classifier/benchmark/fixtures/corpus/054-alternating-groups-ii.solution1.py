# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: alternating-groups-ii
# source_path: LeetCode-Solutions-master/Python/alternating-groups-ii.py
# solution_class: Solution
# submission_id: fa3d1983497cca887b461abc269151fb3a154758
# seed: 3839293731

# Time:  O(n)
# Space: O(1)

# sliding window, two pointers

class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        result = curr = left = 0
        for right in xrange(len(colors)+k-1):  
            if right-left+1 == k:
                result += int(curr == k-1)
                curr -= int(colors[left] != colors[(left+1)%len(colors)])
                left += 1
            curr += int(colors[right%len(colors)] != colors[(right+1)%len(colors)])
        return result