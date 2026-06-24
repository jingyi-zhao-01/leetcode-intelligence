# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: decode-the-slanted-ciphertext
# source_path: LeetCode-Solutions-master/Python/decode-the-slanted-ciphertext.py
# solution_class: Solution
# submission_id: 573bcd55f98f9bb12b07a45bb4229dfdd7279be1
# seed: 2254073086

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        cols = len(encodedText)//rows
        k = len(encodedText)
        for i in reversed(xrange(cols)):
            for j in reversed(xrange(i, len(encodedText), cols+1)):
                if encodedText[j] != ' ':
                    k = j
                    break
            else:
                continue
            break
        result = []
        for i in xrange(cols):
            for j in xrange(i, len(encodedText), cols+1):
                result.append(encodedText[j])
                if j == k:
                    break
            else:
                continue
            break
        return "".join(result)