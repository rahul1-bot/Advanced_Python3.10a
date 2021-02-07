from typing import Any, Dict, List, Set, Mapping, MutableSequence, MutableSet, Iterator, Iterable, Callable
# Classes : 1
class RandomClass:
    def __init__(self, var1: str, var2: str) -> None:
        # Here properties are called ...
        self.var1: str = var1        
        self.var2: str = var2
        
    """def __setattr__(self) -> None:
        pass

        def __getattribute__(self) -> Any:
            pass
        
        def __delattr__(self) -> None:
            pass   

        def __repr__(self) -> str:
            pass
        
        def __doc__(self) -> str:
            pass
        
        def __class__(self) -> Any:
            pass"""         
    
    # -- Now we can't change the variables -- #
    # -- Getters --  + __name__mangling__#
    @property
    def var1(self) -> str:
        return self.__var1
    @property
    def var2(self) -> str:
        return self.__var2
    
    # -- Setters -- #
    @var1.setter                                                                            
    def var1(self, value: str) -> None:
        if not isinstance(value, str):
            raise AttributeError
        self.__var1 = value
        
    @var2.setter
    def var2(self, value: str) -> None:
        if not isinstance(value, str):
            raise AttributeError
        self.__var2 = value
    
    # here __var1 and __var2 are different and we can't access them even outside of the class    
    
    def show(self) -> Any:
        return self.var1, self.var2


# Driver Code
if __name__ == "__main__":
    random = RandomClass("Hemllo", "Friemd!")
    print(random.show())
    random.var1 = "Friemds"
    print(random.var1)

    # let's check the MRO of this Class
    print(random.__dict__)
    
    # __var1: changed to : _RandomClass__var1
    # __var2: changed to : _RandomClass__var2
    
    inp = lambda: map(int, input())

    # -- inputs -- #
    #arr: List[List[int]] = [[int(input()) for j in range(3)] for i in range(3)]
    #print(arr)
    #matrix: List[List[int]] = [[1 if i % 2 else ... if ... else 1 for j in range(3)] for i in range(3)]
    matrix: List[List[int]] = [[1 if j == 0 or i == 1 else -1 if j*i == 2 else 0 for j in range(3)] for i in range(3)]
    print(matrix)
    