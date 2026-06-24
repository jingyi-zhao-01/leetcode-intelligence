# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-watch
# source_path: LeetCode-Solutions-master/Python/binary-watch.py
# solution_class: Solution
# submission_id: 559a3349b93c9b28e0a650c7f5d0acbe2d7f68f4
# seed: 1878544838

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def bit_count(bits):
            count = 0
            while bits:
                bits &= bits-1
                count += 1
            return count

        return ['%d:%02d' % (h, m) for h in xrange(12) for m in xrange(60)
                if bit_count(h) + bit_count(m) == num]

    def readBinaryWatch2(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ['{0}:{1}'.format(str(h), str(m).zfill(2))
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]