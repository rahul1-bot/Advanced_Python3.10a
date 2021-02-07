from typing import Tuple, Dict, List, Set, Any
# Unpacking
# Extending Unpacking
def unpacking() -> List[int] or List[str]:
    l: List = list(range(1, 20, 2))
    a, *b = l           # a = 1; reminaing all elements goes to b
    print(b, a)
    ## This Extending unpacking applies to all Sequence types as well as 
    ## Iterables
    x, *y = "Hemlo Friemd"
    y = "->".join(y)
    print(x, y)
    
    ## This also works in this ways
    p, q, r, *s, t = list(range(20, 0, -2))
    print(s, p, q, t)

def listMerging() -> List[int] or List[str]:
    l: List = [1,2,3]
    l2: str = "Hemllo Friemd"
    l.extend(l2)
    return l

def setmerging() -> Set:
    s: Set = {12, "helllo", -11}
    s2: Set = {33, "Geiwn", 21}
    for item in s2: s.add(item)
    print(s)
    
def DictMerging() -> Dict:
    d: Dict[int, List[str]] = {
        73: ["Hello", "friemd"], 
        12: ["Bye", "Friemd"]
    }
    d2: Dict[int, List[str]] = {
        13: ["hi", "Friemd"]
    }
    d = {**d, **d2}             # Full Dictionaries Concatenation
    print(d)
    v = {*d, *d2}               # Dictionaries key Concatenation -> Set
    
    # We can merge `n` number of dictionaries
    dd: Dict[Any, Any] = {
        99: list(range(1,3,1)),
        114: (23,131,442,4, ["Hello", False, "friemd"]),
        **d, **d2
    }
    print(dd)

#Driver Code
if __name__ == "__main__":
    t: Tuple = 1,2,3,
    d: Dict[int,str] = {1: "Hemllo", 2: "Friemd"}
    for ptr in d.values(): print(ptr)
    for key, value in d.items():
        print(f"Key = {key}, Value = {value}")
    for index, key in enumerate(d):
        print(f"index = {index}, key = {key}, value = {d[key]}")
    
    # Extending Unpacking
    next_dict: Dict[str, int] = {
        "Hello": 1, "Friemd": 2
    }
    ## Dictionaries concatenation
    new_dict: Dict = {**d, **next_dict}
    print(new_dict)
    unpacking()
    print(listMerging())
    setmerging()
    DictMerging()