# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: next-closest-time
# source_path: LeetCode-Solutions-master/Python/next-closest-time.py
# solution_class: Solution
# submission_id: b40522ce7c815e92dffc86b9367d93c9cbcab9a7
# seed: 52349582

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        h, m = time.split(":")
        curr = int(h) * 60 + int(m)
        result = None
        for i in xrange(curr+1, curr+1441):
            t = i % 1440
            h, m = t // 60, t % 60
            result = "%02d:%02d" % (h, m)
            if set(result) <= set(time):
                break
        return result