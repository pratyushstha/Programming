class Animal : 
    def speak(self) : 
        print("Animal makes a sound")
class Dog(Animal) : 
    def speak(self) : 
        print("Dog barks")
        # super().speak() If Animal had to be called too
d1 = Dog()
d1.speak()