# Common Operations on Dictionaries
from typing import Any, Dict, Iterator
# Driver Code
if __name__ == "__main__":
    #1. Creation of Dictionaries
    dic: Dict[Any, Any] = {
        str(i): i**4 
        for i in range(5)
    }
    
    #2. Accessing the Elements
    for key in dic: print(f"Key = {key}")                                       # For accessing the Keys
    for key in dic: print(f"Value -> {dic[key]}")                               # For getting the Values
    for key, value in dic.items():                                              # For accessing both keys And values
        print(f"Key = {key}, Value = {value}")      
    for index, key in enumerate(dic):                                           # For Accessing index and Keys
        print(f"Index = {index}, Key = {key}")
    for index, key in enumerate(dic):                                           # For Accessing index, keys, values
        print(f"Index = {index}, Keys = {key}, Value = {dic[key]}")
        
    #3. Methods on Dictionaries
    """Methods
        1. clear() -> clears all the elements of the dictionary
        2. copy() -> performs Shallow copy of the Dictionary
        3. get(key: Any, default = ) -> Returns Value associated with the key else call default {para, class, obj, func}
        4. items() -> 
        5. pop(key: Any, default = ) -> Removes the element with that key and returns its value
        6. popitem() -> Remove element from dict and returns Tuple(key, Value) ### POP LAST ITEM WHICH IS INSERTED IN THE DIC [LIFO]
        7. update()
        8. values()
        9. Dic merging :
            d: Dict[Any, Any] = {**d1, **d2}
        # Basic searching for Key -> bool
        key in dic := True
        key not in dic := False
        # No. of keys: len(dic) := len<dic>
    """
        # Inserting in Dictionaries
    if "hemllo" not in dic:
        dic["hemllo"] = "Friemd"
    
 
    
    
    