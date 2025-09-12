# Example of Dynamic Polymorphism in Python

class Bird():
    def speak(self):
        return "Chirp!"
    
class Dog():
    def speak(self):
        return "Woof!"
    
class Cat():
    def speak(self):
        return "Meow!"  
    
def animal_sound(animal):
    print(animal.speak())   

if __name__ == "__main__":
    animal_sound(Dog())
    animal_sound(Cat())
    animal_sound(Bird())
