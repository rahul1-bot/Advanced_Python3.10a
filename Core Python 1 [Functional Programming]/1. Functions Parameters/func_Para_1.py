from typing import Any, Tuple
## Positional vs Keyword Arguments
## Unpacking Iterables
    ## Application -> Swap Values

class RandomClass:
    def func(self, x: int, y: int) -> int:
        return x+y

t: Tuple = 1,2,3,
x, y = 12, 11
x, y = y, x 

# Driver Code
if __name__ == "__main__":
    for cases in range(int(input())):
        x, y = map(int, input().split())
        print(y)
        print(RandomClass().func(x, y))
    print(t)
         
        