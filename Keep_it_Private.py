class Stuff_to_keep_private:

    __privateVar = 27

    def __privateMethod(self):
        print("I'm inside the class")

    def hello(self):
        print("Private Variabl value", Stuff_to_keep_private.__privateVar)

foo = Stuff_to_keep_private()
foo.hello()
foo.__privateMethod

