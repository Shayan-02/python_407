rezaee = {
    "name" : "ali rezaee",
    "age" : 20,
    "tel" : ["0987654321", "1234567890"]
}

rezaee["pID"] = "0987654321"

# print(rezaee["name"]["lname"])
# print(rezaee["age"])
# print(rezaee["tel"])

for i in rezaee:
    print(i, "->", rezaee[i])