# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: watering-plants-ii
# source_path: LeetCode-Solutions-master/Python/watering-plants-ii.py
# solution_class: Solution
# submission_id: dfe00b4113e228cc61933349ac0dfdad5c16b27b
# seed: 1803552043

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        result = 0 
        left, right = 0, len(plants)-1
        canA, canB = capacityA, capacityB
        while left < right: 
            if canA < plants[left]:
                result += 1
                canA = capacityA
            canA -= plants[left]
            if canB < plants[right]:
                result += 1
                canB = capacityB
            canB -= plants[right]
            left, right = left+1, right-1
        if left == right:
            if max(canA, canB) < plants[left]:
                result += 1
        return result