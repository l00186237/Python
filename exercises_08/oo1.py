class JORzClass():
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for JORzClass")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)

# Creating an instance of JORzClass named my_class1
my_class1 = JORzClass("Morning JOR!")
my_class1.my_method()
print(type(my_class1))

# Adding another class named my_class2
class JDClass():
    # Constructor for my_class2
    def __init__(self, another_message):
        print("Running constructor for JDClass")
        self.another_message = another_message

    def another_method(self):
        print(self.another_message)

# Creating an instance of JDClass named my_class2
my_class2 = JDClass("Good evening!")
my_class2.another_method()
print(type(my_class2))
