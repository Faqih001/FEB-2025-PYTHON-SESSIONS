# Step 1: Create the input.txt file with 5+ lines of text
with open("input.txt", "w") as infile:
    infile.write("Hello there!\n")
    infile.write("This is a test file.\n")
    infile.write("It contains multiple lines.\n")
    infile.write("Each line has some words.\n")
    infile.write("Let's count them all.\n")

# Step 2: Read the contents of input.txt
with open("input.txt", "r") as infile:
    contents = infile.read()

# Step 3: Count the number of words
word_count = len(contents.split())

# Step 4: Convert text to uppercase
uppercase_contents = contents.upper()

# Step 5: Write processed text and word count to output.txt
with open("output.txt", "w") as outfile:
    outfile.write("PROCESSED TEXT:\n")
    outfile.write(uppercase_contents)
    outfile.write(f"\n\nWORD COUNT: {word_count}\n")

# Step 6: Print success message
print("✅ output.txt has been created successfully with processed content.")
