import random,alphabets
from colorama import Fore, Back, Style

for i in range(100000):
    Small_letters = alphabets.small()
    text = random.choice(Small_letters) 
    print(Fore.GREEN+Back.BLACK+text+Fore.RESET+Back.RESET,end='')

