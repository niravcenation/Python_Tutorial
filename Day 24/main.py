# First way to open file & in this we have to close the file that we have opened

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Second way to open file & in this we don't need to close the file
# read only mode

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# write mode

with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
