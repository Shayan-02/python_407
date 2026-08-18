def game(number):
    yekan = number % 10
    dahgan = number // 10
    # if yekan > dahgan:
    #     return yekan - dahgan
    # else:
    #     return dahgan - yekan
    result = yekan - dahgan
    if result >= 0:
        return result
    else:
        return result * -1

