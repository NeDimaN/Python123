for i in range(1, 9):
    for j in range(1, 9):
        if i == (9 - 1):
            print("*", end=" ")
        else:
            if j < (i + 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
