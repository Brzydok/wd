class Point:

    def __init__(self, x=0, y=0):
        """Konstuktor punktu."""
        self.x = x
        self.y = y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __str__(self):
        return f'Point({self.x}, {self.y})'


liczba = int('5')
liczba2 = int('6')

p1 = Point(1, 1)
p2 = Point(-5, 2)

p3 = p1 + p2
print(p3)



# # wyrażenia generujące
# # litery = (litera for litera in "Zdzisław")
# # print(litery)
# # print(next(litery))

# kody = ('A'*n for n in range(1000))
# print(kody)
# print(next(kody))
# print(next(kody))

# class Parzyste:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
 
#     def __iter__(self):
#         return self
 
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         if self.index % 2 == 0 :
#             value = self.data[self.index]
#             self.index += 2
#             return value

 
 
# moj_iterator = Parzyste("Ala ma kota")
# # print(moj_iterator)
# for element in moj_iterator:
#     print(element)