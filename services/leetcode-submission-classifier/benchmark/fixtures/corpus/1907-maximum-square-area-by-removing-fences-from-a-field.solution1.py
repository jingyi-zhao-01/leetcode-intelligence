# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-square-area-by-removing-fences-from-a-field
# source_path: LeetCode-Solutions-master/Python/maximum-square-area-by-removing-fences-from-a-field.py
# solution_class: Solution
# submission_id: 4f7f3151bccca0b30e6a8a6bb44339deda127bda
# seed: 713555541

# Time:  O(h^2 + v^2)
# Space: O(h^2 + v^2)

# hash table

class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        def diff(arr, x):
            arr.append(1)
            arr.append(x)
            return {abs(arr[i]-arr[j]) for i in xrange(len(arr)) for j in xrange(i+1, len(arr))}

        lookup = diff(hFences, m)
        result = -1
        for x in diff(vFences, n):
            if x in lookup:
                result = max(result, x**2)
        return result%MOD if result != -1 else -1