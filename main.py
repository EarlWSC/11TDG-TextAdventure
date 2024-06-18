import random
import time
# Multiquestion Formats
QFORMAT_2 = "{}\nA. {} B. {} \nDecision Here: "
QFORMAT_3 = "{}\nA. {} B. {} C. {}\nDecision Here: "
QFORMAT_4 = "{}\nA. {} B.{} C. {} D. {}\nDecision Here: "

# Prompts/ Questions/ Outcomes/ Endings
INTRO_PROMPTS = ["Do you have what it takes to survive?",
                 #1
                 "Would you like a tutorial on how to play Survival of The Isle before you are left to die?",
                 #2 
                 "The decisions will be given out like this.\n",
                 #3
                 "It can either be 2, 3 or 4 decisions like so. Do you understand?",
                 #4 
                 "When given a prompt like this with no questions, it will wait for you to press ENTER key. Please do that now.",
                 #5
                 "To select an answer, a word or a sentence will be in CAPITAL letters to indicate the possible answers.",]

PROMPTS_1 = ["You survived a plane crash, and was washed ashore on an island with an inflatable raft. You decide whether to stay in the raft or explore. Do you...",
             #1 
             "You decide to explore the island for whatever can help you temporarily. You suddenly stumble upon an array of small wooden houses. Do you...",
             #2
             "After that, you managed to stumble upon an abandoned lighthouse after trekking for a while. Do you...",
             #3
             "You decide to remain in the boat. Now you're starting to become hungry. Do you...",
             #4
             "You decide to wait out for longer. It is getting dark. Do you...",
             #5
             "You're starting to suffer from starvation. Do you...",
             #6
             "You decide to find food. Do you...",]

PROMPTS_2 = ["You decide to either continue on the forest, or the houses, or the lighthouse. Do you...",
             #1
             "You decide to sleep since its become dark again. You then managed to wake up in the middle of the night. Do you...", 
             #2
             "Suddenly, you hear a weird noise as you see a pair of white eyes staring at you. You decide whether to run off or get a weapon. Do you...",
             #3
             "You decide fight it. Do you aim for its head or its body?",
             #4
             "You decide to run off. You managed to evade whatever that thing is. Do you go to the houses or the forest?",
             #5
             "You're currently on the run. Do you plan to hide under the bushes or behind a tree?",
             #6
             "You decide whether to fix the plane with the tools and supplies you have, or head back to the lighthouse",]

OUTCOMES = ["You decide to scavenge through the houses for some supplies.",
            #1
            "You decide to keep walking instead.",
            #2
            "You decide to head back to the boat.",
            #3
            "You decide to get a coconut from a tree.",
            #4
            "You decide to look for something else.",
            #5
            "You decide to stay in the lighthouse.",
            #6
            "You decide to go somewhere else until you find a palm tree.",
            #7
            "You decide to go back towards the houses.",
            #8
            "You decide to sleep since its become dark again.",
            #9
            "You wake up the next day.",
            #10
            "You wake up the next day. And decide to go exploring.",
            #11
            "You wake up the next day. You decide to go to the forest",
            #12
            "You see a dense forest throughout your way.",
            #13
            "You realize you're hungry and you need food",]

OUTCOMES_2 = ["You realize that you do not have suffiecient items, so you decide to go back to the houses to look for something.",
              #1
              "You have the items, but you decide to fix it later since you want to go exploring first.",
              #2
              "You hear rustling in the bushes. It may be something you can eat.",
              #3
              "You have to hunt down a pig!",
              #4
              "You have to hunt down a wolf!",
              #5
              "You have to hunt down an...anomaly?",
              #6
              "You try to fight it in order to get the upper hand.",
              #7
              "You failed to capture! You lost some hp but you still have a chance to try again!",
              #8
              "You managed to finally succeed! You have food now.",
              #9
              "You decide to go back to the lighthouse.",
              #10
              "You decide to continue to the forest.",
              #11
              "You decide to go towards the houses by the beach.",]
            

OUTCOMES_3 = ["You decide to sleep since its become dark again.",
              #
              "You decide to not to use to lighthouse and try to explore for more.",
              #
              "You decide to continue sleeping and not fix the lighthouse.",
              #
              "You manage to find an abandoned plane after exploring for a while.",
              #
              "You wake up and decide to go exploring again.",
              #
              "As you were exiting, you hear footsteps outside.",
              #
              "You manage to find another beach upon exiting the forest. You also find a boathouse.",]

ENDINGS = ["You have died from starvation. Game Over.",
          #1
          "You failed to capture as you slowly die of hunger. Game Over.",
          #
          "You managed to pace towards the houses, but suddenly, you feel extremely tired as you turn around and see the thing getting closer. Game Over",
          #
          "You managed to pace towards the houses, but suddenly, you feel extremely tired as you turn around and see the thing getting closer. Game Over",
          #
          "You managed to put up a fight against it, but suddenly, you feel something stab deep in your chest. Game Over",
          #
          "You have managed to fix the plane as the sun begins to rise. You successfully take off as you fly away. You've unlocked the best ending.",
          #
          "You see what appears to be a group of guards aiming rifles at you. Where did they come from? Game Over",]

