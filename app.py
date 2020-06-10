import random
import os

english = ["the", "be", "of", "and", "a", "to", "in", "he", "have", 
"it", "that", "for", "they", "I", "with", "as", "not", "on", "she", 
"at", "by", "this", "we", "you", "do", "but", "from", "or", "which", 
"one", "would", "all", "will", "there", "say", "who", "make", 
"when", "can", "more", "if", "no", "man", "out", "other", "so", 
"what", "time", "up", "go", "about", "than", "into", "could", 
"state", "only", "new", "year", "some", "take", "come", "these", 
"know", "see", "use", "get", "like", "then", "first", "any", "work", 
"now", "may", "such", "give", "over", "think", "most", "even", 
"find", "day", "also", "after", "way", "many", "must", "look", 
"before", "great", "back", "through", "long", "where", "much", 
"should", "well", "people", "down", "own", "just", "because", "good", 
"each", "those", "feel", "seem", "how", "high", "too", "place", 
"little", "world", "very", "still", "nation", "hand", "old", "life", 
"tell", "write", "become", "here", "show", "house", "both", 
"between", "need", "mean", "call", "develop", "under", "last", 
"right", "move", "thing", "general", "school", "never", "same", 
"another", "begin", "while", "number", "part", "turn", "real", 
"leave", "might", "want", "point", "form", "off", "child", "few", 
"small", "since", "against", "ask", "late", "home", "interest", 
"large", "person", "end", "open", "public", "follow", "during", 
"present", "without", "again", "hold", "govern", "around", 
"possible", "head", "consider", "word", "program", "problem", 
"however", "lead", "system", "set", "order", "eye", "plan", "run", 
"keep", "face", "fact", "group", "play", "stand", "increase", 
"early", "course", "change", "help", "line"]

#from https://github.com/briano1905/typings/blob/master/texts/random.json
#possibly change to "shuf" function under a txt file

CRUCIALVARIABLES = [1000, 50, 60]
#the words generated for each test, the words target for each word test, the time limit of each time test
#possibly also put into a seperate file

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

#endinginfo[0] == wordtyped, endinginfo[1] == wordcompleted, endinginfo[2] == time used(s))

def gui(words, testtype):
	if(testtype % 2 == 0):
		#place limits for time
		print("time")
	else:
		current = 0
		for i in range(0, CRUCIALVARIABLES[1], 5):
			#output
			for j in range(5):
				if(i * 5 + j == current):
					print("\033[44;33m", words[i * 5 + j] ,"\033[m")
				else:
					print(words[i * 5 + j])
			#input
			for j in range(5):
				#event listener
				print("input")
		inputword = input("input: ")
	endinginfo = [100, 89, 63]
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




