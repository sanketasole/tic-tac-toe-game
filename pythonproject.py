def printt(a): #print table
    i = 0
    while i<3:
        print("",a[i][0]," |", a[i][1],"| ", a[i][2])
        if i != 2:
            print("----|---|----")
        i = i+1
    print("")    

def valid(a, r, c): #to check wether the move is valid or not
    return not a[r][c] == ' '

def winner(a): #to check if given player win or not
    i = 0
    win = 0
    while i<3:# checking all rows and coloumn
        if a[0][i] != ' ' and a[0][i] == a[1][i] and a[0][i] == a[2][i]:
            return True
        elif a[i][0] != ' ' and a[i][0] == a[i][1] and a[i][0] == a[i][2]:
            return True
        i = i+1    
    
    if a[0][0] != ' ' and a[0][0] == a[1][1] and a[0][0] == a[2][2]: #checking digonal blocks
        return True
    elif a[1][1] != ' ' and a[0][2] == a[1][1] and a[0][2] == a[2][0]:
        return True
    
    return False

#main code    
t = 0
while t == 0:
    pa = [' ', ' '] #player name array 
    print("Enter player1 name")
    pa[0] = input()
    print("Enter player2 name")
    pa[1] = input()
    print(pa[0],"your symbol 'X'\n",pa[1],"your symbol is 'O'\nLET THE GAME BEGIN\n")
    sa = ['X', 'O'] #symbol array
    arr = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] # array for table
    win = 0 
    cp = 0 # cp = current player
    tie = 0
    while win == 0 and tie != 9:
        print(pa[cp], "enter your choice",sa[cp])
        row = int(input())
        col = int(input())
        while valid(arr, row, col):
            print("please enter valid input the cell is already occupied")
            row = int(input())
            col = int(input())
        arr[row][col] = sa[cp]
        if winner(arr):
            win = 1
            printt(arr)
            print("CONGRULATION !!\n",pa[cp],"wins the game")
            break
        else: printt(arr)
        tie = tie+1
        cp = ~cp #~ is use for complement of number
    if tie == 9:
        print("Match is tie Nice try", pa[0],pa[1])
    
    print("Press <0>Restart game\n<1>Quit")
    m = int(input())
    t = m
print("!! THANKS FOR PLAYING GAME !!")

