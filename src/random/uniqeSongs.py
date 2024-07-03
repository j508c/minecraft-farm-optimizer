# Open the file in read mode
with open('worshipMusic.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

# Remove any trailing newline characters
lines = [line.strip() for line in lines]

# Print the lines
for line in lines:
    print(line)