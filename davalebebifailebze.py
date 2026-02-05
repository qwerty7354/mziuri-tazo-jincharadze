# #1
# with open("paili.txt", "a") as f:
#     f.write("random text")
# #2
# file = open("paili2.txt", "r")
# content = file.read()
# file.close()
# print(content)
# print("Number of characters:", len(content))
# #3
# file = open("paili2.txt", "a", encoding="utf-8")
# file.write("\nდამატებული ქართული ტექსტი")
# file.close()
# #4
# source = open("paili2.txt", "r")
# destination = open("copy.txt", "w")
#
# destination.write(source.read())
#
# source.close()
# destination.close()
# #5
#
# #6
# file = open("paili2.txt", "r")
# content = file.read()
# file.close()
#
# print(content.upper())
#
# #7
# file = open("data.txt", "w")
#
# while True:
#     text = input("Enter text (0 to finish): ")
#     if text == "0":
#         break
#     file.write(text + "\n")
#
# file.close()
#
# #8
# source = open("paili2.txt", "r")
# destination = open("paili3.txt", "w")
#
# lines = source.readlines()
# one_line = " ".join(line.strip() for line in lines)
#
# destination.write(one_line)
#
# source.close()
# destination.close()

