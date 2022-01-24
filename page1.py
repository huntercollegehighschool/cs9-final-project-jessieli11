#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.
import time

def bus():
  import os
  os.system('clear')
  print("You patiently wait at the bus stop. After a good ten minutes, it finally arrives. The bus driver gives you a nod as you step on and pay the fare. It's been an exhausting night.")
  time.sleep(3)
  print("\nEvery second that the bus is driving, you wait for something wild to happen. Maybe a bird will fly through the open window and transform into a monster.")
  time.sleep(4)
  print("\nOr maybe the bus driver will start growing ten arms and try to eat you.")
  time.sleep(3)
  import os
  os.system('clear')
  print("But everything is peaceful. It's probably around 2am by now, and everything is so... quiet. As you sit there on the bus, watching the streets pass by, your eyelids get heavier, and heavier.")
  time.sleep(4)
  print("\nTaking a nap won't hurt. Just a snooze...")
  time.sleep(2)
  go = input("\nEnter E to continue. ")
  while go != "E":
    go = input("\nYou must enter E to continue. ")
  if go == "E":
    import os
    os.system('clear')
    time.sleep(1)
    print(".")
    import os
    os.system('clear')
    time.sleep(1)
    print("..")
    import os
    os.system('clear')
    time.sleep(1)
    print("...")
    import os
    os.system('clear')
    time.sleep(2)
    print("You slowly open your eyes. You were awoken by someone tapping on your shoulder. ")
    time.sleep(3)
    print("\nAfter a few blinks, you realize that you're still on the bus, and the bus driver is standing beside you.")
    time.sleep(3)
    print("\nBus Driver: You have to get off now.")
    time.sleep(3)
    print("\nYou: What? I don't think I'm at my stop yet.")
    time.sleep(3)
    print("\nBus Driver: Buddy, this is the last stop.")
    time.sleep(3)
    print("\nYou: Well can't we drive back?")
    time.sleep(3)
    print("\nBus Driver: Uhh I'm taking a break. This bus won't be moving until another hour or two.")
    time.sleep(3)
    print("\nYou: What?! Is that how buses work?")
    time.sleep(3)
    print("\nBus Driver: Well I'm tired. Now get off.")
    time.sleep(3)
    print("\nYou: Can you at least tell me the fastest route to my neighborhood?")
    time.sleep(3)
    print("\nBus Driver: You can always just take the subway. It'll take you straight to your house.")
    time.sleep(3)
    print("\nYou: Ahhh crap not the subway--")
    time.sleep(3)
    import os
    os.system('clear')
    time.sleep(1)
    print("THE END")

def escape():
  import os
  os.system('clear')
  print("You really only had one option. When the train finally goes to a stop, you run towards the doors and up the stairs. You try not to think about the fact you might've trampled on a few mice on your way out.")
  time.sleep(5)
  print("\nYou're too scared to go back to the train station, in fear of the mice sniffing you out. You take out your phone to find the nearest bus route, only to see that your phone is completely cracked and broken.")
  time.sleep(5)
  print("\nIt must've broken during your shuffle with the Thief.")
  time.sleep(5)
  import os
  os.system('clear')
  print("You decide to wander around and try to find a bus stop.")
  dog = input("\nAs you are walking, you spot a stray dog. Do you feel like [follow]ing the dog or continue [walk]ing? ")
  while dog != "follow" and dog != "walk":
    print("\nPlease enter [follow] or [walk].")
    dog = input("\nDo you feel like [follow]ing the dog or continue [walk]ing? ")
  if dog == "follow":
    import os
    os.system('clear')
    print("\nYou decide to follow the dog. It smells it a bit, honestly, but after today's events, you're feeling impulsive and too drained to make logical decisions.")
    time.sleep(3)
    print("\nLuckily for you, the dog was feeling nice and led to to a bus stop.")
    time.sleep(3)
    print("\nYou: Thanks a ton, dude.")
    time.sleep(2)
    print("\nDog: No problem, man. \nThe Dog winks at you with sparkling eyes and struts away.")
    time.sleep(3)
    bus()
  elif dog == "walk":
    import os
    os.system('clear')
    print("You decide to make the more logical decision and you continue wandering around in an unfamiliar neighborhood, until you spot a stray cat. There seems to be a lot of stray animals around here.")
    time.sleep(3)
    print("\nYou approach the friendly-looking cat. \nYou: Hi. Do you know where the nearest bus stop is?")
    time.sleep(3)
    print("\nAfter licking a paw leisurely, the cat looks back at you. \nCat: Only if you pay me.")
    time.sleep(3)
    print("\nOh, look. A talking cat. \nYou: What? Like with money?")
    time.sleep(2)
    print("\nCat: What other types of payment are there? Of course I'm talking about money.")
    time.sleep(3)
    print("\nYou: But what could a cat possibly use money for?")
    time.sleep(2)
    print("\nCat: Do you want directions or not? Give me a 5 and I'm good. I need to get my nails done this week.")
    time.sleep(3)
    print("\nYou: Alright, fine.")
    time.sleep(2)
    print("You take out your wallet and hand the cat a five dollar bill and the cat gives you directions. ")
    time.sleep(3)
    print("\nAfter a short walk, you finally arrive at a bus stop.")
    time.sleep(3)
    bus()



