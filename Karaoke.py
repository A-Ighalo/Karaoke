import sys
import time 
from rich import print as rprint
from rich.console import Console
from time import sleep

console = Console()

lyrics = [
    'Oh', 
    '(Mad)',
    'Ooh',
    'Ooh',
    'Ooh',
    'Ooh',
    'Baby, the weather',
    'Is getting cold',
    'Cold inside',
    'Double sweater',
    'I am your own',
    'Ordinary',
    'Paranoid',
    "I can't picture this world, without you in my life, oh",
    "Baby",
    "Uhh-uhh-uhh, uh, uh, uh",
    "Uhh, uhh, uhh, uh, uh, uh",
    "Uhh-uhh-uhh, uh, uh, uh (My love, my love, my love)",
    "Uhh, uhh, uhh, uh, uh, uh (My love, my love, my love)",
    "Sweet Fanta Diallo, I no fit forget you o",
    "Ebezina, ebezina, Nsọgbu Sọọgbu o (Yeah)",
    "If I speak English, oh-oh",
    "Chọ-chọ-chọ, no workings",
    "I no wan punish you, whoa, whoa",
    "I want to polish you (Ìdí ará bànkó)",
    "If you see my baby, you go shut up, oh, (Ìdí ará bànkó)",
    "Ọmọge too fine, no be makeup, oh",
    "Ó ya baby, lie down, oh",
    "Finish work for me, oh",
    "Oh, Tomato, put that thing back, oh (Yeah)",
    "Ah, baby",
    "Uhh-uhh-uhh, uh, uh, uh",
    "Uhh, uhh, uhh, uh, uh, uh",
    "Baby, baby, baby",
    "Uhh-uhh-uhh, uh, uh, uh",
    "Uhh, uhh, uhh, uh, uh, uh",
    "Baby, baby, baby",
    "Oh, na, na",
    "Uhh-uhh-uhh, uh, uh, uh",
    "Uhh, uhh, uhh, uh, uh, uh",
    "My love, my love, my love",
    "Baby, oh"
    ]

colors = [
    "red", "blue", "green", "yellow", "magenta", "cyan", 
    "bright_red", "bright_blue", "bright_green", "bright_yellow", 
    "bright_magenta", "bright_cyan", "white", "bright_white"
]

for x,song in enumerate(lyrics):
    time.sleep(0.1)
    console.print(song, style = colors[x%len(colors)],soft_wrap=True)