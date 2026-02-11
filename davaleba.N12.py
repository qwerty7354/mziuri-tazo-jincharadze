# #1
# while True:
#     try:
#         a = float(input("sheiyvane pirveli ricxvi: "))
#         b = float(input("sheiyvane meore ricxvi: "))
#         result = a / b
#         print("shedegi:", result)
#         break
#     except ValueError:
#         print("shecdoma: sheiyvane ricxvi!!!")
#     except ZeroDivisionError:
#         print("shecdoma: nulze gayofa ar sheileba!!!")
# #2
# def divide_numbers(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         return ("nulze gayofa ar sheileba!!!")
#     except TypeError:
#         return "araswori monacemebi"
#
# print(divide_numbers(10, 2))
# print(divide_numbers(5, 0))
# #3
# try:
#     lst = [1, 2, 3]
#     i = int(input("sheiyvane indexi: "))
#     print("elementi:", lst[i])
# except IndexError:
#     print("shecdoma: aseti indexi araa!")
# except ValueError:
#     print("shecdoma: indexi unda iyos mteli ricxvi!")
# #4
# try:
#     f = open("myresult.txt", "r")
#     print(f.read())
#     f.close()
# except FileNotFoundError:
#     print("secdoma: myresult.txt ar arsebobs!")
# #5
# import math
#
# try:
#     a = float(input("a = "))
#     b = float(input("b = "))
#     c = float(input("c = "))
#
#     if a == 0:
#         raise ValueError("a ar unda iyos 0")
#
#     D = b**2 - 4*a*c
#
#     if D < 0:
#         raise ValueError("uaryopiti diskriminanti — ar arsebobs")
#
#     x1 = (-b + math.sqrt(D)) / (2*a)
#     x2 = (-b - math.sqrt(D)) / (2*a)
#
#     print("pesvebi:", x1, x2)
#
# except ValueError as e:
#     print("shecdoma:", e)
# #6
# try:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     c = int(input("c = "))
#
#     if a + b <= c or a + c <= b or b + c <= a:
#         raise ValueError("es ciprebi samkutxedi samkutxeds ver gaaketeben!")
#
#     avg = (a + b + c) / 3
#     print("sash. aritmetikuli:", avg)
#
# except ValueError as e:
#     print("shecdoma:", e)
