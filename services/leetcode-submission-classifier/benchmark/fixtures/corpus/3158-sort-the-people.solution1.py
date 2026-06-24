# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-the-people
# source_path: LeetCode-Solutions-master/Python/sort-the-people.py
# solution_class: Solution
# submission_id: 4d24465f58796f0b5551da35acae893ff15e857c
# seed: 644042065

# Time:  O(nlogn)
# Space: O(n)

# sort

class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        order = range(len(names))
        order.sort(key=lambda x: heights[x], reverse=True)
        return [names[i] for i in order]