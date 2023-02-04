import random

random_number = random.randint(1, 12)
# print(random_number)

name = 'Loki!'
question = "Are you the tits?"
answer = ""

if random_number == 1:
    answer = "Yes - definitely!"
elif random_number == 2:
    answer = "It is decidely so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
elif random_number == 10:
    answer = "Fuckin a you're the tits!"
elif random_number == 11:
    answer = "You got great tits."
elif random_number == 12:
    answer = "Sometimes."
else: 
    answer = "ERROR"

if question == "":
    print("")
elif name != "":
    print(name + " asks: " + question)
else:
    print("Question: " + question)

if question != "":
    print("Magic 8-Ball's answer:" + answer)
else:
    print("")