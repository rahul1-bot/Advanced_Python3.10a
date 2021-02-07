import collections
from typing import Dict, Any


def DCreating() -> Dict[Any, Any]:
    d: Dict[Any, Any] = {
        "key_1" : "Value_1",
        "Key_2" : "value_2",
        "key_3" : ["Value_a", "Value_b"],
        "key_4" : ("value", False, [1,2,3], {False, True, 11})
    }
    # Dict Comprehentions
    #value = {
        # key : Value   
    #}
    dvalue: Dict[Any, Any] = {
        str(i): i**2                # Performing functions and actions
        for i in range(5)           # Looping
        if i % 2 == 0               # Some filter conditions
    }
    dvalue_2 = {}                   # This is a Non- Pythonic way of doing
    for i in range(1, 10):          # Looks very Ugly
        if i %2 == 0:               # Don't do this until 
            dvalue_2[i] = i**2      # you don't have much calculations inside
    
def func_1(x, y): return x+y
def func_2(x, y): return x*y
def func_3(x, y): return x/y
def func_4(x, y): return x//y

# Driver Code
if __name__ == "__main__":
    # Creating the Functions and functions arguments dict
    functions: Dict[Any, Any] = {
        func_1: (10, 20),           # Key<functions> : value<Func_Args>
        func_2: (20, 30),               
        func_3: (10, 11),
        func_4: (30, 10)
    }
    
    # Dict containing function Object and Result of functions
    functions_ans: Dict[Any, Any] = {
        func: func(*functions[func]) 
        for func in functions
    }
    
    # Iterating over the dict to get ans
    for value in functions_ans:
        print(functions_ans[value])
        
    # Retriving keys and Values at the same time
    for key, value in functions.items():
        print(f"Ans -> {key(*value)}")
         
    #print(math.factorial(12))
    print(collections.deque())
    print(math.factorial(1))
    
    