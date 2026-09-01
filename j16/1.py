# f = open("./2.txt", encoding="utf-8")

# print(f.read())
# print(f.readline())
# print(f.readlines())

# f.close()

# with open("1.txt", mode="w", encoding="utf-8") as f:
#     f.write("خوبی")

# with open("1.txt", mode="a", encoding="utf-8") as f:
#     f.write("\nخوبی")


with open("2.txt", mode="x", encoding="utf-8") as f:
    f.write("خوبی")
