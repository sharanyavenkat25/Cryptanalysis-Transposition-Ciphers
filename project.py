import math 

def encryptMessage(msg,key): 
    cipher = "" 
  
    # track key indices 
    k_indx = 0
  
    msg_len = float(len(msg)) 
    msg_lst = list(msg) 
    key_lst = sorted(list(key)) 
  
    # calculate column of the matrix 
    col = len(key) 
      
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 
  
    # add the padding character '_' in empty 
    # the empty cell of the matix  
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('_' * fill_null) 
  
    # create Matrix and insert message and  
    # padding characters row-wise  
    matrix = [msg_lst[i: i + col]  
              for i in range(0, len(msg_lst), col)] 
  
    # read matrix column-wise using key 
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
        cipher += ''.join([row[curr_idx]  
                          for row in matrix]) 
        k_indx += 1
  
    return cipher 
  
# Decryption 
def decryptMessage(cipher,key): 
    msg = "" 
  
    # track key indices 
    k_indx = 0
  
    # track msg indices 
    msg_indx = 0
    msg_len = float(len(cipher)) 
    msg_lst = list(cipher) 
  
    # calculate column of the matrix 
    col = len(key) 
      
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 
  
    # convert key into list and sort  
    # alphabetically so we can access  
    # each character by its alphabetical position. 
    key_lst = sorted(list(key)) 
  
    # create an empty matrix to  
    # store deciphered message 
    dec_cipher = [] 
    for _ in range(row): 
        dec_cipher += [[None] * col] 
  
    # Arrange the matrix column wise according  
    # to permutation order by adding into new matrix 
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
  
        for j in range(row): 
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
            msg_indx += 1
        k_indx += 1
  
    # convert decrypted msg matrix into a string 
    try: 
        msg = ''.join(sum(dec_cipher, [])) 
    except TypeError: 
        raise TypeError("This program cannot", 
                        "handle repeating words.") 
  
    null_count = msg.count('_') 
  
    if null_count > 0: 
        return msg[: -null_count] 
  
    return msg 

def encryptRailFence(text, key): 
  
    # create the matrix to cipher  
    # plain text key = rows ,  
    # length(text) = columns 
    # filling the rail matrix  
    # to distinguish filled  
    # spaces from blank ones 
    rail = [['\n' for i in range(len(text))] 
                  for j in range(key)] 
      
    # to find the direction 
    dir_down = False
    row, col = 0, 0
      
    for i in range(len(text)): 
          
        # check the direction of flow 
        # reverse the direction if we've just 
        # filled the top or bottom rail 
        if (row == 0) or (row == key - 1): 
            dir_down = not dir_down 
          
        # fill the corresponding alphabet 
        rail[row][col] = text[i] 
        col += 1
          
        # find the next row using 
        # direction flag 
        if dir_down: 
            row += 1
        else: 
            row -= 1
    # now we can construct the cipher  
    # using the rail matrix 
    result = [] 
    for i in range(key): 
        for j in range(len(text)): 
            if rail[i][j] != '\n': 
                result.append(rail[i][j]) 
    return("" . join(result)) 
      
# This function receives cipher-text  
# and key and returns the original  
# text after decryption 
def decryptRailFence(cipher, key): 
  
    # create the matrix to cipher  
    # plain text key = rows ,  
    # length(text) = columns 
    # filling the rail matrix to  
    # distinguish filled spaces 
    # from blank ones 
    rail = [['\n' for i in range(len(cipher))]  
                  for j in range(key)] 
      
    # to find the direction 
    dir_down = None
    row, col = 0, 0
      
    # mark the places with '*' 
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key - 1: 
            dir_down = False
          
        # place the marker 
        rail[row][col] = '*'
        col += 1
          
        # find the next row  
        # using direction flag 
        if dir_down: 
            row += 1
        else: 
            row -= 1
              
    # now we can construct the  
    # fill the rail matrix 
    index = 0
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((rail[i][j] == '*') and
               (index < len(cipher))): 
                rail[i][j] = cipher[index] 
                index += 1
          
    # now read the matrix in  
    # zig-zag manner to construct 
    # the resultant text 
    result = [] 
    row, col = 0, 0
    for i in range(len(cipher)): 
          
        # check the direction of flow 
        if row == 0: 
            dir_down = True
        if row == key-1: 
            dir_down = False
              
        # place the marker 
        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1
              
        # find the next row using 
        # direction flag 
        if dir_down: 
            row += 1
        else: 
            row -= 1
    return("".join(result)) 
  
# Driver Code 

if __name__ == '__main__':
    ans=True
    while ans:
        print ("""

        1.Columnar Transposition
        2.Double Columnar Transposition
        3.Rail Fence Cipher
        4.Exit/Quit
        """)
        ans=input("Please choose one of the above encryption methods: ")
        choice=input("Choose 1. Encryption 2. Decryption \n")
        msg=input("Please enter the message you wish to encrypt/decrypt below: ")
        if ans=="1": 
            print("\n Columnar Transposition")
            n=input("Please enter the key:")
            if choice=="1":
                cipher = encryptMessage(msg,n)
            else: 
                cipher = decryptMessage(msg,n) 
        elif ans=="2":
            print("\n Double Columnar Transposition")
            n=input("Please enter the key:")
            if choice=="1":
                cipher = encryptMessage(msg)
            else: 
                cipher = decryptMessage(msg) 
        elif ans=="3":
            print("\n Rail Fence Cipher")
            n=int(input("Please enter the key:"))
            if choice=="1":
                cipher = encryptRailFence(msg, n)
            else: 
                cipher = decryptRailFence(msg, n)
            
        elif ans=="4":
            print("\n Goodbye!")
            exit() 
        else:
            print("\n Not Valid Choice Try again")
            exit()
     
        print("Encrypted Message: {}". 
                   format(cipher)) 
      
    
      
