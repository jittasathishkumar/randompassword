import random
from string import ascii_letters,punctuation,digits

result=ascii_letters+punctuation+digits
password=""

try:
    n=int(input("Enter any number:"))
    #print(random.choice(result))
    for i in range(n):
        result1=random.choice(result)
        password+=result1
    print(password)
except ValueError:
    print("invalid input")