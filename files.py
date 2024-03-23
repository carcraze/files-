def create_file():
    try:
        # Create a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("I'm ambitious \n")
            file.write("i'm happy \n")
            file.write("i hope to become a millionare\n")
        print("File created successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File creation process completed.")


def read_file():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())  # Strip newline characters
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File reading process completed.")


def append_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("Fourth line\n")
            file.write("Fifth line\n")
            file.write("Sixth line\n")
        print("File appended successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File appending process completed.")


if __name__ == "__main__":
    create_file()
    print()  # Print an empty line for separation
    read_file()
    print()  # Print an empty line for separation
    append_file()
