class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Create hashsets for rows and cols

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        
        #Create dictionary for the blocks
        blocks = collections.defaultdict(set)

        #Check if individual elements are duplicates
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                block_key = (row // 3, col // 3)
                if val != '.':
                    #Check if val is in the row bucket
                    if val in rows[row]:
                        return False
                    #Check if val is in the col bucket
                    if val in cols[col]:
                        return False
                    #Check if val is in blocks bucket
                    if val in blocks[block_key]:
                        return False
                    #If val isnt in any of the buckets add to all
                    else:
                        blocks[block_key].add(val)
                        rows[row].add(val)
                        cols[col].add(val)

        return True