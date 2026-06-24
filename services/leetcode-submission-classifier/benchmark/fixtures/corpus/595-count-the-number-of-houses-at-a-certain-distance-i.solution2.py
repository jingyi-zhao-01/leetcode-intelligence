# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-houses-at-a-certain-distance-i
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-houses-at-a-certain-distance-i.py
# solution_class: Solution2
# submission_id: df664cea4c5b4fcef04330f364e7d8f17ca2a39d
# seed: 4036307411

# Time:  O(n)
# Space: O(1)

# math, prefix sum, difference array

class Solution2(object):
    def countOfPairs(self, n, x, y):
        """
        :type n: int
        :type x: int
        :type y: int
        :rtype: List[int]
        """
        x, y = x-1, y-1
        result = [0]*n
        for i in xrange(n):
            for j in xrange(i+1, n):
                result[min(abs(i-j), abs(i-x)+1+abs(y-j), abs(i-y)+1+abs(x-j))-1] += 2
        return result