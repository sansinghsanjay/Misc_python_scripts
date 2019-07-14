#libraries
import numpy as np
import pandas as pd
import random
import sys
from termcolor import colored

# setting random seed
rand_seed = np.random.randint(0, 1000)
random.seed(rand_seed)

# dictionary file path
dictionary_path = "/home/sansingh/github/Misc_python_scripts/EnglishVocab/addedWords.txt"

# read file
fileReadDict = open(dictionary_path, "r")
dictData = fileReadDict.read()
dictLines = dictData.split("\n")

# find out question numbers with highest mistakes
mistakes = []
for i in range(len(dictLines)):
	splits = dictLines[i].split(">")
	if(len(splits) > 2):
		mistakes.append(int(splits[len(splits) - 1]))

# get indices of mistakes in descending order
#indices = np.argsort(mistakes)[::-1]

# print statistics
mistake_stats = list(np.zeros(30, dtype=np.uint8))
quesIndexCategoryList = []
mistake_count = 30
while(mistake_count >= 0):
	tempList = []
	for i in range(len(mistakes)):
		if(mistakes[i] == mistake_count):
			mistake_stats[mistake_count] = mistake_stats[mistake_count] + 1
			tempList.append(i)
	if(len(tempList) > 0):
		quesIndexCategoryList.append(tempList)
	mistake_count = mistake_count - 1
print("Following is the statistics of previous performance: ")
print("# mistakes" + "\t" + "# questions")
for i in range(len(mistake_stats)):
	if(mistake_stats[i] > 0):
		print(str(i) + "\t" + str(mistake_stats[i]))
print("Total:" + "\t" + str(sum(mistake_stats)))

# shuffle ques indexes and form a common list
quesList = []
for i in range(len(quesIndexCategoryList)):
	random.shuffle(quesIndexCategoryList[i])
	for j in range(len(quesIndexCategoryList[i])):
		quesList.append(quesIndexCategoryList[i][j])

# start test
# pop up questions one by one
score = 0
len_quesList = len(quesList)
for i in range(len_quesList):
	# fetch question number, question and answer
	q_no = quesList[i]
	tokens = dictLines[q_no].split(">")
	ques = tokens[1]
	ans = tokens[0].strip().lower()
	ans_ticks = []
	for j in range(2, len(tokens) - 1):
		ans_ticks.append(int(tokens[j]))
	print("-----------------------------------------------------------------------------------------")
	# ask question
	print("# Ques. " + str(i + 1) + " of " + str(len_quesList) + " #mistakes = " + str(tokens[len(tokens) - 1]))
	print(ques)
	while(True):
		# ask for user input
		choice = input(">> Enter your answer OR ' ' to show answer OR 'q' to quit: ")
		if(len(choice) > 1):
			user_ans = choice.strip()
			user_ans = user_ans.lower()
			if(user_ans == ans):
				score += 1
				l = len(ans_ticks) - 1
				while(l > 0):
					ans_ticks[l] = ans_ticks[l - 1]
					l = l - 1
				ans_ticks[0] = 0
				print(colored("CORRECT", "green"))
			else:
				l = len(ans_ticks) - 1
				while(l > 0):
					ans_ticks[l] = ans_ticks[l - 1]
					l = l - 1
				ans_ticks[0] = 1
				print(colored("INCORRECT", "red"))
			print("Ans. " + str(ans))
		if(choice == ' '):
			l = len(ans_ticks) - 1
			while(l > 0):
				ans_ticks[l] = ans_ticks[l - 1]
				l = l - 1
			ans_ticks[0] = 1
			print(colored("MISSED", "yellow"))
			print("Ans. " + str(ans))
		if(len(ans_ticks) > 1 and choice != "q"):
			for j in range(len(ans_ticks)):
				if(j == 0):
					tokens = str(ans_ticks[j])
				else:
					tokens = tokens + ">" + str(ans_ticks[j])
			dictLines[q_no] = ans + ">" + ques + ">" + tokens + ">" + str(sum(ans_ticks))
			break
		if(choice == "q"):
			for j in range(len(dictLines)):
				if(j == 0):
					dictData = dictLines[j]
				else:
					dictData = dictData + "\n" + dictLines[j]
			fileReadDict.close()
			fileWriteDict = open(dictionary_path, "w")
			fileWriteDict.write(dictData)
			fileWriteDict.close()
			print("Data Written Successfully")
			perc = (score / float(i)) * 100
			print(colored("Your score is: " + str(score) + " out of " + str(i) + ", " + str(perc) + " %", "blue"))
			print("BYE...")
			sys.exit(0)

# print score
for j in range(len(dictLines)):
	if(j == 0):
		dictData = dictLines[j]
	else:
		dictData = dictData + "\n" + dictLines[j]
fileReadDict.close()
fileWriteDict = open(dictionary_path, "w")
fileWriteDict.write(dictData)
fileWriteDict.close()
print("Data Written Successfully")
print("############################################################################################")
perc = (score / float(len_quesList)) * 100
print(colored("Your score is: " + str(score) + " out of " + str(len_quesList) + ", " + str(perc) + " %", "blue"))
