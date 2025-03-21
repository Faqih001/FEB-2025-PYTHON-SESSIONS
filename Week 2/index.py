# Task 1: Sum of integers in a list
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
print("Sum of all integers:", sum(numbers))

# Task 2: Tuple of favorite books
favorite_books = ("1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby-Dick", "Pride and Prejudice")
print("\nFavorite Books:")
for book in favorite_books:
    print(book)

# Task 3: Dictionary with user info
person_info = {
    "name": input("\nEnter your name: "),
    "age": int(input("Enter your age: ")),
    "favorite_color": input("Enter your favorite color: ")
}
print("\nPerson Information:", person_info)

# Task 4: Common elements in two sets
set1 = set(map(int, input("\nEnter integers for the first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter integers for the second set separated by spaces: ").split()))
common_elements = set1 & set2
print("Common elements:", common_elements)

# Task 5: Words with odd number of characters
words = ["apple", "banana", "grape", "kiwi", "orange"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("\nWords with odd number of characters:", odd_length_words)
