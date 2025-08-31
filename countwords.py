#Write a program to count the number of words in a text file
with open("input.txt", "r") as file:
    # Read the entire content of the file
    text = file.read()

# Split the text into words using whitespace as separator
words = text.split()

# Count the total number of words
word_count = len(words)

# Print the result
print("Total words:", word_count)