"""
Name(s):Jessie Li
Name of Project:
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

name = input("Enter your name: ")
import time
print("Welcome,", name, ".")
time.sleep(1)

def intro():
  print("\nYou had spent your entire Saturday evening exploring the city and you had just realized how late it was. You turn on your phone and you see that it's 11:17pm. ")
intro()

def tp(): 
  print("\nYou go on Google Maps to find the fastest way home. According to the app, you'd get home around the same time whether you decide to take the bus or the train. So, you decide to take the train.")
  time.sleep(5)
  start = input("\nEnter E to continue. ")
  while start != "E":
    start = input("You must enter E to continue. ")
  if start == "E":
    import page1
tp()