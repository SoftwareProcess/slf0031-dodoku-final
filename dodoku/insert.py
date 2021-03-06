"""
Created on October 20,2021
 @author: Sterling Fuchsberger
 Modified: October 20,2021
 Comment: Added level parameter scanning and associated table data and hash data
 Modified: October 20,2021
"""
#used for parsing
import re
def _insert(parms):
    #if (parms['grid'] && parms['integrity'] && parms['status'])) :
    #    result = {'status': 'error: 102'}
    #    return result
    
    
    
   
    gridText = parms['grid']
    cellText = parms['cell']
    value = parms.get('value','0')
    integrity = parms['integrity']
    print(gridText)
    gridText = gridText[1:-1]
    print(gridText)
    grid = list(gridText.split(","))
    print(grid)
    isGridOk = _error_checking(grid)
    if (isGridOk != True):
        result = {'status': 'error 104' }
        return result
    
    cellPattern = r"^[rR](\d\d?)[cC](\d\d?)$"
    cellData = re.fullmatch(cellPattern, cellText)
    
    if cellData is None:
        result = {'status': 'error:103' }
        return result
    if (len(grid) != 153) :
        lengthg = len(grid)
        result = {'status': 'error: 101','length': lengthg }
        return result
    
    cellRow = int(cellData[1])
    cellColumn = int(cellData[2])
    
    board = _create_board(grid)
    board[cellRow -1][cellColumn-1] = value
    
    grid = _create_grid(board)
    result = {"status":"ok", "grid":grid, "integrity": integrity}
    
    return result
    
    
    

def _create_board(grid):
    #Creates a 15x15 Dodoku board with the proper spacing 
    board =[]
    loc = 0
    w = range(15)
    x = range(6)
    y = range(3)
    z = range(9)
    print(len(grid))
    for n in x:
        row=[]
        for m in z:
            row.append(grid[loc])
            loc = loc + 1
        row += [None]*6
        board.append(row)
        
    for n in y:
        row=[]
        for m in w:
            row.append(grid[loc])
            loc = loc + 1
        board.append(row)
    for n in x:
        row=[]
        row += [None]*6
        for m in z:
            row.append(grid[loc])
            loc = loc + 1
        board.append(row)
    return board

def _create_grid(board):
    grid = []
    top = range(6)
    mid = range(6,9)
    bot = range(9,15)
    
    for m in top:
        ins = board[m][:9]
        grid.extend(ins)
    for m in mid:
        ins = board[m][:]
        grid.extend(ins)
    for m in bot:
        ins = board[m][6:15]
        grid.extend(ins)
    return grid
        
def _error_checking(grid):
    try:
        assert len(grid) == 153
        
            
        return True
    except:
        return False
