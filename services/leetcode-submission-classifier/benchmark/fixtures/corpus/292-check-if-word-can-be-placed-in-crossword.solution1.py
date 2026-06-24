# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-word-can-be-placed-in-crossword
# source_path: LeetCode-Solutions-master/Python/check-if-word-can-be-placed-in-crossword.py
# solution_class: Solution
# submission_id: a23c6ce80ff33e66f2901ea52fde04516c844201
# seed: 48230169

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def get_val(mat, i, j, transposed):
            return mat[i][j] if not transposed else mat[j][i]

        def get_vecs(mat, transposed):
            for i in xrange(len(mat) if not transposed else len(mat[0])):
                yield (get_val(mat, i, j, transposed) for j in xrange(len(mat[0]) if not transposed else len(mat)))

        for direction in (lambda x: iter(x), reversed):
            for transposed in xrange(2):
                for row in get_vecs(board, transposed):
                    it, matched = direction(word), True
                    for c in row:
                        if c == '#':
                            if next(it, None) is None and matched:
                                return True
                            it, matched = direction(word), True
                            continue
                        if not matched:
                            continue
                        nc = next(it, None)
                        matched = (nc is not None) and c in (nc, ' ')
                    if (next(it, None) is None) and matched:
                        return True
        return False