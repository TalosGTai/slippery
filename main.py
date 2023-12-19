class BaseCharater():
    def __init__(self, name = 'Karl', is_live = True) -> None:
        self.__name = name
        self.__is_live = is_live
    
    def __str__(self) -> str:
        return self.__name + ' live = ' + str(self.__is_live)