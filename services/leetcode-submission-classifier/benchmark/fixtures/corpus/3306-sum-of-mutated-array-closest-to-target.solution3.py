# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-mutated-array-closest-to-target
# source_path: LeetCode-Solutions-master/Python/sum-of-mutated-array-closest-to-target.py
# solution_class: Solution3
# submission_id: 98b9d5ba19305e6270819a55b8beb0a171b5f4da
# seed: 749342008

# Time:  O(nlogn)
# Space: O(1)

class Solution3(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        def total(arr, v):
            result = 0
            for x in arr:
                result += min(v, x)
            return result

        def check(arr, v, target):
            return total(arr, v) >= target
        
        left, right = 1, max(arr)
        while left <= right:
            mid = left + (right-left)//2
            if check(arr, mid, target):
                right = mid-1
            else:
                left = mid+1
        return left-1 if target-total(arr, left-1) <= total(arr, left)-target else left