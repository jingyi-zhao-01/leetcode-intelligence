# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-k-strongest-values-in-an-array
# source_path: LeetCode-Solutions-master/Python/the-k-strongest-values-in-an-array.py
# solution_class: Solution2
# submission_id: d167445c5d8cd67dec4e71c367c85b130bb73007
# seed: 2622716474

# Time:  O(nlogn)
# Space: O(1)

class Solution2(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        m = arr[(len(arr)-1)//2]
        arr.sort(key=lambda x: (-abs(x-m), -x))
        return arr[:k]