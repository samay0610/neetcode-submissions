from typing import List

def read_integers() -> List[int]:
    x = input()
    y = x.split(",")
    for i in range(len(y)):
        y[i] = int(y[i])
    return y

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
