# Open the file in read mode
with open('example.txt', 'r') as file:
    content = file.read()

# Print the content of the file
print(content)

with open("output.txt", "w") as file:
    file.write("Hello, Love!")
    file.write("\nHello Peace.")
    file.write("\nHello Joy, Its a new horizon!")

    