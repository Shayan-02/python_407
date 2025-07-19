import pandas as pd

employee = {
    "ali_amini" : {
        "name" : "ali amini",
        "age" : 24,
        "pID" : "0987654321",
        "tel" : "98765456"
    },
    "reza_kaviani" : {
        "name" : {
            "fname" : "reza",
            "lname" : "kaviani"},
        "age" : 30,
        "pID" : "1234567800",
        "tel" : {
            "mobile" : "09123456789",
            "phone" : {
                "home" : "098765432",
                "work" : "987654345"
            }
        }
    }
}

print(employee["reza_kaviani"]["tel"]["phone"]["work"])
print(employee)

df = pd.DataFrame(employee)
print(df)