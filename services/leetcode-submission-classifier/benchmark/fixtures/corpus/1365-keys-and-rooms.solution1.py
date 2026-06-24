# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: keys-and-rooms
# source_path: LeetCode-Solutions-master/Python/keys-and-rooms.py
# solution_class: Solution
# submission_id: 292dc5589645bcba2e896ce58da6a26747007e12
# seed: 1823981087

# Time:  O(n!)
# Space: O(n)

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        lookup = set([0])
        stack = [0]
        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                if nei not in lookup:
                    lookup.add(nei)
                    if len(lookup) == len(rooms):
                        return True
                    stack.append(nei)
        return len(lookup) == len(rooms)