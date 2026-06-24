# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: counting-elements
# source_path: LeetCode-Solutions-master/Python/counting-elements.py
# solution_class: Solution
# submission_id: d12fa57e0bab74b4356bd30b52b1043f7bad5505
# seed: 4124763701

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        result, l = 0, 1
        for i in xrange(len(arr)-1):
            if arr[i] == arr[i+1]:
                l += 1
                continue
            if arr[i]+1 == arr[i+1]:
                result += l
            l = 1
        return result