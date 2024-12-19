class Dog:
    
    species = "Canis Familaris"
    
    def _init_(self, name, age):
        
        self.name = name
        self.age = age
        
        def bark(self):
            return f"{self.name} says woof!"
        
               
dog1 = Dog("Buddy", 5)
dog2 = Dog("Lucy", 3)

print(dog1.name)
print(dog2.age)

print(dog1.bark())
        