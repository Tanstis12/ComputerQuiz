#Thomas Anstis
#Computer Quiz
score = 0
print("WARNING!, ALL ANSWERS MUST BE IN lower case")
print("Do you want to play my computer quiz? ")


playing = input("Do you want to play?(yes/no) ")
if playing != "yes":
    quit()
    
print("Ok, let's play :)")

print("Question 1")

Answer1 = input("What does CPU mean? ")
if Answer1 == "central processing unit":
    print("Correct! ")
    score = score + 1
    print("Your score is")
    print(score)
else:
    print("Incorrect! ")
    print("The correct answer is central processing unit")
    score = score + 0
    print("Your score is")
    print(score)
    
print("Question 2")

Answer2 = input("What does GPU mean? ")
if Answer2 == "graphics processing unit":
    print("Correct! ")
    score = score + 1
    print("Your score is")
    print(score)
else:
    print("Incorrect! ")
    print("The correct answer is graphics processing unit")
    score = score + 0
    print("Your score is")
    print(score)

print("Question 3")
print("FINAL QUESTION")
print("DOUBLE POINTS")

Answer3 = input("What does HDD mean? ")
if Answer3 == "hard disk drive":
    print("Correct! ")
    score = score + 2
    print("Your score is")
    print(score)
else:
    print("Incorrect! ")
    print("The correct answer is hard disk drive")
    score = score + 0
    print("Your score is")
    print(score)
    
print((score),"/4 is your final score")
print("Thanks for PLaying :)")


