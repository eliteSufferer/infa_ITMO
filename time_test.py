import timeit
print("0-я программа: ", timeit.timeit("task0.main()", setup="import task0", number=100))
print("1-я программа: ", timeit.timeit("task1.main()", setup="import task1", number=100))
print("2-я программа: ", timeit.timeit("task2.main()", setup="import task2", number=100))