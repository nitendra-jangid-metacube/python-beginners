def foo():
    print("foo Called")
    def bar():
        print("bar Called")
    bar()
    
foo()