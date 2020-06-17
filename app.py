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
from pynput import keyboard
from pynput.keyboard import Key, Controller

#the words generated for each test
#the words target for each word test
#the time limit of each time test

class CRUCIALVARIABLES():
	genmaxword = 150
	timelimit = 60
	wordsinline = 10

class param():
	letter = []
	keys = [" "]
	endvalue = 0
	endinginfo = [0,0]

def on_press(key):
	global param
	try:
		param.letter.append(key.char)
	except AttributeError:
		param.keys.append('{0}'.format(key))
		if(key == keyboard.Key.esc):
			param.endvalue = 1
			return False
		if(key == keyboard.Key.space and len(param.letter) != 0):
			return False
		if(key == keyboard.Key.backspace and len(param.letter) != 0):
			del param.letter[-1]


def wordRad():
	global CRUCIALVARIABLES
	#have the function that is dedicated to get words off from the txt file
	words = []
	for i in range(CRUCIALVARIABLES.genmaxword):
		word = ""
		temp = os.popen("shuf -n 1 words.txt").read()
		for i in range(len(temp) - 1):
			word = word + temp[i]
		words.append(word)
	return words
#return time is too long


def ui():
	global param
	global CRUCIALVARIABLES
	#put good theme to make the text prinout in the center
	os.system("clear")
	while(param.endvalue == 0):	
		param.letter = []
		param.keys = [" "]
		current = 0
		correct = 0
		starttime = 0
		wordindex = 0
		starttime = time.time()
		words = wordRad()
		while(time.time() - starttime <= CRUCIALVARIABLES.timelimit):
			#output
			resultReturn()
			for i in range(CRUCIALVARIABLES.wordsinline):
				if(wordindex + i == current):
					print("\033[44;33m", words[wordindex + i] ,"\033[m", end = " ")
				else:
					print(words[wordindex + i], end = " ")
			print(" ")
			#input
			wordinput = ""
			while(wordinput == "" and param.keys[-1] != "Key.esc"):
				with keyboard.Listener(on_press=on_press) as listener:
					listener.join()
				for l in range(len(param.letter)):
					wordinput = wordinput + param.letter[l]
			current += 1 
			#var change
			if(wordinput == words[current - 1]):
				correct += 1
			if(param.keys[-1] == "Key.space"):
				param.letter = []
			if(param.endvalue == 1):
				break
			if(current % CRUCIALVARIABLES.wordsinline == 0):
				wordindex += CRUCIALVARIABLES.wordsinline
			os.system("clear")
		if(time.time() - starttime >= CRUCIALVARIABLES.timelimit):
			param.endvalue = 1
		else:
			block = input("press enter button to continue...\n")
			param.endvalue = 0
		
	param.endvalue = 0
	param.endinginfo = [correct, current]

#endinginfo[0] == wordtyped
#endinginfo[1] == wordcompleted
#endinginfo[2] == time used(s))

def resultReturn():
	global CRUCIALVARIABLES
	global param
	os.system("clear")
	if(param.endinginfo != [0,0]):
		wpm = str(int(param.endinginfo[0] / (CRUCIALVARIABLES.timelimit / 60)))
		acc = str(int(param.endinginfo[0] / param.endinginfo[1] * 100))
	else: 
		wpm = 0
		acc = 0
	print("\n =============\n", "| wpm = ", wpm, " |\n", "| acc = ", acc, " |\n", "=============\n")
	#print out results

os.system("clear")
print("welcome to typing practice...")
print("u r aiming 2 type as much as u can in 60s")
parameters = param()
variables = CRUCIALVARIABLES()

while True:
	ui()
	resultReturn()
	choice = input("quit or continue: \npress q + enter to quit,\nenter key to continue...\n")
	if(choice[-1] == "q"):
		print("thank you for using...")
		break

os.system("clear")
		




