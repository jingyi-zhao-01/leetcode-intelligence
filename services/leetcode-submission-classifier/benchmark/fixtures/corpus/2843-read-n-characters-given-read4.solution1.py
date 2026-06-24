# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: read-n-characters-given-read4
# source_path: LeetCode-Solutions-master/Python/read-n-characters-given-read4.py
# solution_class: Solution
# submission_id: 9b86b0a6e21d76f3482fc642d534586b073bac1e
# seed: 4193951311

# Time:  O(n)
# Space: O(1)

def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1

    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        read_bytes = 0
        buffer = [''] * 4
        for i in xrange((n+4-1)//4):
            size = min(read4(buffer), n-read_bytes)
            buf[read_bytes:read_bytes+size] = buffer[:size]
            read_bytes += size
        return read_bytes