def mice():
  import os
  os.system('clear')
  print("\nA boisterous laugh escapes the Old Man. Suddenly, the moving train car erupts with mice.")
  time.sleep(3)
  print("\nYou look at the train floor in horror. Small, brown mice crawl from every nook and cranny and from underneath the seats.") 
  time.sleep(3)
  print("\nYou spring up from your seat and look at the Old Man. \nYou: What the hell is going on?!")
  time.sleep(3)
  print("\nOld Man: Say hi to my buddies! Sorry if they're a bit hyper, they're just as excited to see you as I am!")
  time.sleep(3)
  print("\nYou are terrified of mice. Especially ones that are able to be summoned by a cheery old man on the subway at 12am.")
  time.sleep(3)
  mouse = input("\nAnd so, you realize that you only have two options in this situation. \nEnter Y to escape at the next stop or N to stay in the train. ")
  while mouse != "Y" and mouse != "N":
    mouse = input("\nPlease enter Y or N. ")
  if mouse == "Y":
    escape()
  elif mouse == "N":
    import os
    os.system('clear')
    print("You need to get home fast and you cannot afford leaving the train now. It'll only be a few stops... right?")
    time.sleep(3)
    print("\nYou: Please get these mice away. I beg of you.")
    time.sleep(3)
    print("\nOld Man: You... want to kick my buddies out? Do you not like my mice? How could you say such harsh words in front of them?")
    time.sleep(3)
    print("\nThe Old Man's face reddens, and with a single swoop of a hand, he orders the mice to attack you.")
    time.sleep(3)
    fightmice = input("\nDo you [beg] for forgiveness or [fight] the mice? ")
    while fightmice != "beg" and fightmice != "fight":
      fightmice = input("\nPlease enter [beg] or [fight]. ")
    if fightmice == "beg":
      import os
      os.system('clear')
      print("It is far too late. The mice overwhelm you and you become their prey.")
      escapetrain = input("\nEnter E to turn back time and escape the train before the mice get you. ")
      while escapetrain != "E":
        escapetrain = input("\nPlease enter E to turn back.  ")
      if escapetrain == "E":
          escape()
    elif fightmice == "fight":
      import os
      os.system('clear')
      print("You decide to fight the mice, but you are only one man against many. You pull a few punches but your skills can only do so much.")
      time.sleep(3)
      print("\nThe mice overwhelm you and you become their prey.")
      time.sleep(2)
      escapetrain = input("\nEnter E to turn back time and escape the train before the mice get you.")
      if escapetrain == "E":
        escape()

def trainride():
  import os
  os.system('clear')
  print("\nYou triumphantly strut to the train station. Lucky for you, the train arrived the moment you entered. Though you look a bit unkempt, you feel refreshed.")
  time.sleep(5)
  print("\nAs you step into the train, you notice that you are not alone. Across from where you chose you sit is an old man grinning widely.")
  time.sleep(4)
  print("\nOld Man: Ah! A visitor. We don't get many these days.")
  time.sleep(2)
  reply = input("\nEnter Y to respond or N to ignore. ")
  while reply != "Y" and reply != "N":
    reply = input("\nPlease choose either Y or N. ")
  if reply == "Y":
    import os
    os.system('clear')
    print("You know you probably shouldn't respond, but you couldn't help yourself.")
    time.sleep(3)
    print("\nYou: Pardon?")
    time.sleep(3)
    print("\nOld Man: Well you see, usually its just me and my buddies down here. It's quite nice to see human face once in a while!")
    time.sleep(3)
    print("\nYou: Isn't this one of the busiest trains in the morning?")
    time.sleep(3)
    print("\nOld Man: Well my buddies and I don't like the light. Far too bright. We don't see many humans around this time of the day. ")
    time.sleep(3)
    print("\nYou: Oh... what about your buddies then?")
    time.sleep(2)
    go = input("\nEnter E to continue. ")
    while go != "E":
      go = input("\nYou must enter E to continue. ")
    if go == "E":
      mice()
  elif reply == "N":
    import os
    os.system('clear')
    print("\nThis guy seems a bit weird. It's probably safer to keep to yourself.")
    time.sleep(3)
    print("\nOld Man: Ah, not much of a talker are we. Well that's fine... just the usually response from humans. I have my own buddies here to keep me company.")
    time.sleep(3)
    print("\nYou're confused and feel the pressure to talk.\nYou: Pardon?")
    time.sleep(3)
    print("\nOld Man: Well you see, usually it's just me and my buddies down here at this hour. We don't receive much human contact.")
    time.sleep(3)
    print("\nYou: Oh... what about your buddies then?")
    time.sleep(2)
    go = input("\nEnter E to continue. ")
    while go != "E":
      go = input("\nYou must enter E to continue. ")
    if go == "E":
      mice()

