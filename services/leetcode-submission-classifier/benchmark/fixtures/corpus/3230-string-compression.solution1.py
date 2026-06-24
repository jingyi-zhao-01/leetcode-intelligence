# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: string-compression
# source_path: LeetCode-Solutions-master/Python/string-compression.py
# solution_class: Solution
# submission_id: 2cb76aab40cbdf2bbf1924ffcbd9c391728edceb
# seed: 2974393459

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        anchor, write = 0, 0
        for read, c in enumerate(chars):
            if read+1 == len(chars) or chars[read+1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    n, left = read-anchor+1, write
                    while n > 0:
                        chars[write] = chr(n%10+ord('0'))
                        write += 1
                        n /= 10
                    right = write-1
                    while left < right:
                        chars[left], chars[right] = chars[right], chars[left]
                        left += 1
                        right -= 1
                anchor = read+1
        return write