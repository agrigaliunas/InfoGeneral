b=9
for fil in range(b):
    for col in range(b):
        if col == b//2 and fil >= b//2 or fil+col == b-1 and fil > b//2 or fil == col and fil > b//2 or fil > (b//2)+1 and col < b-2 or fil > (b//2)+1 and col > b+1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
