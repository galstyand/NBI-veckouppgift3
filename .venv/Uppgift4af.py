print("a")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        s += "."
    print(s)

print("b")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

print("c")
for y in range(1, 7):
    s = ""
    for x in range(1, 7):
        if x == 3:
            for z in range(1, 4):
                s += "#"
        else:
            s += "."
    print(s)

print("d")
for y in range(1, 7):
    s = ""
    if y == 3:
        s = "########"
    else:
        s = ""
        for x in range(1, 9):
            if x == 3:
                s += "#"
            s += "."
    print(s)

print("e")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 5:
            s += "#"
        elif x == 7-y:
            s += "#"
        else:
            s += "."
    print(s)

print("f")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y or x == 7 - y:
            s += "#"
        else:
            s += "."
    print(s)