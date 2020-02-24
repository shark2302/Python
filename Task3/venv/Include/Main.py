from Triangle import Triangle
from Point import Point

def readTrianglesFromFile(fileName) :
    f = open(fileName, "r")
    triangles = []
    strFromFile = f.read().replace("\n", " ").split(" ")
    i = 0
    print(len(strFromFile))
    while i < len(strFromFile):
        j = i
        points = []
        while j < i + 6:
            points.append(Point(strFromFile[j], strFromFile[j + 1]))
            j += 2
        i += 6
        try:
            triangles.append(Triangle(points))
        except ValueError as e:
            print("Строка", i // 6, "не может быть интерпритирована как треугольник")
    return triangles

def createTriangleList(list) :
    allTriangles = []
    while len(list) != 0 :
        triangle = list.pop(0)
        similar = []
        similar.append(triangle)
        for tr in list :
            if(triangle.isSimilar(tr)) :
                similar.append(tr)
                list.remove(tr)
        allTriangles.append(similar)
    return allTriangles

print(createTriangleList(readTrianglesFromFile("test1.txt")))


