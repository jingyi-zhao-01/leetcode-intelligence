# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: replace-elements-with-greatest-element-on-right-side
# source_path: LeetCode-Solutions-master/Python/replace-elements-with-greatest-element-on-right-side.py
# solution_class: Solution
# submission_id: 2b561c25f8771342e02f4b7fad81dcede3b5841d
# seed: 3101904456

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        curr_max = -1
        for i in reversed(xrange(len(arr))):
            arr[i], curr_max = curr_max, max(curr_max, arr[i])
        return arr