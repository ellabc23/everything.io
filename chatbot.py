name= input("Enter your name!")
print("Welcome to the ChatBot, " + name +"!")
input("How is your day so far?")
print("Same with me.")
joke= input(name +", do you want to hear a joke, yes or no?")
if joke=='yes':
  input("What did one snowman say to the other?")
  print("I smell carrots!")
  print("Aww. Maybe next time.")
else:
  print("Maybe later.")
tellme=input("Do you want to tell me a joke?")
if tellme=='yes':
   input("Go ahead!")
   input("What's the punch line?")
   print("Haha! You're so funny!")
else:
    print("That's too bad.")
color = input(name + ", I really like the color blue. What's your favorite color?")
if color=='blue':
   print("Wow, " + name + ", we are two birds of a feather!")
else:
    print(color + " is a nice color too.")
games = input("Do you like games?")
if games=='yes':
   input("What's your favorite game?")
   print("I like that one too!")
hobby = input("What do you like doing in your free time?")
input("I haven't tried that one. Could you describe what it's like?")
print("Wow. I'll have to try " + hobby + " sometime.")
goodbye= input(name + ", I have to leave soon, but do you want to keep talking? Yes, or no?")
if goodbye=='yes':
  print("Great!")
  input("Here's a riddle: You have three stoves: a gas stove, a wood stove, and a coal stove, but only one match. Which should you light first?")
  print("The match!")
  input("If you were running a race, and you passed the person in 2nd place, what place would you be in now?")
  print("Second place! You passed the person in second, not the person in first!")
  input("What weighs more? A pound of feathers or a pound of bricks?")
  print("None of them! They all weigh a pound!")
  print("I'm so tired! I should probably go, " + name +", bye!")
else:
    print("Ok, " + name + ", goodbye!")
