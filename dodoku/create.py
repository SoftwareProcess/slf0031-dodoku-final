def _create(parms):
    from hashlib import sha256
    if (parms['level'] =='1'):
        grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0]
        integrity = sha256(grid.hexdigest())
             
        result= {'grid': '[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0]', 'integrity': integrity[0:6],'status': 'ok'}
        
    elif (parms['level'] == '2'):
        grid = [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,-7,0,0,0,0,-8,0,-4,0,0,-1,0,0,0,0,-9,0,0,0,0,0,0,0,0,0,0,0,-7,0,-5,-8,0,0,0,-2,0,0,0,-6,-1,0]
        integrity = sha256(grid.hexdigest())
        result={'grid': '[0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,-7,0,0,0,0,-8,0,-4,0,0,-1,0,0,0,0,-9,0,0,0,0,0,0,0,0,0,0,0,-7,0,-5,-8,0,0,0,-2,0,0,0,-6,-1,0]', 'integrity': integrity[0:6], 'status': 'ok'}
        
    elif (parms['level'] == '3'):
        grid = [0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,0,0,-6,0,-4,0,0,0,0,0,0,0,-5,0,0,0,0,0,-9,-8,-2,0,0,0,-4,-3,0,0,-7,0,0,0,0,0,0]
        integrity = sha256(grid.hexdigest())
        result={'grid': '[0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,0,0,-6,0,-4,0,0,0,0,0,0,0,-5,0,0,0,0,0,-9,-8,-2,0,0,0,-4,-3,0,0,-7,0,0,0,0,0,0]', 'integrity': integrity[0:6], 'status': 'ok'}
    else:
        result = {'status': 'error:100'}
    
    
    return result

