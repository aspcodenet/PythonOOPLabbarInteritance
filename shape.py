from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, point):
        self.__Point = point
    
    def Test(self):
        print("Hallo")

    @abstractmethod
    def Draw(self):
        pass

class Circle(Shape):
    def __init__(self, point, radius:int):
        super().__init__(point)
        self.__radius = radius

    def Draw(self):
        print(f"Nu ritas en cirkel ut som är {self.__radius} stor") 

