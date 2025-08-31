# Write a program to count vowels and consonants in a string.
vowels='aeiouAEIOU'
vowel=0
consonant=0
name=input("Enter string ")
for i in name:
   if i in vowels:
     vowel+= 1
   else: consonant+= 1
print(name , "contains", consonant ,"consonants and ", vowel, "vowels" )