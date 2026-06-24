# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: word-ladder-ii
# source_path: LeetCode-Solutions-master/Python/word-ladder-ii.py
# solution_class: Solution2
# submission_id: 7d649c179916943d0f221ceb32be780a75c59366
# seed: 2011052396

# Time:  O(b^(d/2)), b is the branch factor of bfs, d is the result depth
# Space: O(w * l), w is the number of words, l is the max length of words

from collections import defaultdict
from string import ascii_lowercase

class Solution2(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        dictionary = set(wordList)
        result, cur, visited, found, trace = [], [beginWord], set([beginWord]), False, defaultdict(list)

        while cur and not found:
            for word in cur:
                visited.add(word)

            next = set()
            for word in cur:
                for i in xrange(len(word)):
                    for c in ascii_lowercase:
                        candidate = word[:i] + c + word[i + 1:]
                        if candidate not in visited and candidate in dictionary:
                            if candidate == endWord:
                                found = True
                            next.add(candidate)
                            trace[candidate].append(word)
            cur = next

        if found:
            self.backtrack(result, trace, [], endWord)

        return result

    def backtrack(self, result, trace, path, word):
        if not trace[word]:
            path.append(word)
            result.append(path[::-1])
            path.pop()
        else:
            for prev in trace[word]:
                path.append(word)
                self.backtrack(result, trace, path, prev)
                path.pop()