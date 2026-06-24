# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-frequency-stack
# source_path: LeetCode-Solutions-master/Python/maximum-frequency-stack.py
# solution_class: Solution
# submission_id: b2d7a7ceb369db3c10dc7adcf5c4420cd5c9eba0
# seed: 2858254245

# Time:  O(1)
# Space: O(n)

import collections


class FreqStack(object):

    def __init__(self):
        self.__freq = collections.Counter()
        self.__group = collections.defaultdict(list)
        self.__maxfreq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.__freq[x] += 1
        if self.__freq[x] > self.__maxfreq:
            self.__maxfreq = self.__freq[x]
        self.__group[self.__freq[x]].append(x)   

    def pop(self):
        """
        :rtype: int
        """
        x = self.__group[self.__maxfreq].pop()
        if not self.__group[self.__maxfreq]:
            self.__group.pop(self.__maxfreq)
            self.__maxfreq -= 1
        self.__freq[x] -= 1
        if not self.__freq[x]:
            self.__freq.pop(x)
        return x