Q_INTRO = [["Yes","No","Dunno"],
           #1
           ["Example 1","Example 2","Example 3","Example 4"],
           #
           ["In this case, YES proceeds.","You'd say NO if you're confident you're not sure.","if you're not too sure, then you DUNNO right?"]
           ]
Q_SHIPWRECK = [["STAY on the Ship and wait to be rescued...", "Leave and EXPLORE into the unknown and potentially deadly island..."],
               #1
             ["WAIT LONGER, I hope we get rescued very soon...", "Let's LOOK FOR FOOD, I'm starving..."],
             #
             ]
Q_BEACH_CAVE = []
Q_LIGHTHOUSE = []

# Available Answers
INTRO_ANS = [["yes", "no", "dunno"]]
SHIPWRECK_ANS =  [["stay", "explore"],
              ["wait longer", "look for food"]]
BEACH_CAVE_ANS = [["go back", "explore", "scavenge"]]
LIGHTHOUSE_ANS = [["explore", "stay"]]
S_OPTIONS = [["a", "b"],
             ["a", "b", "c"],
             ["a", "b", "c", "d"]]

# Functions
run = "no"
running_level = 1
Health = 5

# _ INTRO _
# INTRO
#  _ INTRO _ 
# INTRO
#  _ INTRO _ 
# INTRO
#  _ INTRO _ 
print("Welcome to our game:")
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
confidence = input(QFORMAT_3.format(INTRO_PROMPTS[0],Q_INTRO[0][0],Q_INTRO[0][1],Q_INTRO[0][2])).lower()
if confidence == INTRO_ANS[0][0]:
    input("Well well... \nYour decisions will be put to the test... (PRESS ENTER TO CONTINUE)")
elif confidence == INTRO_ANS[0][1]:
    input("Haha! You're a fool for playing... \nYou will face certain death, I'm sure... (PRESS ENTER TO CONTINUE)")
elif confidence == INTRO_ANS[0][2]:
    input("Ha! You're not so sure huh... \nYou're going to die here, I know of that now...(PRESS ENTER TO CONTINUE)")

tutorial = input(QFORMAT_2.format(INTRO_PROMPTS[1],Q_INTRO[0][0],Q_INTRO[0][1])).lower()
if tutorial == INTRO_ANS[0][0]:
    input("\nGood choice... Here's how it will work. (PRESS ENTER TO CONTINUE)")
    run = "Yes".lower()
elif tutorial ==INTRO_ANS[0][1]:
    input("\nWow.. I must say, you're brave..\nGood luck on survivng, you will need it. (PRESS ENTER TO CONTINUE)")

while run == "Yes".lower():
  input("Your objective of the game is to survive and escape an island.. You are unaware of your surroundings and have different choices to make. (PRESS ENTER TO CONTINUE)\n")
  print(QFORMAT_4.format(INTRO_PROMPTS[2],Q_INTRO[1][0],Q_INTRO[1][1],Q_INTRO[1][2],Q_INTRO[1][3]))
  understand = input(QFORMAT_3.format(INTRO_PROMPTS[3],Q_INTRO[0][0],Q_INTRO[0][1],Q_INTRO[0][2])).lower()
  if understand == INTRO_ANS[0][0]:
    input("Wonderful, you may be alive by the end of the night, but I cannot guarantee your survival. (PRESS ENTER TO CONTINUE)")
  elif understand == INTRO_ANS[0][1]:
    input("Wow.. such easy instructions and you fail to understand?\n Let's try that again... (PRESS ENTER TO CONTINUE)")
    continue
  elif understand == INTRO_ANS[0][2]:
    input("Ha! You're not so sure huh... \nYou're going to die here, I know of that now...\n I will give you the instructions one more time...\n (PRESS ENTER TO CONTINUE)")
    continue


  input("So,{}".format(INTRO_PROMPTS[4]))
  understand = input(QFORMAT_3.format(INTRO_PROMPTS[5],Q_INTRO[2][0],Q_INTRO[2][1],Q_INTRO[2][2]))
  if understand == INTRO_ANS[0][0]:
    input("Wonderful, you may be alive by the end of the night, but I cannot guarantee your survival. ")
  elif understand == INTRO_ANS[0][1]:
    input("Wow.. such easy instructions and you fail to understand?\n Let's try that again... (PRESS ENTER TO CONTINUE)")
    continue
  elif understand == INTRO_ANS[0][2]:
    input("Ha! You're not so sure huh... \nYou're going to die here, I know of that now...\n I will give you the instructions one more time...\n (PRESS ENTER TO CONTINUE)")
    continue
  

# SHIPWRECK PHASE

# BEACH CAVE PHASE

# LIGHTHOUSE PHASE


