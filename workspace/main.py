import sys

def introduction():
  print ("You have an hour to live. You must cross the bridge and get to the hospital! But the world needs your help. What will you choose to do?")
  print("")
  
def collectTrash():
  print ("Some volunteers want you to collect trash. Will you help them or not?") 
  answer = input("Type y for YES or n for NO")
  if answer == "y":
    print ("The volunteers thank you.")
    print("")
    homelessMan()
  elif answer == "n":
    print ("The volunteers beat you up")
    print("")
    carAccident()
  else:
    collectTrash()
    
def carAccident():
  print("There has been a major car accident on the road. People are stuck in their cars and are about to die. Do you help them?")
  answer = input("Type y for YES or n for NO")
  if answer == "y":
    print ("You decide to help the victims. You end up successfully getting all of the victims out of the car and to safety. Although, you got your arm stuck in something and you lose your arm. Sorry.")
    print ("")
    stealMoney()
  elif answer == "n":
    print ("You decide to walk past it and not help the victims. Suddenly, you hear a loud explosion and you see that the car and the victims have exploded.")
    print("")
    helpSuicidal()
  else:
    carAccident()
    
def helpSuicidal():
  print ("You see a woman leaning over the edge of the bridge, looking like she wants to jump off. Do you try and help her and convince her not to jump?")
  answer = input("Type y for YES or n for NO")
  if answer == "y":
    print ("When you try and help the woman, she reaches for you and pulls you with her off the edge. You both fall and die. Go to heaven.")
    sys.exit()
  elif answer == "n":
    print ("You decide to leave her alone and let her do her business. As you are walking you hear a scream and see a person faling from the bridge. Oh well.")
    print("")
    helpChild()
  else:
    helpSuicidal()
    
def helpChild():
  print ("Suddenly, the cables start to snap and the bridge violently shakes. The bridge is collapsing! You see a safe point up ahead and you think you can make it if you hurry. But, you see a cute child alone and scared. Do you help him?")
  answer = input("Type y for YES or n for NO")
  if answer == "y":
    print ("You decide to help the child. You run over to him and he starts crying and screaming. As you reach for him, the ground below collapses and you both fall and die. Go to hell.")
    sys.exit()
  elif answer == "n":
    print ("You decide to save yourself instead of helping the child. But, you couldn't make it after all. The bridge collapses under your feet. You fall and die. Go to heaven.")
    sys.exit()
  else:
    helpChild()
  
def stealMoney():
  print ("You see a fat kid with a hundred bucks. This will cover the rest of your medical bills. Do you steal it?")
  answer = input("Type y for YES or n for NO")
  if answer == "y":
    print ("Assuming that the kid will buy more food and die from obesity, you think you are saving his life. You walk up to him and take the hundo. However, his really fat mama, at least 600 pounds, comes and sits on your face and you suffocate and you die. Go to hell.")
    sys.exit()
  elif answer == "n":
    print ("You keep walking and continue your journey.")
    print("")
    chooseDestination2()
  else:
    stealMoney()
    
def chooseDestination2():
  print ("While on your journey to the hospital, you succumb to your wounds. You die. Now, you see two signs on the road leading to different directions. One says heaven, one says hell. Decide, do you want to go to Heaven, or to Hell? ")
  answer = input("Type y for HEAVEN or n for HELL")
  if answer == "y":
    print ("You picked heaven and you got tricked. Go to hell.")
    sys.exit()
  elif answer == "n":
    print ("You picked hell and you got tricked. Go to heaven.")
    sys.exit()
  else:
    chooseDestination2()

def homelessMan():
  print ("A homeless man approaches you on your journey to the hospital. He asks for money, do you give him some?")
  answer = input("Type y for YES or n for NO")
  if answer == "y":
    print ("The homelessman thanks you.")
    print("")
    helpOldWoman()
  elif answer == "n":
    print ("The homeless man beats you up!")
    print("")
    pickGun()
  else:
    homelessMan()
    
def helpOldWoman():
  print ("You see an old woman getting robbed by a man. She has a cane and she is calling for help. Do you help her and retrieve her bag or no?")
  answer = input("Type y for YES or n for NO")
  if answer == "y":
    print ("You decide to chase the man down and try and retrieve her bag. Unfortunately, you have not been going to the gym lately. You try and fight him, but he pushes you over the ledge of the bridge and you fall and die. Go to heaven.")
    sys.exit()
    print ("")
  elif answer == "n":
    print ("You decide to just keep walking and mind your own business. But, the old woman hits you with her cane and she has been working out. You lose a limb. Oh well.")
    print ("")
    chooseDestination()
  else:
    helpOldWoman()
    
def chooseDestination():
  print("While walking, you succumb to your wounds and die. Now, you see two signs on the road leading to different directions. One says heaven, one says hell. Decide, do you want to go to Heaven, or to Hell?")
  answer = input("Type y for HEAVEN or n for HELL")
  if answer == "y":
    print ("Go to Hell.")
    sys.exit()
  elif answer == "n":
    print ("Go to Heaven")
    sys.exit()
    print ("")
  else:
    chooseDestination()
    
def pickGun():
  print ("You find a gun on the side of the bridge. Do you pick it up?")
  answer = input("Type y for YES or n for NO")
  if answer == "y":
    print ("You pick up the gun and continue your journey")
    print("")
    killStranger()
  elif answer =="n":
    print ("The bridge collapses. You fall and die. Go to heaven")
    sys.exit()
    print("")
  else:
    pickGun()

def killStranger():
  print ("You encounter a stranger, his face seems familiar. Do you shoot him?")
  answer = input("Type y for YES or n for NO")
  if answer == "y":
    print("You shoot the man. The cops arrive and shoot you on sight. You die and go to heaven. While in heaven, you find out the man you shot was a serial killer.")
    sys.exit()
    print("")
  elif answer == "n":
    print ("You decide not to kill the man. You continue and you see the end of the bridge and the hospital. You made it. Congratulations. While in the hospital, you see the news and notice that the familiar face you saw was a serial killer.")
    sys.exit()
  else:
    killStranger()
    
introduction()
collectTrash()