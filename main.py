import random
# Dictionary
QFORMAT_2 = "{}\n A. {} \n B. {} \n  Decision Here: "
QFORMAT_3 = "{}\n A. {} \n B. {} \n C. {} \n Decision Here: "
QFORMAT_4 = "{}\n A. {} \n B. {} \n C. {} \n D. {}\n Decision Here: "

SHIPWRECK = [["Stay on the Ship and wait to be rescued...", "Leave and Explore into the unknown and potentially deadly island..."],
             ["Wait longer, I hope we get rescued very soon...", "Leave to find food, I'm absolutely starving..."]]
BEACH_HUT = []
LIGHTHOUSE = []
SHIPWRECK_ANS =  [["Stay", "Explore"],
              ["Wait Longer", "Look for Food"]]
BEACH_HUT_ANS = [["Go Back", "Explore", "Scavenge"]]
LIGHTHOUSE_ANS = [["Explore", "Stay"]]

S_OPTIONS = [["a", "b"],
             ["a", "b", "c"],
             ["a", "b", "c", "d"]]

# Functions
health = 5
def intro():
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
print

# SHIPWRECK PHASE
intro()

print("You survived a plane crash, and was washed ashore on an island with an inflatable raft. You decide whether to stay in the raft or explore.")

answer = input("Welcome, do you have what it takes to survive?")

print(QFORMAT_2.format(SHIPWRECK[0][0],SHIPWRECK[0][1]))


answer = input()

if answer == SHIPWRECK_ANS[0][0]:
    print("fanum")
elif answer == SHIPWRECK_ANS[0][1]:
    print("skibidi")

# BEACH HUT PHASE

print("You decide to explore the island for whatever can help you temporarily. You suddenly stumble upon an array of small wooden houses. Do you...")

answer == input()

if answer == BEACH_HUT_ANS[0][0]:
  print("rizz")
elif answer == BEACH_HUT[0][1]:
  print("adin ross")
elif answer == BEACH_HUT[0][2]:
  print("grimace shake")

# LIGHTHOUSE PHASE

print("After that, you managed to stumble upon an abandoned lighthouse after trekking for a while. Do you...")

answer == input()
