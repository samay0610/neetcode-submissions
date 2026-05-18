def add_two_numbers() -> int:
    x = input()
    x = x.split(",")
    for i in range(len(x)):
        x[i] = int(x[i])
    y = sum(x)
    return y



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
