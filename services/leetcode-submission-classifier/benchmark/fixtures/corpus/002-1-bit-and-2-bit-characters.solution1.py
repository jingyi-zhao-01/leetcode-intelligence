# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 1-bit-and-2-bit-characters
# source_path: LeetCode-Solutions-master/Python/1-bit-and-2-bit-characters.py
# solution_class: Solution
# submission_id: 0ebb160504957949902710ee642eb53fd7e3dae1
# seed: 3027587322

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        parity = 0
        for i in reversed(xrange(len(bits)-1)):
            if bits[i] == 0:
                break
            parity ^= bits[i]
        return parity == 0