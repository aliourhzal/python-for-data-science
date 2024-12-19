from abc import ABC, abstractmethod

class Character(ABC):
    """
    Character class, each character created must be based on this one

    Attributes:
    - first_name (str): character first name
    - is_alive (bool): character health state, Defatults to True

    Methodes:
    - die(): abstract method changing is_alive to False
    """

    def __init__(self, first_name, is_alive = True):
        """
        Character class constructor
        
        Args:
        - first_name (str): character first_name
        - is_alive (bool): sets character health state, Defaults to True
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Character class ABSTRACT method, sets character health state to False

        Args: None 
        """
        self.is_alive = False
        return self


class Stark(Character):
    """
        Stark class, an implementation of the Character abstact class

        Attributes:
        - same as Character class

        Methodes:
        - same as Character class
    """
    def die(self):
        """
        die method, sets character health state to False

        Args: None 
        """
        return super().die()
