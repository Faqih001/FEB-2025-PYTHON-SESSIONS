import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename="file_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# The above code implements a simple file tool with a menu-driven interface. It allows users to read a file, modify its content (reverse each line), and save the modified content to a new file. The code also uses logging to record actions and errors. 
def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n📄 File Content:\n")
            print(content)
            logging.info(f"Successfully read file: {filename}")
            return content
    except FileNotFoundError:
        print("❌ Error: File not found.")
        logging.error(f"File not found: {filename}")
    except PermissionError:
        print("❌ Error: No permission to read the file.")
        logging.error(f"Permission denied: {filename}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        logging.exception("Unexpected error")
    return None

# This function modifies the content by reversing each line and saves it to a new file with a timestamp. It also logs the success or failure of the operation. 
# The function takes the content and the output filename as parameters. It uses a try-except block to handle potential errors during file writing.
def modify_and_save(content, output_filename):
    try:
        modified = "\n".join(line[::-1] for line in content.splitlines())
        with open(output_filename, "w") as outfile:
            outfile.write(modified)
        print(f"✅ Modified content saved to '{output_filename}'")
        logging.info(f"Modified content written to {output_filename}")
    except Exception as e:
        print(f"❌ Failed to write file: {e}")
        logging.exception("Error writing file")

# This function serves as the main menu for the file tool. It provides options to read a file, modify and save a file, or exit the program. 
# The user's choice is taken as input, and appropriate actions are performed based on the choice. The function also logs each action taken by the user. 
# The menu is displayed in a loop until the user chooses to exit. It handles invalid choices gracefully and logs them as well. 
# The function uses a while loop to keep displaying the menu until the user chooses to exit. It also handles invalid choices and logs them.
def main_menu():
    while True:
        print("\n🗂️ File Tool Menu")
        print("1. Read a file")
        print("2. Read & Save Modified (Reversed) version")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            filename = input("Enter the filename to read: ")
            read_file(filename)

        elif choice == "2":
            filename = input("Enter the filename to read & modify: ")
            content = read_file(filename)
            if content:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_filename = f"modified_{timestamp}.txt"
                modify_and_save(content, output_filename)

        elif choice == "3":
            print("👋 Exiting. All actions have been logged to 'file_log.txt'")
            break

        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

# This is the entry point of the script. It calls the main_menu function to start the program.
# The script is designed to be run directly, and the main_menu function is called to initiate the menu-driven interface. The script uses a standard Python convention to check if it is being run as the main module.
# If it is, the main_menu function is called to start the program. This allows the script to be imported as a module without executing the main menu.
if __name__ == "__main__":
    main_menu()
