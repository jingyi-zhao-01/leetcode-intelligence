# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-array-empty
# source_path: LeetCode-Solutions-master/Python/make-array-empty.py
# solution_class: Solution2
# submission_id: 79aea55871afa1304414b034e9b2817b508fee98
# seed: 3997074788

# Time:  O(nlogn)
# Space: O(n)

# sort

class Solution2(object):
    def countOperationsToEmptyArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        class BIT(object):  # 0-indexed.
            def __init__(self, n):
                self.__bit = [0]*(n+1)  # Extra one for dummy node.

            def add(self, i, val):
                i += 1  # Extra one for dummy node.
                while i < len(self.__bit):
                    self.__bit[i] += val
                    i += (i & -i)

            def query(self, i):
                i += 1  # Extra one for dummy node.
                ret = 0
                while i > 0:
                    ret += self.__bit[i]
                    i -= (i & -i)
                return ret
        
        bit = BIT(len(nums))
        idxs = range(len(nums))
        idxs.sort(key=lambda x: nums[x])
        result = len(nums)
        prev = -1
        for i in idxs:
            if prev == -1:
                result += i
            elif prev < i:
                result += (i-prev)-(bit.query(i)-bit.query(prev-1))
            else:
                result += ((len(nums)-1)-bit.query(len(nums)-1))-((prev-i)-(bit.query(prev)-bit.query(i-1)))
            bit.add(i, 1)
            prev = i
        return result