# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: design-underground-system
# source_path: LeetCode-Solutions-master/Python/design-underground-system.py
# solution_class: Solution
# submission_id: 020811a7e23fa97efd9e0aabbfa92c36723d74b2
# seed: 3955293657

# Time:  ctor:       O(1)
#        checkin:    O(1)
#        checkout:   O(1)
#        getaverage: O(1)
# Space: O(n)

import collections


class UndergroundSystem(object):

    def __init__(self):
        self.__live = {}
        self.__statistics = collections.defaultdict(lambda: [0, 0])
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.__live[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation, startTime = self.__live.pop(id)
        self.__statistics[startStation, stationName][0] += t-startTime
        self.__statistics[startStation, stationName][1] += 1
        
    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        total_time, cnt = self.__statistics[startStation, endStation]
        return float(total_time) / cnt
