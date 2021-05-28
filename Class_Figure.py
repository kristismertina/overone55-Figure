class Figure:
    def __init__ (self, color,*side):
        self.__color = color
        self.__side = side

    def __str__ (self):
        return f"{self.__color}, {self.__side}"

    @property
    def color (self):
        return self.__color

    @color.setter
    def color (self, c):
        self.__color = c

    @property
    def side (self):
        return self.__side

    @side.setter
    def side (self, s):
        self.__side = s

    @property
    def perimetr (self):
        if self.__side == int or self.__side == float:
            for i in self.__side:
                return sum(i)
        else:
            raise ValueError ("Enter num")


class Rectangle(Figure):

    def __init__(self, color,*side,width ):
        super.__init__(self, color,*side )
        self.__width = width

    @property
    def area (self,width):
        if (self.__side == int or self.__side == float) and (self.__width == int or self.__width == float) :
            return self.__side * self.__width
        else:
            raise ValueError ("Enter num")


class Squere (Figure):


    @property
    def area (self):
        if self.__side == int or self.__side == float:
            return  self.__side **2
        else:
            raise ValueError ("Enter num")


class Triagle (Figure):

    def __init__(self, color,*side,width, hight ):
        super.__init__(self, color,*side )
        self.__width = width
        self.__hight = hight

    @property
    def area (self, width, hight):
        self.__width = width
        self.__hight = hight
        if (self.__side == int or self.__side == float) and (self.__width == int or self.__width == float) and self.__hight == int or self.__hight == float:
            return  (self.__width /2) * self.__hight
        else:
            raise ValueError ("Enter num")



class Hexagon (Figure):

    @property
    def area (self):
        if self.__side == int or self.__side == float:
            return (3*(self.side ** 0.5)*self.side**2)/2
        else:
            raise ValueError ("Enter num")
