a = input("enter a word: ")

valid = []

# l = [1, 2, 3, 4, 5]
# l.append(6)
# l.insert(2, "ali")
invalid = ["a", "i", "u", "o", "e"]
for i in a:
    if i in invalid:
        continue
    # if i not in invalid:
    else:
        valid.append(i)

for i in valid:
    print(i, end="")