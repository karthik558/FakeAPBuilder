import random
import string

# get user input for length of strings and number of strings to generate
length = int(input("Enter the length of the strings: "))
num_strings = int(input("Enter the number of strings to generate: "))

# define the pool of characters to choose from
chars = string.ascii_lowercase + string.digits

# generate the specified number of random strings
for i in range(num_strings):
    # join a random selection of characters to create the string
    rand_string = ''.join(random.choices(chars, k=length))
    print(rand_string)