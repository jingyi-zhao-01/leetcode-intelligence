# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: multiply-strings
# source_path: LeetCode-Solutions-master/Python/multiply-strings.py
# solution_class: Solution2
# submission_id: 3f5c7bb398a79e93b65a15c04e609f33de1d410e
# seed: 2133789938

# Time:  O(m * n)
# Space: O(m + n)

class Solution2(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        result = [0]*(len(num1)+len(num2))
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                result[i+j] += int(num1[i])*int(num2[j])
                result[i+j+1] += result[i+j]//10
                result[i+j] %= 10
        for i in reversed(xrange(len(result))):
            if result[i]:
                break
        return "".join(map(str, result[i::-1]))