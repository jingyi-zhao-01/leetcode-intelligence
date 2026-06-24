# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-index-of-the-large-integer
# source_path: LeetCode-Solutions-master/Python/find-the-index-of-the-large-integer.py
# solution_class: Solution
# submission_id: b279b78df219afe8ddf613e1fba5b7a2ac70272e
# seed: 1025927040

# Time:  O(logn)
# Space: O(1)

class ArrayReader(object):
   def compareSub(self, l, r, x, y):
       pass

   def length(self):
       pass

class Solution(object):
    def getIndex(self, reader):
        """
        :type reader: ArrayReader
        :rtype: integer
        """
        left, right = 0, reader.length()-1
        while left < right:
            mid = left + (right-left)//2
            if reader.compareSub(left, mid, mid if (right-left+1)%2 else mid+1, right) >= 0:
                right = mid
            else:
                left = mid+1
        return left