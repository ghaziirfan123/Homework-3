# My name is Mohammad Ghazi Irfan and my ID is 1626488

# Reads input from user
words = input()
# Split the given words list by space and store as a list
wordsList = words.split()
# Loop runs till the length of wordsList
for i in range(len(wordsList)):
    # wordsList.count(wordsList[i]) will returns the count of the given word in the list
    # Printing output with word and count
    print(wordsList[i], wordsList.count(wordsList[i]))
