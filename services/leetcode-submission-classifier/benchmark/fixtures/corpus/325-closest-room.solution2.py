# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-room
# source_path: LeetCode-Solutions-master/Python/closest-room.py
# solution_class: Solution2
# submission_id: b63e9b1d79e23250013b11262b75fb063c2942bc
# seed: 998777268

# Time:  O(nlogn + klogk + klogn)
# Space: O(n + k)

from sortedcontainers import SortedList

class Solution2(object):
    def closestRoom(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def find_closest(ids, r):
            result, min_dist = -1, float("inf")
            i = ids.bisect_right(r)
            if i-1 >= 0 and abs(ids[i-1]-r) < min_dist:
                min_dist = abs(ids[i-1]-r)
                result = ids[i-1]
            if i < len(ids) and abs(ids[i]-r) < min_dist:
                min_dist = abs(ids[i]-r)
                result = ids[i]
            return result

        rooms.sort(key=lambda x: x[1])
        for i, q in enumerate(queries):
            q.append(i)
        queries.sort(key=lambda x: x[1])
        ids = SortedList(i for i, _ in rooms)        
        i = 0
        result = [-1]*len(queries)
        for r, s, idx in queries:
            while i < len(rooms) and rooms[i][1] < s:
                ids.remove(rooms[i][0])
                i += 1
            result[idx] = find_closest(ids, r)
        return result