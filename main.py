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
#Go Back, Explore or Scavenge? 
S1_Scenario_1 = {
   "BeachCave": "\nYou decide to explore the island for whatever can help you temporarily.",
   "BC_Decision": "\nYou suddenly stumble upon a large cave that seems to lead to somewhere.. Do you...",
   "BC_Choices": ["SCAVENGE through the cave for some supplies.","You decide to keep EXPLORING somewhere else instead.","GO BACK to the boat."],
   "BC_Answers": ["go back", "explore", "scavenge"],
   "BC_Outcomes":["You decide to scavenge through the cave for anything or better, supplies.","You decide to keep exploring instead.","You decide to head back to the boat."],

   "Raft": "You decide to remain in the boat. Now you're starting to become hungry. Do you...",
   "R_Choices":["WAIT for longer", "FIND something to eat."],
   "R_Answers":["wait","find"],
   "R_Outcomes":["Wait at the boat, I canw wait","You decide to find food"],

   "Raft_2": "You're starting to suffer from starvation now. Do you...",
   "R2_Choices":["WAIT for longer","START to look for food"],
   "R2_Answers":["wait","start"],
   "R2_Outcomes": ["You decided to keep waiting at the boat.","You decide to find food"],
   
   "Food": "You explore in order to find food. You have 2 choices. Do you...",
   "Food_Choices": ["GO towards a coconut tree", "FIND something else."],
   "Food_Answers": ["go", "find"],
   "Food_Outcomes": ["You decide to get a coconut from a tree. It tasted good, but it'll last you not long.","You look somewhere else.."],
}
S1_Scenario_2 = {
   "Lighthouse": "\nAfter that, you managed to stumble upon a lighthouse after trekking for a while. Do you...",
   "L_Choices":["Stay at the BOTTOM of the lighthouse.","Stay at the TOP of the lighthouse."],
   "L_Answers": ["bottom","top"],
   "L_Outcomes": ["You decide to stay on the bottom of the lighthouse.","You decide to stay on top of the lighthouse."],
   "L_Outcomes_Extra": ["You decide to sleep since its becoming dark.", "You soon wake up in the morning.", "You then realize you can fix the lighthouse with the toolbox.", "You then realize you can try to fix the lighthouse."],
   "L_Top": "\nUpon gazing around the views, you barely managed to spot an abandoned plane far away.",
   
   #If toolbox is not present
   "L_Bottom": "\nYou wake up in the middle of the night. You then realize you can try to fix the lighthouse. Do you...",
   "LBottom_Choices2": ["Try to FIX the lighthouse.","EXPLORE in order to find it."],
   "LBottom_Answers": ["fix", "explore"],
   "LBottom_Outcomes": ["You try to fix the lighthouse without the toolbox. However, you were then fatally electrocuted as you fall back and die.", "You decide to explore in order to find the toolbox. Suddenly, you see an unknown entity charging towards you. You tried to dodge as you were then fatally mauled."],
   
   "L_Top2_Choices": ["GO towar"],
}
S1_Scenario_3 = {
   
}
S1_Scenario_4 = {
   
}
S1_Scenario_5 = {
   
}   
Attack_Function = {
  "Choices": ["ATTACK", "DEFEND", "RUN"],
  "Attack": ["PUNCH", "KICK", "TACKLE"],
  "Defend": ["BLOCK", "DODGE", "PARRY"],
}

# Functions
toolbox = "no".lower()
hungry = "no".lower()
run = "no".lower()
boar_health = 7
ending_scenario = "".lower()
ending = "".lower()
boarattackoutcome = "".lower()

