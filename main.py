# My name is Mohammad Ghazi Irfan and my ID ias 1626488

# empty dictionary
dic={}
#loop to accept 5 player's details
for i in range(5):
    #accepting jersey number
    num=int(input("Enter player's jersey number: "))
    #accepting rating
    rating=int(input("Enter player's rating: "))
    #adding the details to dictionary
    dic[num]=rating
#sorting the key's in dictionary
for i in sorted(dic):
    #printing key and value
    print(str(i)+" : "+str(dic[i]))

# the code gives the answer but i cannot figure out how to get the credit in zybooks