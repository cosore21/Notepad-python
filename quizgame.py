print("welcome to my computer quiz")

playing = input("Do you want to play?")

if playing.lower() == "yes":
   print("okay! let's play :")

else:

    print("You Have Selected a Wrong Choice!")
    quit()

score=0

answer = input("what does CPU stand for? ")

if answer == "Central Processing Unit":
    print('Correct answer!')
    score+=1
else:
    print("Incorrect answer")

answer = input("What does GPU stand for?" )

if answer== "Graphical Processing Unit":
    print('Correct answer!')
    score+=1
else:
    print("Incorrect answer")

answer = input("what does RAM stand for? ")

if answer == "Random Access Memory":
    print('Correct answer!')
    score+=1
else:
    print("Incorrect answer")

answer = input("what does PSU stand for? ")

if answer == "Power Supply Unit":
    print('Correct answer!')
    score+=1
else:
    print("Incorrect answer")

print("You got "  + str(score)+" questions correct!")
print("You got "  + str(score/4*100)+"%")