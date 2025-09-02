# Impor modul-modul yang dibutuhkan
from game.Level import start, over
from game.Level.load import load_level
from game.Sound import play,pause,load
from game.Image.open import open_image
from game.Image import close,change

print(f"{"-"*10}Package Sound{"-"*10}")
load.load_music()
play.play_music()
pause.pause_music()
print()
print(f"{"-"*10}Package Image{"-"*10}")
open_image()
change.change_image()
close.close_image()
print()
print(f"{"-"*10}Package Level{"-"*10}")
start.start_level()
load_level()
over.over_level()
