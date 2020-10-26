import time
from colorama import init, Fore, Back, Style
import playsound
a = 'Half-Life 3 has been announced, but it will be exclusive to EPIC GAME STORE'

for i in a[:60]:
    print(Back.LIGHTBLACK_EX + Fore.RED + i, end='')
    time.sleep(0.1)
b = 'D:/Music/lamborgini.wav'
for z in a[60:]:
    print(Fore.CYAN + z, end="")
    time.sleep(0.3)
playsound.playsound(b)


