
class Alphabet():

    def __init__(self):
        print("Alphabet Initialised")

    def display(self):
        print("Display from Alphabet")


class Google(Alphabet):

    def __init__(self):
        print("Google initialised")

    def display(self):  # Overriding the display method
        print("Display from Google")

    def show(self):
        super().display()  # Call the parent class's display method
        self.display()  # Call the overridden display method



class Microsoft(Alphabet):

    def __init__(self):
        super().__init__() # Call the parent class's constructor
        print("Microsoft Initialised")

    def display(self):  # Overriding the display method
        print("Display from Microsoft")


if __name__ == "__main__":

    parent = Alphabet() # Alphabet Initialised
    parent.display() # Display from Alphabet

    child = Google() # Google initialised
    child.display() # Display from Google

    child.show() # Display from Alphabet, Display from Google
    

    child_microsoft = Microsoft()  # Alphabet Initialised, Microsoft Initialised
    child_microsoft.display()  # Display from Microsoft

"""
Explanation of Changes:
super() Usage:

Used in the Google and Microsoft constructors to call the parent class's constructor.
Used in the show method of Google to call the parent class's display method.
Method Overriding:

Both Google and Microsoft override the display method to provide their own implementation.
New Derived Class:

Added a new class Microsoft to demonstrate multiple derived classes inheriting from the same parent.
This demonstrates more advanced inheritance concepts and showcases how derived classes can interact with their parent class.
"""