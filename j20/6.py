import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def sum_number():
    sumnumbers = 0
    for i in range(20_000_001):
        sumnumbers += i
    return sumnumbers

print(sum_number())