
a = 1  # globalne a z pkt widzenia foo

def foo():
    a = 2  # lokalne a z pkt widzenia foo
    b = 3
    print(a)

    
foo()
print(a)
# print(b)
