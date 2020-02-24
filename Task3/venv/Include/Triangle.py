from typing import Iterable

from Point import Point
import math
class Triangle:



    def __init__(self, points) :
        self.__p1 = points[0]
        self.__p2 = points[1]
        self.__p3 = points[2]
        if(self.checkPoints()) :
            raise ValueError("Это не треугольник!")

    def getP1(self):
        return self.__p1

    def getP2(self):
        return self.__p2

    def getP3(self):
        return self.__p3

    def getP1P2(self):
        return math.sqrt((self.__p2.getX() - self.__p1.getX())**2 + (self.__p2.getY() - self.__p1.getY())**2)

    def getP1P3(self):
        return math.sqrt((self.__p3.getX() - self.__p1.getX()) ** 2 + (self.__p3.getY() - self.__p1.getY()) ** 2)

    def getP2P3(self):
        return math.sqrt((self.__p3.getX() - self.__p2.getX()) ** 2 + (self.__p3.getY() - self.__p2.getY()) ** 2)

    def isSimilar(self, triangle):
        return self.getP1P2() / triangle.getP1P2() == self.getP1P3() / triangle.getP1P3() ==  self.getP2P3() / triangle.getP2P3()

    def checkPoints(self):
        try:
            return  (self.__p3.getX() - self.__p1.getX()) / (self.__p2.getX() - self.__p1.getX()) ==  (self.__p3.getY() - self.__p1.getY()) / (self.__p2.getY() - self.__p1.getY())
        except ZeroDivisionError as e :
            try:
                return (self.__p2.getX() - self.__p1.getX()) / (self.__p3.getX() - self.__p1.getX()) ==  (self.__p2.getY() - self.__p1.getY()) / (self.__p3.getY() - self.__p1.getY())
            except ZeroDivisionError as e :
                try:
                    return (self.__p1.getX() - self.__p2.getX()) / (self.__p3.getX() - self.__p2.getX()) ==  (self.__p1.getY() - self.__p2.getY()) / (self.__p3.getY() - self.__p2.getY())
                except ZeroDivisionError as e :
                    return True