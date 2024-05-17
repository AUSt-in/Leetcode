class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # What I am thinking right now
        #Build a hashmap and check row that maps 1 to 9
        # check row and columns and see 1-9
        #Check the rows and cols for 3*3
        rows = [set() for x in range(9)]
        cols = [set() for x in range(9)]
        square = [[set() for x in range(3)] for y in range(3)] #0 to 8 working with floors
        #We are going for O(n*2)
        for x in range(9):
            for y in range(9):
                cell = board[x][y]
                if cell == ".":
                    continue
                if cell in rows[x] or cell in column[y] or cell in square[x//3][y//3]
                    return False
                row[x].add(cell)
                column[y].add(cell)
                squares[x//3][y//3].add(cell)

        return True
