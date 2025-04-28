try:
    with open("example.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The file was not found. Please check the file name and path.")
except IOError:
    print("An error occurred while reading the file.")
finally:
    print("Execution completed.")
    file.close()
# The above code attempts to open a file named "nonexistent.txt" in read mode. If the file does not exist, it catches the FileNotFoundError and prints a message indicating that the file was not found. If any other I/O error occurs, it catches the IOError and prints a different message. Finally, it prints "Execution completed." regardless of whether an error occurred or not.