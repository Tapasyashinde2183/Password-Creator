import string
import random

# Store all the char in lists.
S1 = list(string.ascii_lowercase)
S2 = list(string.ascii_uppercase)
S3 = list(string.digits)
S4 = list(string.punctuation)

# Ask user about the number of characters
user_input = input("Enter the  length of Password :  ") 

# Check this input is it number ? is it more then 8?
while True:
    try:
        characters_number = int(user_input)
        if characters_number < 8:
            print("Your number should be atleast 8")
            user_input = input("Please, Enter your number again : ")
        else:

            break

    except:
        print("Please, Enter number only.")
        user_input = input("How many characters do you want in Password ? ")
# Shuffle all lists
random.shuffle(S1)
random.shuffle(S2)
random.shuffle(S3)
random.shuffle(S4)        

# Calculate 30% & 20% of numbers of characters

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

# Generation of password (60% letters and 40% digits & punctuations)
results = []

for x in range(part1):
    results.append(S1[x])
    results.append(S2[x])
for x in range(part2):
    results.append(S3[x])
    results.append(S4[x])   

    # Shuffle result
random.shuffle(results)  

# Join result
password ="" .join(results)
print("Strong Password :",password)
