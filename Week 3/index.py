# Function to check if base^exponent is greater than 5000
# If true, return True; otherwise, return False
def large_power(base, exponent):
    result = base ** exponent  # Calculate power
    if result > 5000:
        return True
    else:
        return False

# Test cases for large_power function
print(large_power(10, 3))  # False (10^3 = 1000)
print(large_power(5, 4))   # False (5^4 = 625)
print(large_power(20, 3))  # True (20^3 = 8000)


# Function to check if a number is divisible by 10
# If num % 10 == 0, return True; otherwise, return False
def divisible_by_ten(num):
    if num % 10 == 0:  # Check divisibility using modulus
        return True
    else:
        return False

# Test cases for divisible_by_ten function
print(divisible_by_ten(50))  # True
print(divisible_by_ten(23))  # False
print(divisible_by_ten(100)) # True
