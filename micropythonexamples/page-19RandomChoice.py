import random
from microbit import *


names = ['Mary', 'Yolanda', 'Damien', 'Alia', 'Kushal', 'Mei Xiu', 'Zoltan']
choice = random.choice(names)
display.scroll(choice)
