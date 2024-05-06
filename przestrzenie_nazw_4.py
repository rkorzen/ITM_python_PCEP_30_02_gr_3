
a = 1  # globalne a z pkt widzenia foo

def foo():
    
    def bar():
        global a
        a = 2  # lokalne a z pkt widzenia foo
        print(a)

    bar()
    
foo()
print(a)
# print(b)
