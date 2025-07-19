# start = int(input("start: "))
# end = int(input("end: "))
# lst = []

# for _ in range(start, end+1):
#     if _ % 2 == 0:
#         lst.append(_)

# for _ in lst:
#     print(_, end=" ")

# num = int(input("enter a number: "))
# print("even" if num % 2 == 0 else "odd")

start = int(input("start: "))
end = int(input("end: "))
lst = [_ for _ in range(start, end+1) if _ % 2 == 0]

for _ in lst:
    print(_, end=" ")