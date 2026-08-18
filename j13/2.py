def sum_numbers(*numbers: tuple) -> str:
    sumnumbers = 0
    minnumber = numbers[0]
    for i in range(len(numbers)):
        sumnumbers += numbers[i]
    for j in range(len(numbers)):
        if numbers[j] < minnumber:
            minnumber = numbers[j]
    return f"""
    sum of numbers : {sumnumbers}
min number : {minnumber}
"""


# call function
# for i in sum_numbers(10, 20):
#     print(i)

print(sum_numbers(10, 20).strip())
