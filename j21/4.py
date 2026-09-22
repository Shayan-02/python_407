def my_generator():
  for i in range(10):
    yield i


for value in my_generator():
  print(value)


def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(10_000_000)
print(next(gen))
print(next(gen))
print(next(gen))
