# upper
for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end=" ")
    print("\r")
# lower
for i in range(4, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print("\r")