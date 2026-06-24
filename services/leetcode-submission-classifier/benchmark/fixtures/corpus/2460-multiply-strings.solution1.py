# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: multiply-strings
# source_path: LeetCode-Solutions-master/Python/multiply-strings.py
# solution_class: Solution
# submission_id: e0ee06fc917aa52a4bdfeb5b1e9809e81f660196
# seed: 11912204

# Time:  O(m * n)
# Space: O(m + n)

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0]*(len(num1)+len(num2))
        for i in reversed(xrange(len(num1))):
            for j in reversed(xrange(len(num2))):
                result[i+j+1] += int(num1[i])*int(num2[j])
                result[i+j] += result[i+j+1]//10
                result[i+j+1] %= 10
        for i in xrange(len(result)):
            if result[i]:
                break
        return "".join(map(lambda x: str(x), result[i:]))