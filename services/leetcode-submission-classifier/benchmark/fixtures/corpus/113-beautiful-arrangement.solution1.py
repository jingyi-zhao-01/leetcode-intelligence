# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: beautiful-arrangement
# source_path: LeetCode-Solutions-master/Python/beautiful-arrangement.py
# solution_class: Solution
# submission_id: 846bae2356cf7c58e112450aefee08cee0c9e96b
# seed: 22894816

# Time:  O(n!)
# Space: O(n)

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def countArrangementHelper(n, arr):
            if n <= 0:
                return 1
            count = 0
            for i in xrange(n):
                if arr[i] % n == 0 or n % arr[i] == 0:
                    arr[i], arr[n-1] = arr[n-1], arr[i]
                    count += countArrangementHelper(n - 1, arr)
                    arr[i], arr[n-1] = arr[n-1], arr[i]
            return count

        return countArrangementHelper(N, range(1, N+1))