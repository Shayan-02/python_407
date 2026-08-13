employees = {
    "emp1" : {
        "name" : {
            "fname" : "ali",
            "lname" : "ahmadi"
        },
        "age" : 30,
        "tel" : {
            "phone" : "02177163338",
            "tel" : "0987654321"
        },
        "job" : ["accountant", "snapp"],
        "taahol" : True,
        "birth" : "1375/10/03",
        "avg" : 18.5,
        "pID" : "0200000000"
    },
    "emp2" : {
            "name" : {
                "fname" : "reza",
                "lname" : "akbari"
            },
            "age" : 40,
            "tel" : {
                "phone" : "09874321",
                "tel" : "123455665645"
            },
            "job" : "computer engineer",
            "taahol" : False,
            "birth" : "1365/10/03",
            "avg" : 16.5,
            "pID" : "032234235234"
    }
}


for i in employees.items():
    print(i)