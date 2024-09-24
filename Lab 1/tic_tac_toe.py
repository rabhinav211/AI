import random

tic = [["-"] * 3 for _ in range(3)]
players = ["O", "X"]
current_player = "O"

def place(i, j, player):
    tic[i][j] = player

def listify():
    res = []
    for i in range(3):
        res.append("".join(tic[i])) 
    for i in range(3):
        temp = ""
        for j in range(3):
            temp += tic[j][i] 
        res.append(temp)


    temp = ""
    for i in range(3):
        temp += tic[i][i]
    res.append(temp)
    res.append(tic[0][2] + tic[1][1] + tic[2][0])

    return res

def check(lis):
    count = -1
    for i in lis:
        count = max(count, i.count("-"))
        if i.count("O") == 3:
            return 0 
        if i.count("X") == 3:
            return 1 
    if count == -1:
        return -1 
    return 4 

def display():
    for i in range(3):
        for j in range(3):
            print(tic[i][j], end=" ")
        print("\n")
    print()

def computer_move():

    for i in range(3):
        for j in range(3):
            if tic[i][j] == "-":
                place(i, j, "X")
                if check(listify()) == 1:
                    return 
                place(i, j, "-") 

    for i in range(3):
        for j in range(3):
            if tic[i][j] == "-":
                place(i, j, "O")
                if check(listify()) == 0:
                    place(i, j, "X") 
                    return
                place(i, j, "-") 
    

    for i in range(3):
        for j in range(3):
            if tic[i][j] == "-":
                place(i, j, "X")
                return

def main():
    global current_player

    while True:
        display()
        lis = listify()
        flag = check(lis)

        if flag == 0:
            print("Player O wins!")
            break
        elif flag == 1:
            print("Player X (Computer) wins!")
            break
        elif flag == -1:
            print("It's a draw!")
            break

        if current_player == "O":

            print("Player O's turn")
            i, j = map(int, input("Enter row and column (0-2): ").split())
            if tic[i][j] == "-":
                place(i, j, current_player)
                current_player = "X"
            else:
                print("Invalid move, try again.")
        else:
            print("Computer's turn")
            computer_move()
            current_player = "O"


main()
