# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: alternating-groups-i
# source_path: LeetCode-Solutions-master/Python/alternating-groups-i.py
# solution_class: Solution
# submission_id: dd0b23401528d3c5d2ab648595895c971698bfef
# seed: 2976596780

# Time:  O(n)
# Space: O(1)

# sliding window, two pointers

class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        k = 3
        result = curr = left = 0
        for right in xrange(len(colors)+k-1):  
            if right-left+1 == k:
                result += int(curr == k-1)
                curr -= int(colors[left] != colors[(left+1)%len(colors)])
                left += 1
            curr += int(colors[right%len(colors)] != colors[(right+1)%len(colors)])
        return result