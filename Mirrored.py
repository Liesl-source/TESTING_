for r in range(1,6):

    # printing the space
    for c in range(4,r-1,-1):
        print(' ',end='')

    # printing the star
    for c in range(0,r):
        print('*',end='')

    print()