
a = 1  # globalne a z pkt widzenia foo

def foo():
    b = 2
    
    def bar():
        global b
        b = 4  # lokalne a z pkt widzenia foo
        print(b, "z bar")
    

    bar()
    print(b, "z foo")
    
foo()