def duel():
  import os
  os.system('clear')
  print("You have now entered a duel with the Thief who stole your phone. You've taken karate lessons back in third grade, so you're pretty confident.")
  print("\nYou want to make the first move.")
  move = input("Enter F to punch. ")
  if move == "F":
    print("You dealt 15% damage to Thief.")
    time.sleep(1)
    print("\nThief punched You and did 10% damage.")
  if move != "F":
    print("You made the wrong move and receive 15% damage from Thief.")
  move = input ("Enter K to kick. ")
  if move == "K":
    print("You dealt 25% damage to Thief.")
    time.sleep(1)
    print("\nThief punched You and did 10% damage.")
  if move != "K":
    print("You made the wrong move and receive 15% damage from Thief.")
  move = input("Enter F to punch. ")
  if move == "F":
    print("You dealt 15% damage to Thief.")
    time.sleep(1)
    print("\nThief punched You and did 10% damage.")
  if move != "F":
    print("You made the wrong move and receive 15% damage from Thief.")
  move = input ("Enter K to kick. ")
  if move == "K":
    print("You dealt 25% damage to Thief.")
    time.sleep(1)
    print("\nThief punched You and did 10% damage.")
  if move != "K":
    print("You made the wrong move and receive 15% damage from Thief.")
  move = input ("Enter K to kick. ")
  if move == "K":
    print("You dealt 25% damage to Thief.")
  if move != "K":
    print("You made the wrong move, and receive 15% damage from Thief.")
  time.sleep(2)
  print("\nTHIEF'S HP: 0")
  print("\nYou've successfully defeated the Thief. You shuffle through his pocket and take your phone back.")
  time.sleep(3)
  go = input("\nEnter E to continue. ")
  while go != "E":
    go = input("\nYou must enter E to continue. ")
  if go == "E":
    trainride()

def confront():
  import os
  os.system('clear')
  print("You walk back stealthily and spot the hooded figure. You're not one to shy away from confrontations. \nYou: Give me my phone back.") 
  time.sleep(3)
  print("\nThief: What phone? I don't have your phone.")
  time.sleep(2)
  print("\nYou: I know you have it. Give it back.") 
  time.sleep(2)
  print(" \nThe thief pauses. \nThief: Would you do anything to get your phone back?")
  time.sleep(2)
  print("\nYou: Of course. It's mine.")
  time.sleep(2)
  print("\nThief: Then I challenge you to a duel to the death.")
  time.sleep(2)
  print("\nAnd of course, you accept the challenge.")
  time.sleep(2)
  go = input("\nEnter E to continue. ")
  while go != "E":
    go = input("\nYou must enter E to continue. ")
  if go == "E":
    duel()

def train():
  import os
  os.system('clear')
  print("You slowly make your way to the train station. As you are nearing the station, someone bumps into your shoulder as they pass by.")
  time.sleep(2)
  print("\nThey simply mutter a quick 'sorry'.")
  time.sleep(1)
  print("\nYou didn't really mind, until you reach for you phone. Your pocket is empty.") 
  time.sleep(3)
  print("\nWell, it looks like you just got pickpocketed.")
  time.sleep(2)
  attack = input("\nThe man hasn't gone far yet. You could still choose to [confront] him, or [ignore] what just happened. ")
  while attack != "confront" and attack != "ignore":
    attack = input("\nPlease choose either to [confront] or [ignore]. ")
  if attack == "confront":
    confront()
  elif attack == "ignore":
    import os
    os.system('clear')
    print("There is an empty void in your chest. Your phone was your life, as well as all that was left of your bank account. It was a newly purchased iPhone XV and you had let it go, just like that. You start sobbing uncontrollably and breaking down in the middle of the sidewalk. It's too late now to confront the thief and you regret your decision.")
    ignore = input("\nEnter Y to go back in time and confront the thief. ")
    while ignore != "Y":
      ignore = input("\nYou must enter Y to go back in time and confront the thief. ")
    if ignore == "Y":
      confront()
train()

