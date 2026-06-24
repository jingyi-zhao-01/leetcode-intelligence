# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: simplify-path
# source_path: LeetCode-Solutions-master/Python/simplify-path.py
# solution_class: Solution
# submission_id: 2c6f611140339f08fb0d984eb8b17322e5d3a92c
# seed: 403789761

# Time:  O(n)
# Space: O(n)

class Solution(object):
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack, tokens = [], path.split("/")
        for token in tokens:
            if token == ".." and stack:
                stack.pop()
            elif token != ".." and token != "." and token:
                stack.append(token)
        return "/" + "/".join(stack)