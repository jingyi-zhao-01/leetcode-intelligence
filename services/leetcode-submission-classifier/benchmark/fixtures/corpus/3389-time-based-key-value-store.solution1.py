# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: time-based-key-value-store
# source_path: LeetCode-Solutions-master/Python/time-based-key-value-store.py
# solution_class: Solution
# submission_id: 7d31897e7862cda25d50f1bfea3580b80634fbaa
# seed: 1449282297

# Time:  set: O(1)
#        get: O(logn)
# Space: O(n)

import collections
import bisect


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.lookup[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        A = self.lookup.get(key, None)
        if A is None:
            return ""
        i = bisect.bisect_right(A, (timestamp+1, 0))
        return A[i-1][1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
