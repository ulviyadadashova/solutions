class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        atl, pac = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c]) #down
            dfs(r - 1, c, visit, heights[r][c]) #up
            dfs(r, c - 1, visit, heights[r][c]) #left
            dfs(r, c + 1, visit, heights[r][c]) #right
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) #top border
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) #bottom border
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) #left border
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res

        

        