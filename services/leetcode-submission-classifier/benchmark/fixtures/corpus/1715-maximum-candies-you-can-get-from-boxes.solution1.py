# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-candies-you-can-get-from-boxes
# source_path: LeetCode-Solutions-master/Python/maximum-candies-you-can-get-from-boxes.py
# solution_class: Solution
# submission_id: b4b70962e8b4eb3c3cf2413d8f0d84d1db01013f
# seed: 445689741

# Time:  O(n^2)
# Space: O(n)

import collections

class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        result = 0
        q = collections.deque(initialBoxes)
        while q:
            changed = False
            for _ in xrange(len(q)):
                box = q.popleft()
                if not status[box]:
                    q.append(box)
                    continue
                changed = True
                result += candies[box]
                for contained_key in keys[box]:
                    status[contained_key] = 1
                for contained_box in containedBoxes[box]:
                    q.append(contained_box)
            if not changed:
                break
        return result