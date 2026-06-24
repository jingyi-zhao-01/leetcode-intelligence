# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-valid-words-for-each-puzzle
# source_path: LeetCode-Solutions-master/Python/number-of-valid-words-for-each-puzzle.py
# solution_class: Solution
# submission_id: 172a69a2feccfb51b57a347733b2a73dd4b3585a
# seed: 4263055468

# Time:  O(n*l + m*L), m is the number of puzzles, L is the length of puzzles
#                    , n is the number of words, l is the max length of words
# Space: O(L!)

class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        L = 7
        def search(node, puzzle, start, first, met_first):
            result = 0
            if "_end" in node and met_first:
                result += node["_end"]
            for i in xrange(start, len(puzzle)):
                if puzzle[i] not in node:
                    continue
                result += search(node[puzzle[i]], puzzle, i+1,
                                 first, met_first or (puzzle[i] == first))
            return result

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for word in words:
            count = set(word)
            if len(count) > L:
                continue
            word = sorted(count)
            end = reduce(dict.__getitem__, word, trie)
            end["_end"] = end["_end"]+1 if "_end" in end else 1
        result = []
        for puzzle in puzzles:
            first = puzzle[0]
            result.append(search(trie, sorted(puzzle), 0, first, False))
        return result