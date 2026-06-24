# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: watering-plants
# source_path: LeetCode-Solutions-master/Python/watering-plants.py
# solution_class: Solution
# submission_id: cb8ba0a8e888bc1b58a4c5f18e521cb1bc1861ab
# seed: 2107044931

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        result, can = len(plants), capacity
        for i, x in enumerate(plants):
            if can < x:
                result += 2*i
                can = capacity
            can -= x
        return result