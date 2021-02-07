from typing import Any, List, Callable, Dict, Tuple
# *args and **kwargs

""" *args : Basically, it exhausts all the Positional Argumets and store them 
    in a tuple
    
    **kwargs : Basically, it exhausts all the KeyWord Arguments and store them 
    in Dictionary
    
    * : Basically, it indicates the end of the positional arguments
"""
# Decorators and Closours

def function_1(a: int, b: int, *args: Any, d) -> None:
    # take `n` number of arguments
    # here, d -> KeyWord Arguments
    print(a, b)
    for item in args: print(item, end = " ")
    print(d)

def function_2(*args: Any, **kwargs: Any) -> int:
    args: List = [int(item) for item in args]
    kwargs: List = [int(kwargs[key]) for key in kwargs]
    return max(sum(args), sum(kwargs))

def function_3() -> None: print("Function 3 called")
def function_4() -> None: print("Function 4 called")
def defaultFunction() -> None: print("Default Function...")

# Driver code
if __name__ == "__main__":
    function_1(1,3,423323,1332,32, d = "Hello")
    print(function_2(12,33,12, a= 113,b = 124))
    
    user_choice = int(input("Enter the Choice: "))
    Switch: Dict[int, Callable] = {
        1: function_1,
        2: function_2, 
        3: function_3, 
        4: function_4
    }.get(user_choice, defaultFunction)()
    
    
    

    