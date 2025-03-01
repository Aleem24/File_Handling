# Open file and storing object in a variable

file = open("demo.txt","r")

# Reading the contents of the file
print(file.read())

# Close the file

file.close()
# Opening a file in write mode
file_w = open("demo.txt", "w")
file_w.write("Today is the first day of Taraweeh.")
file_w.close()


# Opening a file in append mode

file_append = open("demo.txt","a")
file_append.write(f"Tomorrow we will make the first sahoor of Ramadan.{"\n"}Ramadan is the month of perseverence.{"\n"}We should not be intolerable and respectful to everyone.")
file.close()

file_line = open("demo.txt", "r")
counter = 0

# Reading from file
content = file_line.read()
# Splitting content into lines and sorting them in a list

content_list = content.split(".")

for i in content_list:
    if i:
        counter += 1

print(f"This is the number of lines in the file: {counter}")




