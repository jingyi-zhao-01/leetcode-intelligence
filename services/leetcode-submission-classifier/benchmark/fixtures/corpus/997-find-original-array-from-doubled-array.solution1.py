# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-original-array-from-doubled-array
# source_path: LeetCode-Solutions-master/Python/find-original-array-from-doubled-array.py
# solution_class: Solution
# submission_id: bee28a1c80ad5cfccc22bc2690cd22237e502b3f
# seed: 399948641

# Time:  O(n + klogk), k is the distinct number of changed
# Space: O(k)

class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if len(changed)%2:
            return []
        cnts = collections.Counter(changed)
        for x in sorted(cnts.iterkeys()):
            if cnts[x] > cnts[2*x]:
                return []
            cnts[2*x] -= cnts[x] if x else cnts[x]//2
        return list(cnts.elements())