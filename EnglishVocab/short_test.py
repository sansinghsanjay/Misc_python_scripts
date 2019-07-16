from termcolor import colored
from random import shuffle

data = ["Cope#Deal effectively with something difficult.",
"Jingoistic#Characterized by extreme patriotism, especially in the form of aggressive or war like foreign policy",
"Mull#Thinking about deeply and at length, warm and add sugar and spices to it",
"Retribution#punishment/penalty",
"Endeavour#An attempt to achieve a goal",
"Misogyny#Dislike of / Contempt for / ingrained prejudice againts women",
"Pergola#An arched structure in a garden or park consisting of a framework covered with climbing or trailing plants",
"Retro#Imitative of a style or fashion from the past",
"Fatigue#Extreme tiredness resulting from mental or physical excertion or illness",
"Crooked#Bent or twisted out of shape or out of place, dishonest or illegal",
"Intrigue#Arouse the curiosity or interest of fascinate, Make secret plans to do something illicit or determental to someone"]

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
