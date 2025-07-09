# Counts the number of vowels in a user-entered sentence
a = input("Enter a sentence : ")
count = 0; 
for i in a : 
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"): 
        count = count + 1
print("The number of vowels in the given sentence is :", count)