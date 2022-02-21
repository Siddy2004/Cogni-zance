# QUESTION-5

# PROGRAM TO DISPLAY A TRIANGLE PATTERN

for i in range(5, 0, -1):
    for j in range(0, i):
        print(" ", end="")
    for k in range(i, 6):
        print("* ", end="")
    print()