#Boar Attack scenario
def boarattack():
  global fight_status,boarattackoutcome,Health
  fight_status = "attack".lower()
  Health = 5
  boar_health = 7
  input("\nYou have encountered a wild boar on your path!")
  #Your Turn
  input("What will you do?")
  while Health >= 0 or boar_health >= 0:
    choice = input("{} , {} \nDecision Here:".format(Attack_Function["Choices"][0],Attack_Function["Choices"][2])).upper()
    # Attack
    if choice == Attack_Function["Choices"][0] or choice == SHORT_OPTIONS[0].upper():
        input("\nHow will you Attack?")
        attack = input("{} , {} , {} \nDecision Here:".format(Attack_Function["Attack"][0],Attack_Function["Attack"][1],Attack_Function["Attack"][2])).upper()
        # Punch
        if attack == Attack_Function["Attack"][0] or attack == SHORT_OPTIONS[0].upper():
          input("You hit the boar in the face, it squeals as blood spews from its face")
          boar_health = boar_health - 2
          fight_status = "defend".lower()
        # Kick
        elif attack == Attack_Function["Attack"][1] or attack == SHORT_OPTIONS[1].upper():
          input("You kick the boar on its stomach; it gets sent flying and falls with a loud thud.")
          boar_health = boar_health - 3
          fight_status = "defend".lower()
        # Tackle
        elif attack == Attack_Function["Attack"][2] or attack == SHORT_OPTIONS[2].upper(): 
          input("You try to tackle the boar, but you barely had enough power to push it over. It may have fallen unscathed.")
          boar_health = boar_health - 1 
          fight_status = "defend".lower()
    # Run
    elif choice == Attack_Function["Choices"][2] or choice == SHORT_OPTIONS[2].upper():
      input("You decided to run, you did not find its worth to fight at all.")
      fight_status = ""
      break
    # No outputs
    else:
      input("Not a valid answer. Please try again")
      continue

    #Boar Turn
    while fight_status == "defend".lower():
      input("Now the boar will attack you... What will you do?")
      choice = input("{} , {} \nDecision Here:".format(Attack_Function["Choices"][1],Attack_Function["Choices"][2])).upper()
      # Defend
      if choice == Attack_Function["Choices"][1] or choice == SHORT_OPTIONS[1].upper():
          input("\nHow will you Defend?")
          defend = input("{} , {} , {} \nDecision Here:".format(Attack_Function["Defend"][0],Attack_Function["Defend"][1],Attack_Function["Defend"][2])).upper()
          # Block
          if defend == Attack_Function["Defend"][0] or defend == SHORT_OPTIONS[0].upper():
            input("The boar rushes you and you block the attack with your arms. But you werer too weak to stop its attack.")
            Health = Health - 3
            fight_status = "attack".lower()
          # Dodge
          elif defend == Attack_Function["Defend"][1] or defend == SHORT_OPTIONS[1].upper():
            input("The boar rushes you, but you predict its movements and dodge it. It still hits and injures your legs.")
            Health = Health - 1
            fight_status = "attack".lower()
          # Parry
          elif defend == Attack_Function["Defend"][2] or defend == SHORT_OPTIONS[2].upper(): 
            input("You see the boar rushing you and you try to predict its movements. You try to push it away but it bites your arm.")
            Health = Health - 2
            fight_status = "attack".lower()
      # Run
      elif choice == Attack_Function["Choices"][2] or choice == SHORT_OPTIONS[2].upper():
        input("You decided to run, you did not find its worth to fight at all.")
        fight_status = ""
        break
      # No outputs
      else:
        input("Not a valid answer. Please try again")
        continue
    input("The boar is at {} Health. You are at {} Health.".format(boar_health,Health))
    if boar_health < 1 and Health < 1:
      boarattackoutcome = "lose"
      break
    elif boar_health < 1:
      boarattackoutcome = "win"
      break
    elif Health < 1:
      boarattackoutcome = "lose"
      break
    else:
      continue
 
#---------------------------------------- INTRO --------------------------------------------
#-------------Are you ready to play the game?-------------
confirm = input(IntroPrompts["Welcome"][2])
run = "yes".lower()
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

    # ---------------------------------------/--------------------------/ PLANEWRECK PHASE \--------------------------\---------------------------------------
