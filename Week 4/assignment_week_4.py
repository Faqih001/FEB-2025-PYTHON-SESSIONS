# Step 1: Read from an existing file
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 2: Modify the content (e.g., reverse every line)
modified_content = "\n".join(line[::-1] for line in content.splitlines())

# Step 3: Write the modified content to a new file
with open("modified_output.txt", "w") as outfile:
    outfile.write(modified_content)

print("✅ Modified file 'modified_output.txt' created successfully!")

try:
    filename = input("Enter the name of the file to read: ")
    with open(filename, "r") as file:
        data = file.read()
        print("\n📄 File content:")
        print(data)
except FileNotFoundError:
    print("❌ Error: File not found.")
except PermissionError:
    print("❌ Error: You don't have permission to read this file.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
