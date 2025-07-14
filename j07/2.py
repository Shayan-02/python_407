word = input("enter a word: ")
x = input("ennter a char to change: ")
y = input("enter a char to replace: ")

replaced_word = ""

for i in word:
    if i == x:
        replaced_word += y
    else:
        replaced_word += i


print(replaced_word)