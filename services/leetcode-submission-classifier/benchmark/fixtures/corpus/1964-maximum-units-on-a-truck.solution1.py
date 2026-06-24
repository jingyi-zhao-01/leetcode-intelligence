# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-units-on-a-truck
# source_path: LeetCode-Solutions-master/Python/maximum-units-on-a-truck.py
# solution_class: Solution
# submission_id: f9e366746af6de7ee8fc3c5ab5e127c41213d75e
# seed: 16396848

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        result = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                result += box*units
            else:
                result += truckSize*units
                break
        return result