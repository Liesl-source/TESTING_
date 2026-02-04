class myClass:

    # private variable
    __privateVar = 27;

    # private method
    def __privMeth(self):
        print("I'm inside class myClass")

    
    def hello(self):
        print("Private Variable value: ", myClass.__privateVar)


foo = myClass()
foo.hello()
foo.__privMeth