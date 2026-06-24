# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: design-a-number-container-system
# source_path: LeetCode-Solutions-master/Python/design-a-number-container-system.py
# solution_class: Solution
# submission_id: c25945321fc9bc3903ff215eed9368a1acafd776
# seed: 3281600002

# Time:  ctor:   O(1)
#        change: O(logn)
#        find:   O(1)
# Space: O(n)

from sortedcontainers import SortedList


# sorted list
class NumberContainers(object):

    def __init__(self):
        self.__idx_to_num = {}
        self.__num_to_idxs = collections.defaultdict(SortedList)

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if index in self.__idx_to_num:
            self.__num_to_idxs[self.__idx_to_num[index]].remove(index)
            if not self.__num_to_idxs[self.__idx_to_num[index]]:
                del self.__num_to_idxs[self.__idx_to_num[index]]
        self.__idx_to_num[index] = number
        self.__num_to_idxs[number].add(index)

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        return self.__num_to_idxs[number][0] if number in self.__num_to_idxs else -1
