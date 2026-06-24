# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-xor
# source_path: LeetCode-Solutions-master/Python/minimize-xor.py
# solution_class: Solution
# submission_id: cfdfbf614bd3e2c09e582ea4a05abf1cbfb76d19
# seed: 2036864482

# Time:  O(logn)
# Space: O(1)

# bit manipulation, greedy

class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def popcount(x):
            return bin(x)[2:].count('1')
        
        cnt1, cnt2 = popcount(num1), popcount(num2)
        result = num1
        cnt = abs(cnt1-cnt2)
        expect = 1 if cnt1 >= cnt2 else 0
        i = 0
        while cnt:
            if ((num1>>i)&1) == expect:
                cnt -= 1
                result ^= 1<<i
            i += 1
        return result