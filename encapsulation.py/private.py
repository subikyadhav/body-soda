

class Parent:
    def __func1(self):
        print("This function is in parent class")

class Child(Parent):
    def __func2(self):
        print("This function is in child class")

object = Child()
object._Parent__func1()
object._Child__func2()