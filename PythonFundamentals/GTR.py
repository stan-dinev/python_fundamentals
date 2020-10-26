import playsound
from random import shuffle

a = "D:/Music/m1.mp3"
b = "D:/Music/18. The Club Rules (Kilon Tek Remix 1).mp3"
c = "D:/Music/25. Power Curve (Segal Remix).mp3"
Playlist =[a, b, c]
shuffle(Playlist)
for i in Playlist:
    playsound.playsound(i)

