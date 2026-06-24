# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: design-browser-history
# source_path: LeetCode-Solutions-master/Python/design-browser-history.py
# solution_class: Solution
# submission_id: ed366da0d6bb169d656166d4a5af44c5c58a68b8
# seed: 1380083157

# Time:  ctor  : O(1)
#        visit : O(n)
#        back  : O(1)
#        foward: O(1)
# Space: O(n)

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.__history = [homepage]
        self.__curr = 0        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        while len(self.__history) > self.__curr+1:
            self.__history.pop()
        self.__history.append(url)
        self.__curr += 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.__curr = max(self.__curr-steps, 0)
        return self.__history[self.__curr]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.__curr = min(self.__curr+steps, len(self.__history)-1)
        return self.__history[self.__curr]
