import random
import time
# Multiquestion Formats
QFORMAT_2 = "{}\nA. {} B. {} \nDecision Here: "
QFORMAT_3 = "{}\nA. {} B. {} C. {}\nDecision Here: "
QFORMAT_4 = "{}\nA. {} B.{} C. {} D. {}\nDecision Here: "

# Prompts/ Questions/ Outcomes/ Endings
# Introduction and Tutorial
IntroPrompts = {
    "Welcome": ["Do you have what it takes to survive?", 
                "Would you like a tutorial on how to play Survival of The Isle before you are left to die?",
                "Let's get to it... Your Journey begins now (PRESS ENTER TO CONTINUE)"],              
    "Tutorial":["The decisions will be given out like this.\n",
               "It can either be 2, 3 or 4 decisions like so. Do you understand?",
               "When given a prompt like this with no questions, it will wait for you to press ENTER key. Please do that now.",
               "To select an answer, a word or a sentence will be in CAPITAL letters to indicate the possible answers."]     
}
Q_INTRO = [["Yes","No","Dunno"],
           ["Example 1","Example 2","Example 3","Example 4"],
           ["In this case, YES proceeds.","You'd say NO if you're confident you're not sure.","if you're not too sure, then you DUNNO right?"]
           ]
INTRO_ANS = ["yes", "no", "dunno"]
SHORT_OPTIONS = ["a", "b", "c", "d"]
# // MAIN GAME DICTIONARY \\
#Planewreck part; Stay or Explore?
Intro_Scenario = {
   "Planewreck": "\nYou survived a plane crash, and was washed ashore on an island with an inflatable raft.",
    "Decision": "\nYou decide whether to stay in the raft or explore. Do you...", 
    "Choices": ["STAY on the raft and wait to be rescued...", "Leave and EXPLORE into the unknown and potentially deadly island..."],
    "Answers": ["stay", "explore"],
    "Outcomes": ["You decided to stay and wait to be rescued... Time shall pass as you know it will take a while...", "You decide to leave and explore into the unknown and potentially deadly island..."],
}
#Found Beachcave and Stayed at Raft
#Go Back, Explore or Scavenge? || 
S1_Scenario_1 = {
   "BeachCave": "\nYou decide to explore the island for whatever can help you temporarily.",
   "BC_Decision": "\nYou suddenly stumble upon a large cave that seems to lead to somewhere.. Do you...",
   "BC_Choices": ["SCAVENGE through the cave for some supplies.","You decide to keep EXPLORING somewhere else instead.","GO BACK to the boat."],
   "BC_Answers": ["go back", "explore", "scavenge"],
   "BC_Outcomes":["You decide to scavenge through the cave for anything or better, supplies.","You decide to keep exploring instead.","You decide to head back to the boat."],

   "Raft": "You decide to remain in the boat. Now you're starting to become hungry. Do you...",
   "R_Choices":["WAIT for longer", "FIND something to eat."],
   "R_Outcomes":["You decide to find food"],

   "Raft_2": "You're starting to suffer from starvation now. Do you...",
   "R2_Choices":["Wait for longer","Start to look for food"],
   "R2_Outcomes": ["Ending 1","You decide to find food"],
   
   "Food": "You explore in order to find food. You have 2 choices. Do you...",
   "Food_Choices": ["Go towards a coconut tree", "Find something else."],
   "Food_Outcomes": ["You decide to get a coconut from a tree.","BeachCave"],
}
S1_Scenario_2 = {
   "Lighthouse": ["After that, you managed to stumble upon an abandoned lighthouse after trekking for a while. Do you..."],
   "L_Decision":["omaygot"],
}
S1_Scenario_3 = {
   
}
S1_Scenario_4 = {
   
}
S1_Scenario_5 = {
   
}   
                  #"You decide to wait out for longer.", 
                 # "It is getting dark. Do you...",

   #"Lighthouse": ["After that, you managed to stumble upon an abandoned lighthouse after trekking for a while. Do you...",],
   #"Wilderness": ["You decide to find food. Do you...",],