while run == "yes" and boarattackoutcome == "".lower():
  input("{}".format(Intro_Scenario.get("Planewreck")))
  answer = input(QFORMAT_2.format(Intro_Scenario.get("Decision"),Intro_Scenario["Choices"][0],Intro_Scenario["Choices"][1])).lower()
  
    # --------------------------/-------------/ Stayed at Raft \-------------\--------------------------
  if answer == Intro_Scenario["Answers"][0] or answer == SHORT_OPTIONS[0]:
    input("{}".format(Intro_Scenario["Outcomes"][0]))
    
    # --------------------------/-------------/ Now Hungry \-------------\--------------------------
    while run == "yes".lower():
      answer = input(QFORMAT_2.format(S1_Scenario_1.get("Raft"),S1_Scenario_1["R_Choices"][0],S1_Scenario_1["R_Choices"][1])).lower()

        #--------------------------Stay for longer--------------------------
      if answer == S1_Scenario_1["R_Answers"][0] or answer == SHORT_OPTIONS[0]:
          input("{}".format(S1_Scenario_1["R_Outcomes"][0]))
          hungry = "yes".lower()

            #--------------------------Go find food; Starving--------------------------
          while hungry == "yes".lower():
            answer = input(QFORMAT_2.format(S1_Scenario_1.get("Raft_2"),S1_Scenario_1["R2_Choices"][0],S1_Scenario_1["R2_Choices"][1])).lower()
            if answer == S1_Scenario_1["R2_Answers"][1] or answer == SHORT_OPTIONS[1]:
              input("{}".format(S1_Scenario_1["R2_Outcomes"][1]))
              hungry = "no".lower()

                  #--------------------------Stay for longer; Starving--------------------------
            elif answer == S1_Scenario_1["R2_Answers"][0] or answer == SHORT_OPTIONS[0]:
              input("{}".format(S1_Scenario_1["R2_Outcomes"][0]))
              ending_scenario = "Died from Starvation as you did not look for food..."
              ending = "Bad Ending.. Better luck next time"
              run = "no"
              break

                #--------------------------No answer--------------------------
            else:
              input("You have not placed a valid answer. Try again.")
              continue
            
        #--------------------------Go find food--------------------------
      elif answer == S1_Scenario_1["R_Answers"][1] or answer == SHORT_OPTIONS[1]:
          input("{}".format(S1_Scenario_1["R_Outcomes"][1]))
          answer = input(QFORMAT_2.format(S1_Scenario_1.get("Food"),S1_Scenario_1["Food_Choices"][0],S1_Scenario_1["Food_Choices"][1])).lower()

            #--------------------------Coconut Tree--------------------------
          if answer == S1_Scenario_1["Food_Answers"][0] or answer == SHORT_OPTIONS[0]:
            input("{}".format(S1_Scenario_1["Food_Outcomes"][0]))
            

              #--------------------------Boar Attack--------------------------
          elif answer == S1_Scenario_1["Food_Answers"][1] or answer == SHORT_OPTIONS[1]:
            input("{}".format(S1_Scenario_1["Food_Outcomes"][1]))
            boarattack()
            if boarattackoutcome == "win".lower():
              input("You killed the Boar and feasted upon its flesh, tearing it down with your remaining energy.")
              input("\nYou feel sick from eating the raw flesh of the boar, but you don't feel as hungry. You will succumb to the feelings, don't worry.")
              break
            elif boarattackoutcome == "lose".lower():
              input("You fall to the ground.. and as you regain focus, the boar suddenly rushes to you and punts you to a nearby rock. \n")
              input("You lose focus as blood drips from your face.. You know your time has come.")
              ending_scenario = "Died from a wild boar attack..."
              ending = "Bad Ending.. Better luck next time"
              run = "no"
              break
            else:
              input("You ran away, not wanting to fight, but it seems you forgot that you're still starving.")
              input("\nYour body aches for food, you fall as you vomit your insides out, craving for food and water...")
              ending_scenario = "Died from Starvation as you did not eat food..."
              ending = "Bad Ending.. Better luck next time"
              run = "no"
              break
            #--------------------------No answer--------------------------
          else:
            input("You have not placed a valid answer. Try again.")
            continue

        #--------------------------No answer--------------------------
      else:
          input("You have not placed a valid answer. Try again.")
          continue 
          
          
    #--------------------------Explore into the Island--------------------------
  elif answer == Intro_Scenario["Answers"][1] or answer == SHORT_OPTIONS[1]:
    input("{}".format(Intro_Scenario["Outcomes"][1]))
    break

    #--------------------------No answer--------------------------
  else:
    input("You have not placed a valid answer. Try again.")
    continue

    # ---------------------------------------/--------------------------/ BEACH CAVE PHASE \--------------------------\---------------------------------------
while run == "yes".lower() or boarattackoutcome == "win".lower():
  run = "yes".lower()
  boarattackoutcome = "".lower()
  answer = input(QFORMAT_3.format(S1_Scenario_1.get("BC_Decision"),S1_Scenario_1["BC_Choices"][0],S1_Scenario_1["BC_Choices"][1],S1_Scenario_1["BC_Choices"][2])).lower()
    #--------------------------Scavenge--------------------------
  if answer == S1_Scenario_1["BC_Answers"][0] or answer == SHORT_OPTIONS[0]:
    input("{}".format(S1_Scenario_1["BC_Outcomes"][0]))


    #--------------------------Explore deeper--------------------------
  elif answer == S1_Scenario_1["BC_Answers"][1] or answer == SHORT_OPTIONS[1]:
    input("{}".format(S1_Scenario_1["BC_Outcomes"][1]))

  #--------------------------Go back to Raft--------------------------
  elif answer == S1_Scenario_1["BC_Answers"][2] or answer == SHORT_OPTIONS[2]:
    input("{}".format(S1_Scenario_1["BC_Outcomes"][2]))
    break

    # -------------No answer-------------
  else:
    input("You have not placed a valid answer. Try again.")


    # // LIGHTHOUSE PHASE \\




# Finished the Game
input("\nYou have {}".format(ending_scenario))
input("You have achieved the {}".format(ending))
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