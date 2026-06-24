# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: design-ride-sharing-system
# source_path: LeetCode-Solutions-master/Python/design-ride-sharing-system.py
# solution_class: Solution
# submission_id: 39c7b25b643f786ec79e0624844ab79e1a87d306
# seed: 1139963916

# Time:  ctor:                 O(1)
#        addRider:             O(1)
#        addDriver:            O(1)
#        matchDriverWithRider: O(1)
#        cancelRider:          O(1)
# Space: O(n)

import collections


# ordered dict
class RideSharingSystem(object):

    def __init__(self):
        self.__riders = collections.OrderedDict()
        self.__drivers = collections.OrderedDict()
        

    def addRider(self, riderId):
        """
        :type riderId: int
        :rtype: None
        """
        self.__riders[riderId] = True
        

    def addDriver(self, driverId):
        """
        :type driverId: int
        :rtype: None
        """
        self.__drivers[driverId] = True
        

    def matchDriverWithRider(self):
        """
        :rtype: List[int]
        """
        if not self.__riders or not self.__drivers:
            return [-1, -1]
        r = next(iter(self.__riders))
        d = next(iter(self.__drivers))
        del self.__riders[r]
        del self.__drivers[d]
        return [d, r]
    

    def cancelRider(self, riderId):
        """
        :type riderId: int
        :rtype: None
        """
        if riderId in self.__riders:
            del self.__riders[riderId]
        