PROMPTS_2 = ["You decide to either continue on the forest, or back to the cave, or the lighthouse. Do you...",
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
            #7

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
            #14

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
              #12

OUTCOMES_3 = ["You decide to sleep since its become dark again.",
              #1
              "You decide to not to use to lighthouse and try to explore for more.",
              #2
              "You decide to continue sleeping and not fix the lighthouse.",
              #3
              "You manage to find an abandoned plane after exploring for a while.",
              #4
              "You wake up and decide to go exploring again.",
              #5
              "As you were exiting, you hear footsteps outside.",
              #6
              "You manage to find another beach upon exiting the forest. You also find a boathouse.",]
              #7

ENDINGS = ["You have died from starvation. Game Over.",
          #1
          "You failed to capture as you slowly die of hunger. Game Over.",
          #2
          "You managed to pace towards the houses, but suddenly, you feel extremely tired as you turn around and see the thing getting closer. Game Over",
          #3
          "You managed to pace towards the houses, but suddenly, you feel extremely tired as you turn around and see the thing getting closer. Game Over",
          #4
          "You managed to put up a fight against it, but suddenly, you feel something stab deep in your chest. Game Over",
          #5
          "You have managed to fix the plane as the sun begins to rise. You successfully take off as you fly away. You've unlocked the best ending.",
          #6
          "You see what appears to be a group of guards aiming rifles at you. Where did they come from? Game Over",]
          #7

             #["WAIT LONGER, I hope we get rescued very soon...", "Let's LOOK FOR FOOD, I'm starving..."],
             #

# Available Answers


              #["wait longer", "look for food"]
BEACH_CAVE_ANS = [["go back", "explore", "scavenge"]]
LIGHTHOUSE_ANS = [["explore", "stay"]]
#Scenario Numbers and what they represent:
#1 - 14 = Planewreck Area
#15 - 29 = Beachcave Area
#30 - 44 = Lighthouse Area
#45 - 59 = Wilderness Area
#60 - 74 = Unknown for now
#75 - 89 = Unknown for now
#90 - 104 = Unknown for now
#105 - 119 = Unknown for now
#120 - 139 = Unknown for now

# Functions
toolbox = "no"
run = "no"
scenario_stages = 1
Health = 5

# --------------------------- INTRO -------------------------------
#Are you ready to play the game?
input(IntroPrompts["Welcome"][2])
input(r"""  
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
while scenario_stages >= 1 and scenario_stages <= 14:
    # // PLANEWRECK PHASE \\
    #.
  input("{}".format(Intro_Scenario.get("Planewreck")))
  answer = input(QFORMAT_2.format(Intro_Scenario.get("Decision"),Intro_Scenario["Choices"][0],Intro_Scenario["Choices"][1])).lower()
    # // Stayed at Raft; Now Hungry \\
    #.
  if answer == Intro_Scenario["Answers"][0] or answer == SHORT_OPTIONS[0]:
    input("{}".format(Intro_Scenario["Outcomes"][0]))
    scenario_stages = 2
    #.
    while scenario_stages >= 2 and scenario_stages <= 14:
      answer = input(QFORMAT_2.format(S1_Scenario_1.get("Raft"),S1_Scenario_1["R_Choices"][0],S1_Scenario_1["R_Choices"][1])).lower()
      #Scavenge
      #.
      if answer == S1_Scenario_1["R_Answers"][0] or answer == SHORT_OPTIONS[0]:
        input("{}".format(S1_Scenario_1["R_Outcomes"][0]))
        scenario_stages = 3  
      #Explore deeper
      #.
      elif answer == S1_Scenario_1["R_Answers"][1] or answer == SHORT_OPTIONS[1]:
        input("{}".format(S1_Scenario_1["R_Outcomes"][1]))
        scenario_stages = 4
        break
    # Explore into the Island
    #.
  elif answer == Intro_Scenario["Answers"][1] or answer == SHORT_OPTIONS[1]:
    input("{}".format(Intro_Scenario["Outcomes"][1]))
    scenario_stages = 15
    break
    # No answer
  else:
    input("You have not placed a valid answer. Try again.")


      
  
      


    # // BEACH CAVE PHASE \\
while scenario_stages >= 15 and scenario_stages <= 29:
  answer = input(QFORMAT_3.format(S1_Scenario_1.get("BC_Decision"),S1_Scenario_1["BC_Choices"][0],S1_Scenario_1["BC_Choices"][1],S1_Scenario_1["BC_Choices"][2])).lower()
    #Scavenge
  if answer == S1_Scenario_1["BC_Answers"][0] or answer == SHORT_OPTIONS[0]:
    input("{}".format(S1_Scenario_1["BC_Outcomes"][0]))
    scenario_stages = 16
    break
    #Explore deeper
  elif answer == S1_Scenario_1["BC_Answers"][1] or answer == SHORT_OPTIONS[1]:
    input("{}".format(S1_Scenario_1["BC_Outcomes"][1]))
    scenario_stages = 30
    break
  #Go back to Raft
  elif answer == S1_Scenario_1["BC_Answers"][2] or answer == SHORT_OPTIONS[2]:
    input("{}".format(S1_Scenario_1["BC_Outcomes"][2]))
    scenario_stages = 2
    break
    # No answer
  else:
    input("You have not placed a valid answer. Try again.")


    # // Acquired Toolbox \\
    # // LIGHTHOUSE PHASE \\


