from typing import List

def contains_duplicate(words: List[str]) -> bool:
    x = set(words)
    n1 = len(words)
    n2 = len(x)
    if n1 == n2:
        return False
    else:
        return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
