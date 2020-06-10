#author: dealthy
#referenced: 
#https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python#4810595
#https://stackoverflow.com/questions/35731194/how-to-highlight-a-word-found-in-a-text-file#35731408
#https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution#1557584
#https://stackoverflow.com/questions/11918999/key-listeners-in-python#11919074
#https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard

import random
import os
import time
import sys
import termios
import contextlib

CRUCIALVARIABLES = [1000, 50, 60]
#the words generated for each test
#the words target for each word test
#the time limit of each time test


def wordRad():
	#have the function that is dedicated to get words off from the txt file
	words = []
	for i in range(CRUCIALVARIABLES[0]):
		word = ""
		temp = os.popen("shuf -n 1 words.txt").read()
		for i in range(len(temp) - 1):
			word = word + temp[i]
		words.append(word)
	return words
#return time is too long

#endinginfo[0] == wordtyped
#endinginfo[1] == wordcompleted
#endinginfo[2] == time used(s))

def gui(words, testtype):
	#put good theme to make the text prinout in the center
	os.system("clear")
	if(testtype % 2 == 0):
		#place limits for time
		print("time")
	else:
		current = 0
		correct = 0
		starttime = time.time()
		for i in range(0, CRUCIALVARIABLES[1], 5):
			for j in range(5):
				#output
				for k in range(5):
					wordindex = i + k
					if(wordindex == current):
						print("\033[44;33m", words[wordindex] ,"\033[m", end = " ")
					else:
						print(words[wordindex], end = " ")
				print(" ")
				#print(wordindex,  current, correct, i)
				#switch to event listener
				#using pynput
				wordinput = input("input: ")
				#need to fix: terminates each input by space instead of enter
				if(wordinput == words[current]):
					correct += 1
				current += 1
				os.system("clear")
		endinginfo = [CRUCIALVARIABLES[1], correct, int(time.time() - starttime)]
	return endinginfo

def resultReturn(endinginfo):
	wpm = int(endinginfo[1] / endinginfo[2] * 60)
	if(wpm / 100 <= 0):
		wpm = wpm + " "
	acc = int(endinginfo[1] / endinginfo[0] * 100)
	if(acc / 100 <= 0):
		acc = acc + " "
	print(" ==============\n", "| wpm = ", wpm, " |\n", "| acc = ", acc, " |\n", "==============\n\n\n")
	#print out results

print("welcome to typing practice...")
print("you can either set 60 seconds or 50 words as your target")
print("60 seconds test is set to default")
status = 1

while True:
	resultReturn(gui(wordRad(), status))
	choice = input("quit or continue: \nuse q to quit,\nuse s to switch modes,\nother keys to continue...\n")
	if(choice == "q"):
		print("thank you for using...")
		os.system('clear')
		break
	if(choice == "s"):
		status += 1
		os.system('clear')
	else:
		continue




