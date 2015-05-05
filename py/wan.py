def getfib():
    fib_1 = 0
    fib_2 = 1
    while True:
        next = fib_1 + fib_2
        yield next
        fib_1 = fib_2
        fib_2 = next

foo = getfib()
for n in foo:
    print n,"\n"
raw_input()

