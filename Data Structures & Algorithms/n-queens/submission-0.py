class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, d1, d2 = set(), set(), set()
        res = []
        def backtrack(row, placements):
            if row == n:
                res.append(placements.copy())
                return

            cur = ""
            for col in range(n):
                if col not in cols and (row - col) not in d1 and (col + row) not in d2:
                    cols.add(col)
                    d1.add(row - col)
                    d2.add(col + row)

                    placements.append(cur + "Q" + "".join(['.'] * (n - col - 1)))
                    backtrack(row + 1, placements)
                    placements.pop()

                    cols.remove(col)
                    d1.remove(row - col)
                    d2.remove(col + row)
                cur += '.'

        backtrack(0, [])
        return res
        
'''

(0, 0) (0, 1) (0, 2) (0, 3) (0, 4)
(1, 0) (1, 1) (1, 2) (1, 3)
(2, 0) (2, 1) (2, 2)
(3, 0) (3, 1) (3, 2)

'''
