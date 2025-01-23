print("g")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x % 2 != 0:
            s += "#"
        else:
            s += "."
    print(s)

print("h")
for y in range(1, 7):
    s = ""
    #första och sista raderna
    if y == 1 or y == 6:
        for x in range(1, 9):
            s += "."
    #andra och näst sista raderna
    elif y == 2 or y == 5:
        for x in range(1, 9):
            if x == 1 or x == 8:
                s += "."
            else:
                s += "#"
    #mellersta raderna
    else:
        for x in range(1, 9):
            if x == 2 or x == 7:
                s += "#"
            else:
                s += "."
    print(s)

print("i")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if (x - y) % 3 == 0:
            s += "."
        elif (x - y) % 3 == 1:
            s += "#"
        else:
            s += "0"
    print(s)

print("j")
#TODO