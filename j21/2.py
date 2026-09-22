import datetime

now_time = datetime.datetime.now()
c_year = now_time.year
c_month = now_time.month
c_day = now_time.day

print(c_year)
print(c_month)
print(c_day)


birth = datetime.date(1999, 9, 22)

birth_month = birth.month
birth_day = birth.day

birth_date = str(birth_month)+ "-"+ str(birth_day)
print(birth_date)

corent_year_date = str(now_time.month) + "-"+ str(now_time.day)

if corent_year_date == birth_date:
    print("happy birthday")

if birth_month < 10:
    print(f"0{birth_month}")
else:
    print(birth_month)