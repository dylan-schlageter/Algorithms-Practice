class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_cols = len(board[0])
        num_rows = len(board)
        path = set()
        def dfs(i, r, c):
            if i == len(word): #correct-case
                return True
            if (r < 0 or c < 0 or r >= num_rows or c >= num_cols
            or (r,c) in path or word[i] != board[r][c]):
                return False#base-case

            path.add((r,c))
            if (dfs(i+1,r+1,c) or
            dfs(i+1,r-1,c) or
            dfs(i+1,r,c+1) or
            dfs(i+1,r,c-1)):
                return True
            
            path.remove((r,c))

        for r in range(num_rows):
            for c in range(num_cols):
                if dfs(0,r,c): return True
        
        return False
