# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: design-log-storage-system
# source_path: LeetCode-Solutions-master/Python/design-log-storage-system.py
# solution_class: Solution
# submission_id: 32f7fe3549949de7d04af4b20a8ff512d13e4598
# seed: 4091598542

# Time:  put:      O(1)
#        retrieve: O(n + dlogd), n is the size of the total logs
#                              , d is the size of the found logs
# Space: O(n)

class LogSystem(object):

    def __init__(self):
        self.__logs = []
        self.__granularity = {'Year': 4, 'Month': 7, 'Day': 10, \
                              'Hour': 13, 'Minute': 16, 'Second': 19}


    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.__logs.append((id, timestamp))


    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        i = self.__granularity[gra]
        begin = s[:i]
        end = e[:i]
        return sorted(id for id, timestamp in self.__logs \
                      if begin <= timestamp[:i] <= end)



