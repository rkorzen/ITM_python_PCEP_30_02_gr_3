
a = 1

def foo():
    def bar():
        print(a)
    bar()
    
foo()
