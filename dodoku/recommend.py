"""
Created on Decemeber 4,2021
 @author: Sterling Fuchsberger
 Modified: December 4,2021
 Comment: Added input check and error checking
 Modified: December 5,2021
 Comment: Added previous code that would help and finished methods
 Modified:December 6,2021
 Comment: Finished and developed according to previous test cases
 
"""
import re
import hashlib

def _recommend(parms):
    
    gridText = parms['grid']
    cellText = parms['cell']
    integrity = parms['integrity']
    #print(gridText)
    gridText = gridText[1:-1]
    #print(gridText)
    grid = list(gridText.split(","))
    #print(grid)
    
    
    errorCheck = _error_checking(grid, cellText, integrity)
    if errorCheck == False:
        result = "{'status':'error 101: invalid input formatting'}"
        return result
    
    
    
    board = _create_board(grid)
    
    cellPattern = r"^[rR](\d\d?)[cC](\d\d?)$"
    cellData = re.fullmatch(cellPattern, cellText)
    cellRow = int(cellData[1])
    cellColumn = int(cellData[2])
    row = int(cellRow -1)
    col = int(cellColumn-1)
    if row < 0 or row > 14:
        result = "{'status:': 'error 103: cell location out of bounds'}"
        return result
    if col < 0 or col > 14:
        result = "{'status:': 'error 103: cell location out of bounds'}"
        return result
        
    value = int(board[row][col])
    if value != 0:
        #print(row)
        #print(col)
        #print(value)
        result = "{'status:': 'error 102: cell already has number'}"
        return result
    
    notValues = [];
    if (row < 9 and row > -1) and (col < 9 and col >-1):
        for x in range(8):
            if board[row][x] != "0" :
                notValues.append(abs(int(board[row][x])))
        for x in range(8):
            if board[x][cellColumn-1] != "0":
                notValues.append(abs(int(board[x][col])))
                
    if (row > 5 and row < 14) and (col > 5 and col < 14) :
        for x in range(6,15):
            if board[row][x] != "0":
                notValues.append(abs(int(board[row][x])))
        for x in range(6,15): 
            if board[x][col] != "0":
                notValues.append(abs(int(board[x][col])))
             
    
    
    if(row == 1 | row == 4 | row == 7 | row == 10 | row == 13):
        row = row-1
    if(row == 2 | row == 5 | row == 8 | row == 11 | row == 14):
        row = row-2
    if(col == 1 | col == 4 | col == 7 | col == 10 | col == 13):
        col = col-1
    if(col == 2 | col == 5 | col == 8 | col == 11 | col == 14):
        col = col-2    
    for x in range(3):
        if int(board[row+x][col]) != 0:
            notValues.append(abs(int(board[row+x][col])))  
        if int(board[row][col+x]) != 0:
            notValues.append(abs(int(board[row][col+x])))   
    recommendation = []
    for x in range(1,10):
        if x not in notValues:
            recommendation.append(x)
             
            
        
                               
    result = {'recommendation': recommendation, 'status':'ok'}
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


def _error_checking(grid, cell, integrity):
    try:
        assert len(grid) == 153
        assert len(integrity) == 8
       
        
        cellPattern = r"^[rR](\d\d?)[cC](\d\d?)$"
        cellData = re.fullmatch(cellPattern, cell)
    
        assert cellData != None
        
        hashID = hashlib.sha256()
        hashID.update(repr(grid).encode())
        #print("String : ", end ="")
        #print(repr(grid))
        print("Hash Value : ", end ="")
        print(hashID)
        print("Hexadecimal equivalent: ",hashID.hexdigest())
        #print("Digest Size : ", end ="")
        #print(hashID.digest_size)
        #print("Block Size : ", end ="")
        #print(hashID.block_size)
        
        gridHash = hashID.hexdigest()
        assert integrity in repr(gridHash)
        

        
        
        
        
            
        return True
    except:
        return False
    


