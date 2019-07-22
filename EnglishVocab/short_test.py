from termcolor import colored
from random import shuffle

data = ["outlook#a person's point of view or general attitude to life",
"merriment#gaiety and fun",
"frisky#playfull and full of energy",
"hangup#an emotional problem or inhibition",
"realm#a kingdom, a field / domain of activity / interest",
"hatred#intense dislike / hate",
"estuary#the tidal mouth of a large river, a water passage where a tide meets a river current"
]

count = 0
shuffle(data)
for i in range(len(data)):
	line = data[i]
	splits = line.split("#")
	ans = splits[1]
	que = splits[0]
	print(str(i) + " of " + str(len(data)) + ": " + ans)
	user_ans = input("Enter your ans: ")
	if(user_ans.strip() == que.lower().strip()):
		print(colored("CORRECT", "green"))
		count = count + 1
	else:
		print(colored("INCORRECT", "red"))
		print(colored("Ans: " + que, "yellow"))

perc = count / float(len(data)) * 100
print("Percentage: " + str(perc) + " %")
