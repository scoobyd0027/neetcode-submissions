class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                sq = board[i][j]
                if sq == '.':
                    continue

                sub_group = (i // 3, j // 3)
                if (sq in rows[i] 
                    or sq in cols[j] 
                    or sq in boxes[sub_group]):
                    return False
                
                rows[i].add(sq)
                cols[j].add(sq)
                boxes[sub_group].add(sq)
        
        return True

'''
0,0 0,1 0,2
1,0,1,1,1,2
2,0,2,1,2,2


6,0,6,1,6,2
7,0,7,1,7,2
8,0,8,1,8,2

6,3,6,4,6,5
7,3,7,4,7,5
8,3,8,4,8,5

6,6,6,7,6,8
7,6,7,7,7,8
8,6,8,7,8,8
'''