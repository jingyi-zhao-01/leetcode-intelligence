# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: four-divisors
# source_path: LeetCode-Solutions-master/Python/four-divisors.py
# solution_class: Solution
# submission_id: a34202bfd8de4b1e1da18010a1833faa9b33eb04
# seed: 2039202917

# Time:  O(n * sqrt(n))
# Space: O(1)

class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            facs, i = [], 1
            while i*i <= num:
                if num % i:
                    i+= 1
                    continue
                facs.append(i)
                if i != num//i:
                    facs.append(num//i)
                    if len(facs) > 4:
                        break
                i += 1
            if len(facs) == 4:            
                result += sum(facs)
        return result 