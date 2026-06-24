# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: split-message-based-on-limit
# source_path: LeetCode-Solutions-master/Python/split-message-based-on-limit.py
# solution_class: Solution
# submission_id: 2448fe79127159b1a6f0bf5edc7662e6968d340d
# seed: 49476543

# Time:  O(n + rlogr), r is the number of messages
# Space: O(1)

# brute force, linear search (binary search doesn't work)

class Solution(object):
    def splitMessage(self, message, limit):
        """
        :type message: str
        :type limit: int
        :rtype: List[str]
        """
        cnt, l, total, base = 1, 1, len(message)+1, 1
        while 3+l*2 < limit:
            if total+(3+l)*cnt <= limit*cnt:
                break
            cnt += 1
            if cnt == base*10:
                l += 1
                base *= 10
            total += l
        if 3+l*2 >= limit:
            return []
        result = []
        j = 0
        for i in xrange(cnt):
            l = limit-(3+len(str(i+1))+len(str(cnt)))
            result.append("%s<%s/%s>"%(message[j:j+l], i+1, cnt))
            j += l
        return result