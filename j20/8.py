import time

# start_time = time.time()
# print(start_time)

def test(*a, **kw):
    return a


print(test({"a" : 1, "b" : 2, "c" : 3, "d" : 4}))