# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sequence-reconstruction
# source_path: LeetCode-Solutions-master/Python/sequence-reconstruction.py
# solution_class: Solution
# submission_id: 2be8a05b7c0777065ef163dd3f65eda76ce73516
# seed: 819590827

# Time:  O(n * s), n is the size of org, s is the size of seqs
# Space: O(n)

import collections

class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not seqs:
            return False
        pos = [0] * (len(org) + 1)
        for i in xrange(len(org)):
            pos[org[i]] = i

        is_matched = [False] * (len(org) + 1)
        cnt_to_match = len(org) - 1
        for seq in seqs:
            for i in xrange(len(seq)):
                if not 0 < seq[i] <= len(org):
                    return False
                if i == 0:
                    continue
                if pos[seq[i-1]] >= pos[seq[i]]:
                    return False
                if is_matched[seq[i-1]] == False and pos[seq[i-1]] + 1 == pos[seq[i]]:
                    is_matched[seq[i-1]] = True
                    cnt_to_match -= 1

        return cnt_to_match == 0