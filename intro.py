print("Welcome to our game:\n SURVIVAL OF THE ISLE")
#Checks if they are confident in winning or not
confidence = str(input(QFORMAT_3.format((IntroPrompts["Welcome"][0].lower()),Q_INTRO[0][0],Q_INTRO[0][1],Q_INTRO[0][2]))).lower()
if confidence == INTRO_ANS[0] or confidence == SHORT_OPTIONS[0]:
    input("Well well... \nYour decisions will be put to the test... (PRESS ENTER TO CONTINUE)")
elif confidence == INTRO_ANS[1] or confidence == SHORT_OPTIONS[1]:
    input("Haha! You're a fool for playing... \nYou will face certain death, I'm sure... (PRESS ENTER TO CONTINUE)")
elif confidence == INTRO_ANS[2] or confidence == SHORT_OPTIONS[2]:
    input("Ha! You're not so sure huh... \nYou're going to die here, I know of that now...(PRESS ENTER TO CONTINUE)")

#Do you want a tutorial?
tutorial = input(QFORMAT_2.format((IntroPrompts["Welcome"][1]),Q_INTRO[0][0],Q_INTRO[0][1])).lower()
if tutorial == INTRO_ANS[0]:
    input("\nGood choice... Here's how it will work. (PRESS ENTER TO CONTINUE)")
    run = "Yes".lower()
elif tutorial ==INTRO_ANS[1]:
    input("\nWow.. I must say, you're brave..\nGood luck on survivng, you will need it. (PRESS ENTER TO CONTINUE)")

#Tutorial in Progress - How decisions are given to you
while run == "Yes".lower():
  input("Your objective of the game is to survive and escape an island.. You are unaware of your surroundings and have different choices to make. (PRESS ENTER TO CONTINUE)\n")
  input(QFORMAT_4.format((IntroPrompts["Tutorial"][0]),Q_INTRO[1][0],Q_INTRO[1][1],Q_INTRO[1][2],Q_INTRO[1][3]))
  understand = input(QFORMAT_3.format(( IntroPrompts["Tutorial"][1]),Q_INTRO[0][0],Q_INTRO[0][1],Q_INTRO[0][2])).lower()
  if understand == INTRO_ANS[0].lower() or confidence == SHORT_OPTIONS[0].lower():
    input("Wonderful, you may be alive by the end of the night, but I cannot guarantee your survival. (PRESS ENTER TO CONTINUE)")
  elif understand == INTRO_ANS[1].lower() or confidence == SHORT_OPTIONS[1].lower():
    input("Wow.. such easy instructions and you fail to understand?\n Let's try that again... (PRESS ENTER TO CONTINUE)")
    continue
  elif understand == INTRO_ANS[2].lower() or confidence == SHORT_OPTIONS[2].lower():
    input("Ha! You're not so sure huh... \nYou're going to die here, I know of that now...\n I will give you the instructions one more time...\n (PRESS ENTER TO CONTINUE)")
    continue

#Tutorial in Progress - How to go through prompts and how to answer decisions
  input("So, {}".format((IntroPrompts["Tutorial"][2])))
  understand = input(QFORMAT_3.format((IntroPrompts["Tutorial"][3]),Q_INTRO[2][0],Q_INTRO[2][1],Q_INTRO[2][2])).lower()
  if understand == INTRO_ANS[0] or confidence == SHORT_OPTIONS[0]:
    input("Wonderful, you may be alive by the end of the night, but I cannot guarantee your survival.")
    break

  elif understand == INTRO_ANS[1] or confidence == SHORT_OPTIONS[1]:
    input("Wow.. such easy instructions and you fail to understand?\n Let's try that again... (PRESS ENTER TO CONTINUE)")
    continue
  elif understand == INTRO_ANS[2] or confidence == SHORT_OPTIONS[2]:
    input("Ha! You're not so sure huh... \nYou're going to die here, I know of that now...\n I will give you the instructions one more time...\n (PRESS ENTER TO CONTINUE)")
    continue