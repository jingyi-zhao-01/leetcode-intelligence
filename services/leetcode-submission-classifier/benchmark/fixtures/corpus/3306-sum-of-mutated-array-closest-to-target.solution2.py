# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-mutated-array-closest-to-target
# source_path: LeetCode-Solutions-master/Python/sum-of-mutated-array-closest-to-target.py
# solution_class: Solution2
# submission_id: 63465443236c2d9d0f39deacbbbbfb3c634c1aa0
# seed: 3276254084

# Time:  O(nlogn)
# Space: O(1)

class Solution2(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort(reverse=True)
        max_arr = arr[0]
        while arr and arr[-1]*len(arr) <= target:
            target -= arr.pop()
        if not arr:
            return max_arr
        x = (target-1)//len(arr)
        return x if target-x*len(arr) <= (x+1)*len(arr)-target else x+1