# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: design-a-file-sharing-system
# source_path: LeetCode-Solutions-master/Python/design-a-file-sharing-system.py
# solution_class: Solution
# submission_id: a0b1525c6d9b870087b3485a44b80141c555c98d
# seed: 4131627505

# Time:  ctor:    O(1)
#        join:    O(logu + c), u is the number of total joined users
#        leave:   O(logu + c), c is the number of chunks
#        request: O(u)
# Space: O(u * c)

import heapq


# "u ~= n" solution, n is the average number of users who own the chunk
class FileSharing(object):

    def __init__(self, m):
        """
        :type m: int
        """
        self.__users = []
        self.__lookup = set()
        self.__min_heap = []

    def join(self, ownedChunks):
        """
        :type ownedChunks: List[int]
        :rtype: int
        """
        if self.__min_heap:
            userID = heapq.heappop(self.__min_heap)
        else:
            userID = len(self.__users)+1
            self.__users.append(set())
        self.__users[userID-1] = set(ownedChunks)
        self.__lookup.add(userID)
        return userID

    def leave(self, userID):
        """
        :type userID: int
        :rtype: None
        """
        if userID not in self.__lookup:
            return
        self.__lookup.remove(userID)
        self.__users[userID-1] = []
        heapq.heappush(self.__min_heap, userID)

    def request(self, userID, chunkID):
        """
        :type userID: int
        :type chunkID: int
        :rtype: List[int]
        """
        result = []
        for u, chunks in enumerate(self.__users, 1):
            if chunkID not in chunks:
                continue
            result.append(u)
        if not result:
            return
        self.__users[userID-1].add(chunkID)
        return result


# Time:  ctor:    O(1)
#        join:    O(logu + c), u is the number of total joined users
#        leave:   O(logu + c), c is the number of chunks
#        request: O(nlogn)   , n is the average number of users who own the chunk
# Space: O(u * c + m), m is the total number of unique chunks
import collections
import heapq


# "u >> n" solution
class FileSharing2(object):

    def __init__(self, m):
        """
        :type m: int
        """
        self.__users = []
        self.__lookup = set() 
        self.__chunks = collections.defaultdict(set)
        self.__min_heap = []

    def join(self, ownedChunks):
        """
        :type ownedChunks: List[int]
        :rtype: int
        """
        if self.__min_heap:
            userID = heapq.heappop(self.__min_heap)
        else:
            userID = len(self.__users)+1
            self.__users.append(set())
        self.__users[userID-1] = set(ownedChunks)
        self.__lookup.add(userID)
        for c in ownedChunks:
            self.__chunks[c].add(userID)
        return userID

    def leave(self, userID):
        """
        :type userID: int
        :rtype: None
        """
        if userID not in self.__lookup:
            return
        for c in self.__users[userID-1]:
            self.__chunks[c].remove(userID)
        self.__lookup.remove(userID)
        self.__users[userID-1] = []
        heapq.heappush(self.__min_heap, userID)

    def request(self, userID, chunkID):
        """
        :type userID: int
        :type chunkID: int
        :rtype: List[int]
        """
        result = sorted(self.__chunks[chunkID])
        if not result:
            return
        self.__users[userID-1].add(chunkID)
        self.__chunks[chunkID].add(userID)
        return result
