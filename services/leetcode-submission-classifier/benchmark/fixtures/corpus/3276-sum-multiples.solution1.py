# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-multiples
# source_path: LeetCode-Solutions-master/Python/sum-multiples.py
# solution_class: Solution
# submission_id: 1d2b87774bbe6d3888fda124b4abf8a057d09205
# seed: 2517119957

# Time:  O(1)
# Space: O(1)

# math, principle of inclusion and exclusion

class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(d):
            return d*((1+(n//d))*(n//d)//2)
        
        return (f(3)+f(5)+f(7))-(f(3*5)+f(5*7)+f(7*3))+f(3*5*7)