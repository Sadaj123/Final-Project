# Imported Modules
import random
import time

# Variables
ans1 = "Go for it!"
ans2 = "No way, Jose!"
ans3 = "I'm not sure. Ask me again."
ans4 = "As I see it, sorry no."
ans5 = "No, you'd have better luck getting struck by lightning!"
ans6 = "Yea ya can!"
ans7 = "Makes no difference to me, do or don't - whatever."
ans8 = "Honestly, your gonan fail bud."
choice = random.randint(1, 8)

# Main Code
user_name = input("Hey there, Welcome to The Magic 8 Ball. What's your name?\n")
print("Welcome to The Magic 8 Ball", user_name)
question = input("Ask me for advice then press ENTER to shake me.\n")
print("shaking ...")
time.sleep(2)
print("shaking ...")
time.sleep(2)
print("shaking ...")
time.sleep(2)
print("shaking ...\n")
time.sleep(2)
# Assigning values to variables and then creating a new variable to store the random value.
if choice == 1:
    answer = ans1
elif choice == 2:
    answer = ans2
elif choice == 3:
    answer = ans3
elif choice == 4:
    answer = ans4
elif choice == 5:
    answer = ans5
elif choice == 6:
    answer = ans6
elif choice == 7:
    answer = ans7
else:
    answer = ans8
#Now the bit that the user sees.
print(answer)
print("\nThanks for playing The Magic 8 Ball", user_name,".\n")
print("Press ENTER to leave.")
