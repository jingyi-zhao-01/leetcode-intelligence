# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: alternating-groups-i
# source_path: LeetCode-Solutions-master/Python/alternating-groups-i.py
# solution_class: Solution2
# submission_id: 6cfa608fba04ba1abd4026e1afdc83a83114a198
# seed: 3769395390

# Time:  O(n)
# Space: O(1)

# sliding window, two pointers

class Solution2(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        return sum(colors[i] != colors[(i+1)%len(colors)] != colors[(i+2)%len(colors)] for i in xrange(len(colors)))