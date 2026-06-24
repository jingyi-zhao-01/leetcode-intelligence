# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: decode-the-slanted-ciphertext
# source_path: LeetCode-Solutions-master/Python/decode-the-slanted-ciphertext.py
# solution_class: Solution2
# submission_id: 7397d3a33d904fe6af5e876f136b13c32b4ba912
# seed: 3521035285

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        cols = len(encodedText)//rows
        result = []
        for i in xrange(cols):
            for j in xrange(i, len(encodedText), cols+1):
                result.append(encodedText[j])
        while result and result[-1] == ' ':
            result.pop()
        return "".join(result)