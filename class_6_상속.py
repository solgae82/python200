class Person:
    def greet(self):
        return "Hello"

class User(Person):
    def greet(self):
        return super().greet() + " User"
    

u = User()
print(u.greet())  # Hello User

"""
✔ extends 없음
✔ super() 동일
"""