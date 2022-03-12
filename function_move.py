def up_move(input_list):
    if(input_list[0] == 0 and input_list[1] <= 17 and input_list[1] >=3 ):
        input_list[0] += 2
    
    elif(input_list[0] == 0 and input_list[1] >= 17 ):
        input_list[0] = 1
        input_list[1] -= 1     
        
    elif input_list[1] < 1:
        input_list[0] = 0
        input_list[1] = 19
    
    else:
        input_list[0] -=1
        input_list[1] -=1
    
    
    
    return input_list

def left_move(input_list):
    
    if(input_list[0] == 0 and input_list[1] <= 1):
        input_list[1] = 19
    
    elif(input_list[0] == 1 and input_list[1] <= 2):
        input_list[1] = 18
    
    elif(input_list[0] == 2 and input_list[1] <= 3):
        input_list[1] = 15
    
    else:
        input_list[1]-=2
    
    return input_list
        
def right_move(input_list):
    
    if(input_list[0] == 0 and input_list[1] >= 19):
        input_list[1] = 1
    
    elif(input_list[0] == 1 and input_list[1] >= 18 ):
        input_list[1] = 2
    
    elif(input_list[0] == 2 and input_list[1] >= 15):
        input_list[1] = 3
    
    else:
        input_list[1]+=2
    
    return input_list
        
def down_move(input_list):
    
    if(input_list[0] == 0 and input_list[1] == 19):     # jump from letter _D_[0;19] to letter _q_[0;1]
        input_list[1] = 1
        input_list[0] = 0
    
    elif(input_list[0] == 1 and input_list[1] == 16):   # jump from letter _k_[1;16] to letter _o_[0;17]
        input_list[1] = 17
        input_list[0] = 0
    
    elif(input_list[0] == 2):                           # jump from 2-list to 0-list
        input_list[0] -=2
        
    else:    
        input_list[1] += 1
        input_list[0] += 1
        
    return input_list


