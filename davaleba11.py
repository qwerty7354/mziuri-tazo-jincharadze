#1
# with open("ricxvebi.txt", "r") as f:
#     lines = f.readlines()
#
# with open("ricxvebi.txt", "w") as f:
#     for line in lines:
#         number = int(line.strip())
#         square = number ** 2
#         f.write(str(square) + "\n")
#         print(square)

#2
# with open("oscars.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#
# year = input("sheiyvane weli: ")
#
# print(f"\noskarosnebi {year} wels:")
# found = False
#
# for line in lines:
#     data = line.strip().split(",")
#     if data[0] == year:
#         print(data[3])
#         found = True
#
# if not found:
#     print("eror 404 this year not found🥺")
#
#
# youngest_age = 200
# youngest_name = ""
# youngest_age_value = 0
#
# for line in lines:
#     data = line.strip().split(",")
#     age = int(data[2])
#
#     if age < youngest_age:
#         youngest_age = age
#         youngest_name = data[3]
#         youngest_age_value = age
#
# print("\nyvelaze axalgazrda oskarosani!:")
# print(youngest_name, "-", youngest_age_value, "wlis!!!")
