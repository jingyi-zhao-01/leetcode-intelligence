# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-and-say
# source_path: LeetCode-Solutions-master/Python/count-and-say.py
# solution_class: Solution
# submission_id: 8b05009b8e174dc66b85c1a26a3329831fcc3d75
# seed: 2063291373

# Time:  O(n * 2^n)
# Space: O(2^n)

class Solution(object):
    # @return a string
    def countAndSay(self, n):
        seq = "1"
        for i in xrange(n - 1):
            seq = self.getNext(seq)
        return seq

    def getNext(self, seq):
        i, next_seq = 0, ""
        while i < len(seq):
            cnt = 1
            while i < len(seq) - 1 and seq[i] == seq[i + 1]:
                cnt += 1
                i += 1
            next_seq += str(cnt) + seq[i]
            i += 1
        return next_seq