# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-string-prefix
# source_path: LeetCode-Solutions-master/Python/reverse-string-prefix.py
# solution_class: Solution
# submission_id: f62c3f683c934588c44b67b7a41f176125551876
# seed: 1805366400

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def reverse(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -=1
            return arr

        return "".join(reverse(list(s), 0, k-1))