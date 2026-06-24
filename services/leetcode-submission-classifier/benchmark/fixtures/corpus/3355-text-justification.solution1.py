# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: text-justification
# source_path: LeetCode-Solutions-master/Python/text-justification.py
# solution_class: Solution
# submission_id: 97eeee532b2e953e3e64bd002170ac605d7205d7
# seed: 3271012964

# Time:  O(n)
# Space: O(k), k is maxWidth.

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def addSpaces(i, spaceCnt, maxWidth, is_last):
            if i < spaceCnt:
                # For the last line of text, it should be left justified,
                # and no extra space is inserted between words.
                return 1 if is_last else (maxWidth // spaceCnt) + int(i < maxWidth % spaceCnt)
            return 0

        def connect(words, maxWidth, begin, end, length, is_last):
            s = []  # The extra space O(k) is spent here.
            n = end - begin
            for i in xrange(n):
                s += words[begin + i],
                s += ' ' * addSpaces(i, n - 1, maxWidth - length, is_last),
            # For only one word in a line.
            line = "".join(s)
            if len(line) < maxWidth:
                line += ' ' * (maxWidth - len(line))
            return line

        res = []
        begin, length = 0, 0
        for i in xrange(len(words)):
            if length + len(words[i]) + (i - begin) > maxWidth:
                res += connect(words, maxWidth, begin, i, length, False),
                begin, length = i, 0
            length += len(words[i])

        # Last line.
        res += connect(words, maxWidth, begin, len(words), length, True),
        return res