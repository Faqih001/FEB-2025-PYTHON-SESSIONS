# Step 1: Read from an existing file
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 2: Modify the content (e.g., reverse every line)
modified_content = "\n".join(line[::-1] for line in content.splitlines())

# Step 3: Write the modified content to a new file
with open("modified_output.txt", "w") as outfile:
    outfile.write(modified_content)

print("✅ Modified file 'modified_output.txt' created successfully!")
