#Write a program to find the longest word in a given sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = ""
max_len= 0
for word in words:
    length = len(word)
    if length > max_len:
        max_len = length
        longest_word = word
print("The longest word is:", longest_word)