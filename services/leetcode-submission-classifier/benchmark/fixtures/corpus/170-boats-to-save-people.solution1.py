# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: boats-to-save-people
# source_path: LeetCode-Solutions-master/Python/boats-to-save-people.py
# solution_class: Solution
# submission_id: 6f398457f05abcac1760c9a89caeb6534d2c4ed8
# seed: 635035814

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        result = 0
        left, right = 0, len(people)-1
        while left <= right:
            result += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
        return result