import random
import time
# Dictionary
QFORMAT_2 = "{}\nA. {}\nB. {}\nDecision Here:"
QFORMAT_3 = "{}\nA. {}\nB. {}\nC. {}\nDecision Here:"
QFORMAT_4 = "{}\nA. {}\nB.{}\nC. {}\nD. {}\nDecision Here:"

# Prompts/ Questions
INTRO_PROMPTS = ["Welcome! Do you have what it takes to survive? "]

PROMPTS_1 = ["You survived a plane crash, and was washed ashore on an island with an inflatable raft. You decide whether to stay in the raft or explore. Do you...",
             "You decide to explore the island for whatever can help you temporarily. You suddenly stumble upon an array of small wooden houses. Do you...",
             "After that, you managed to stumble upon an abandoned lighthouse after trekking for a while. Do you...",
             "You decide to remain in the boat. Now you're starting to become hungry. Do you...",
             "You decide to wait out for longer. It is getting dark. Do you...",
             "You're starting to suffer from starvation. Do you...",
             "You decide to find food. Do you...",]

PROMPTS_2 = ["You decide to either continue on the forest, or the houses, or the lighthouse. Do you...",
             "You decide to sleep since its become dark again. You then managed to wake up in the middle of the night. Do you...",
             "Suddenly, you hear a weird noise as you see a pair of white eyes staring at you. You decide whether to run off or get a weapon. Do you...",
             "You decide fight it. Do you aim for its head or its body?",
             "You decide to run off. You managed to evade whatever that thing is. Do you go to the houses or the forest?",
             "You're currently on the run. Do you plan to hide under the bushes or behind a tree?",]

OUTCOMES =[""]

ENDINGS =[""]

Q_INTRO = [["Yes","No","Dunno"]]
Q_SHIPWRECK = [["STAY on the Ship and wait to be rescued...", "Leave and EXPLORE into the unknown and potentially deadly island..."],
             ["WAIT LONGER, I hope we get rescued very soon...", "Let's LOOK FOR FOOD, I'm starving..."]]
Q_BEACH_CAVE = []
Q_LIGHTHOUSE = []

# Available Answers
INTRO_ANS = ["yes", "no"]
SHIPWRECK_ANS =  [["stay", "explore"],
              ["wait longer", "look for food"]]
BEACH_CAVE_ANS = [["go back", "explore", "scavenge"]]
LIGHTHOUSE_ANS = [["explore", "stay"]]
S_OPTIONS = [["a", "b"],
             ["a", "b", "c"],
             ["a", "b", "c", "d"]]

# Functions
Health = 5

# IIIIIIIIINNNNNNNNNNNNNNNNNTTTTTTTTTTTTTTTTTRRRRRRRRRRRRRROOOOOOOOOOOOOOOOOOOOOOO
print("You are now playing,")
print(r"""  
  ██████  █    ██  ██▀███   ██▒   █▓ ██▓ ██▒   █▓ ▄▄▄       ██▓        ▒█████    █████▒   ▄▄▄█████▓ ██░ ██ ▓█████     ██▓  ██████  ██▓    ▓█████ 
▒██    ▒  ██  ▓██▒▓██ ▒ ██▒▓██░   █▒▓██▒▓██░   █▒▒████▄    ▓██▒       ▒██▒  ██▒▓██   ▒    ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██▒▒██    ▒ ▓██▒    ▓█   ▀ 
░ ▓██▄   ▓██  ▒██░▓██ ░▄█ ▒ ▓██  █▒░▒██▒ ▓██  █▒░▒██  ▀█▄  ▒██░       ▒██░  ██▒▒████ ░    ▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██▒░ ▓██▄   ▒██░    ▒███   
  ▒   ██▒▓▓█  ░██░▒██▀▀█▄    ▒██ █░░░██░  ▒██ █░░░██▄▄▄▄██ ▒██░       ▒██   ██░░▓█▒  ░    ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ░██░  ▒   ██▒▒██░    ▒▓█  ▄ 
▒██████▒▒▒▒█████▓ ░██▓ ▒██▒   ▒▀█░  ░██░   ▒▀█░   ▓█   ▓██▒░██████▒   ░ ████▓▒░░▒█░         ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░██░▒██████▒▒░██████▒░▒████▒
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░   ░ ▐░  ░▓     ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░   ░ ▒░▒░▒░  ▒ ░         ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░▓  ▒ ▒▓▒ ▒ ░░ ▒░▓  ░░░ ▒░ ░
░ ░▒  ░ ░░░▒░ ░ ░   ░▒ ░ ▒░   ░ ░░   ▒ ░   ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░     ░ ▒ ▒░  ░             ░     ▒ ░▒░ ░ ░ ░  ░    ▒ ░░ ░▒  ░ ░░ ░ ▒  ░ ░ ░  ░
░  ░  ░   ░░░ ░ ░   ░░   ░      ░░   ▒ ░     ░░    ░   ▒     ░ ░      ░ ░ ░ ▒   ░ ░         ░       ░  ░░ ░   ░       ▒ ░░  ░  ░    ░ ░      ░   
      ░     ░        ░           ░   ░        ░        ░  ░    ░  ░       ░ ░                       ░  ░  ░   ░  ░    ░        ░      ░  ░   ░  ░
                                ░            ░                                                                                                   """)
confidence = input("{}".format(INTRO_PROMPTS[0])).lower()
if confidence == INTRO_ANS[0]:
    print("Well well... We'll see about that!")
elif confidence == INTRO_ANS[1]:
    print("NIG")

# SHIPWRECK PHASE

# BEACH CAVE PHASE

# LIGHTHOUSE PHASE

