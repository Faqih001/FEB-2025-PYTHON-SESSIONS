# Assigning values to Variables in Python
site_name = "Power Learn Project"
print(site_name)

# Changing the Value of a Variable in Python
site_name = "Power Learn Project"
print(site_name)

# Assigning new value to site_name
site_name = "I love coding 😊"
print(site_name)

# Example: Assigning multiple values to multiple variables
a,b,c = 5, 7, "Hello world"
print(a) # prints 5
print(b) # prints 5
print(c) # prints Hello World

# Rules for Naming Python Variables
num = 55
Num = 510
print(num) #5
print(Num) #510

num1 = 55
num2 = 5.3
print(num1)
print(num2) 

# Python List Data Type
languages = ["Python", "Dart", "Web", 23]
print(languages)

# Access List Items
languages = ["Python", "Dart", "Web", 23]
print(languages[1])

#Python Tuple Data Type
products = ('XBox', 499.99, "Habibi", 23)
print(products)

# Access Tuple Items
products = ('XBox', 499.99, "Habibi", 23)
print(products[2])

# Python String Data Type
site_name = "Power Learn Project"
print(site_name)

# Python Set Data Type
student_ids = {112, 114, 117, 113}
print(student_ids)

# Python Dictionary Data Type
capital_city = {"Kenya": "Nairobi", "Nigeria": "Lagos"}
print(capital_city)

# Types of Python Operators
# Arithmetic Operators
num1 = 10
num2 = 5
print(num1 + num2) # Addition
print(num1 - num2) # Subtraction
print(num1 * num2) # Multiplication
print(num1 / num2) # Division
print(num1 % num2) # Modulus
print(num1 ** num2) # Exponentiation

# Comparison Operators
num1 = 10
num2 = 5
print(num1 == num2) # Equal
print(num1 != num2) # Not equal
print(num1 > num2) # Greater than
print(num1 < num2) # Less than
print(num1 >= num2) # Greater than or equal to
print(num1 <= num2) # Less than or equal to

# Logical Operators
num1 = 10
num2 = 5
print(num1 and num2) # Logical AND
print(num1 or num2) # Logical OR
print(not num1) # Logical NOT 

# Membership Operators
languages = ["Python", "Dart", "Web", 23]
print("Python" in languages) # Membership operator
print("Java" in languages) # Membership operator

# Identity Operators
num1 = 10
num2 = 10
print(num1 is num2) # Identity operator
print(num1 is not num2) # Identity operator

# Python Conditional Statements 
# If Statement
num = 10
if num > 0:
    print("Positive number")

# If-Else Statement
num = -5
if num > 0:
    print("Positive number")
else:
    print("Negative number")

# If-Elif-Else Statement
num = 0
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    
# Python Loops
# For Loop
for i in range(5):
    print(i)

# While Loop
i = 0
while i < 5:
    print(i)
    i += 1  # Increment i by 1

# Python Functions
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)

# Python Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("John", 30)
person.greet()

