# libraries
import numpy as np
import pandas as pd
import random
import sys
from termcolor import colored

# setting random seed
rand_seed = np.random.randint(0, 1000)

# paths
dictionary_path = "addedWords.csv"

# read data
data = pd.read_csv(dictionary_path, sep=';', header=None)

# make shuffled list of index
l = data.shape[0]
ques_seq = list(range(l))
random.shuffle(ques_seq)

# pop up questions one by one
score = 0
for i in range(l):
	# fetch question number, question and answer
	q_no = ques_seq.pop(0)
	ques = data.iloc[q_no, 1]
	ans = data.iloc[q_no, 0].strip().lower()
	print("-----------------------------------------------------------------------------------------")
	# ask question
	print("# Ques. " + str(i + 1) + " of " + str(l))
	print(ques)
	while(True):
		# ask for user input
		choice = input(">> Enter your answer OR ' ' to show answer OR 'q' to quit: ")
		if(len(choice) > 1):
			user_ans = choice.strip()
			user_ans = user_ans.lower()
			if(user_ans == ans):
				score += 1
				print(colored("CORRECT", "green"))
			else:
				print(colored("INCORRECT", "red"))
			print("Ans. " + str(ans))
			break
		elif(choice == ' '):
			print("Ans. " + str(ans))
			break
		elif(choice == "q"):
			print("BYE...")
			sys.exit(0)

# print score
print("############################################################################################")
perc = (score / float(l)) * 100
print(colored("Your score is: " + str(score) + " out of " + str(l) + ", " + str(perc), "blue"))
