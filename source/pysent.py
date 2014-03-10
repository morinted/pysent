#!/usr/bin/python
# coding: utf-8

from __future__ import division

import sys, getopt, re, time

def main(argv):
	col=70
	row=22
	inputfile=''
	try:
		opts, args = getopt.getopt(argv,"hi")
	except getopt.GetoptError:
		print 'Usage: pysent.py -i <inputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'Usage: pysent.py -i <inputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = args[0]

	if col==70 and row==22:
		#Draw the logo as startup if dimensions are default
		pysent_logo = getLogo()
		for x in range(0,len(pysent_logo)):
			sys.stdout.write(pysent_logo[x])
			time.sleep(0.001)
			sys.stdout.flush()
	else:
		#Draw a box if different dimensions
		for y in range(0, row):
			for x in range(0,col):
				sys.stdout.write('█')
				time.sleep(0.001)
				sys.stdout.flush()
			sys.stdout.write('\n')
	

	txt = open(inputfile, 'r')
	txt = txt.read()

	#remove secondary lines (anything tabbed)
	txt = re.sub('^\t.*$', '', txt, count=0, flags=re.MULTILINE)
	txt = re.sub('^$', '', txt, count=0, flags=re.MULTILINE)
	slides = re.split("-----+", txt)
	totalSlides = len(slides)

	#create titles and points
	titles=[]
	points=[]
	for slide in slides:
		titles.append(re.findall('^#.*$', slide, flags=re.MULTILINE))
		points.append(re.findall('(^- .*$|^\d+.*$)', slide, flags=re.MULTILINE))
	
	prompt ='Loaded slideshow with', totalSlides, ' slides. Press Enter to start.'
	userinput = raw_input(prompt)

	#play sideshow
	x = 0
	while x < totalSlides:
		for r in range (0, row):
			print
			time.sleep(.01)
		linecount = 0;

		titleLines = []
		titleLine = ['','','','','']

		titleWords = str.split(titles[x][0])

		for titleWord in titleWords[1:]:
			ascii_word = [' ',' ',' ',' ',' ']

			#Get word, character by character
			for charX in range(0,len(titleWord)):
				ascii_char = getChar(titleWord[charX])
				for line in range(0,5):
					if ascii_char[line][0] == '|':
						ascii_word[line]=ascii_word[line][:-1] + '|'
					ascii_word[line] += ascii_char[line][1:]

			#Add word to title line.
			if len(ascii_word[0]) + len(titleLine[0]) + 2 > 70:
				titleLines.append(list(titleLine))

				titleLine = ascii_word
				for line in range(0,5):
					titleLine[line] = '  ' + titleLine[line]
			else:
				for line in range(0,5):
					titleLine[line] += '  ' + ascii_word[line]
		
		#Append last word generated.
		titleLines.append(list(titleLine))
		for tLine in titleLines:
			for line in range(0,5):
				print tLine[line] 
				time.sleep(.02)
		sys.stdout.flush()

		print

		for point in points[x]:
			words = str.split(point)
			paragraph = ''
			lines = 2
			lineLength = 0
			for word in words:
				if lineLength+len(word) > 70:
					lineLength = len(word)+5
					lines+=1
					paragraph+='\n    ' + word + ' '
				elif lineLength+len(word) == 70:
					lineLength+=len(word)
					paragraph+=word
				else:
					lineLength+=len(word)+1
					paragraph+=word + ' '
			for y in range (0, len(paragraph)):
				sys.stdout.write(paragraph[y])
				time.sleep(.01)
				sys.stdout.flush()

			print '\n'
			if (point is points[x][len(points[x])-1]):
				if x < totalSlides-1:
					progress = '[Slide '+str(x+1)+' out of '+str(totalSlides)+']'
					edges = (col-len(progress))//2
					for z in range(0,col):
						if z < edges or z >= (edges + len(progress)):
							sys.stdout.write('-')
						else:
							i = z%edges
							sys.stdout.write(progress[i])
				else:
					for z in range(0,col):
						sys.stdout.write('=')
			userinput = raw_input()
			if userinput == 'p':
				x-=2
				if x < -1:
					x=-1
				break
		
		x+=1

	#Draw a box to end slideshow
	for y in range(0, row):
		for x in range(0,col):
			sys.stdout.write('█')
			time.sleep(0.001)
			sys.stdout.flush()
		sys.stdout.write('\n')

def getChar(char): #get ASCII A
	#Font: "Rectangles" from FIGlet. http://www.figlet.org/fontdb_example.cgi?font=rectangles.flf
	#Added in implementation for (, ), modified for height-limit of 5.
	ascii = ''
	if char=='a':
		ascii = ['     ',' ___ ',"| .'|",'|__,|','     ']
	elif char=='b':
		ascii = [' _   ','| |_ ','| . |','|___|','     ']
	elif char=='c':
		ascii = ['     ',' ___ ','|  _|','|___|','     ']
	elif char=='d':
		ascii = ['   _ ',' _| |','| . |','|___|','     ']
	elif char=='e':
		ascii = ['     ',' ___ ',"| -_|",'|___|','     ']
	elif char=='f':
		ascii = [' ___ ','|  _|',"|  _|",'|_|  ','     ']
	elif char=='g':
		ascii = ['     ',' ___ ',"| . |",'|_  |','|___|']
	elif char=='h':
		ascii = [' _   ','| |_ ',"|   |",'|_|_|','     ']
	elif char=='i':
		ascii = [' _ ','|_|',"| |",'|_|','   ']	
	elif char=='j':
		ascii = ['   _ ','  |_|',"  | |",' _| |','|___|']
	elif char=='k':
		ascii = [' _   ','| |_ ',"| '_|",'|_,_|','     ']
	elif char=='l':
		ascii = [' _ ','| |',"| |",'|_|','   ']
	elif char=='m':
		ascii = ['       ',' _____ ','|     |',"|_|_|_|",'       ']
	elif char=='n':
		ascii = ['     ',' ___ ','|   |',"|_|_|",'     ']
	elif char=='o':
		ascii = ['     ',' ___ ','| . |',"|___|",'     ']
	elif char=='p':
		ascii = ['     ',' ___ ','| . |',"|  _|",'|_|  ']
	elif char=='q':
		ascii = ['     ',' ___ ','| . |',"|_  |",'  |_|']
	elif char=='r':
		ascii = ['     ',' ___ ','|  _|',"|_|  ",'     ']
	elif char=='s':
		ascii = ['     ',' ___ ','|_ -|',"|___|",'     ']
	elif char=='t':
		ascii = [' _   ','| |_ ','|  _|',"|_|  ",'     ']
	elif char=='u':
		ascii = ['     ',' _ _ ','| | |',"|___|",'     ']
	elif char=='v':
		ascii = ['     ',' _ _ ','| | |'," \_/ ",'     ']
	elif char=='w':
		ascii = ['       ',' _ _ _ ','| | | |',"|_____|",'       ']
	elif char=='x':
		ascii = ['     ',' _ _ ',"|_'_|","|_,_|",'     ']
	elif char=='y':
		ascii = ['     ',' _ _ ',"| | |","|_  |",'|___|']
	elif char=='z':
		ascii = ['     ',' ___ ',"|- _|","|___|",'     ']
	elif char=='A':
		ascii = [' _____ ','|  _  |','|     |','|__|__|','       ']
	elif char=='B':
		ascii = [' _____ ','| __  |','| __ -|','|_____|','       ']
	elif char=='C':
		ascii = [' _____ ','|     |','|   --|','|_____|','       ']
	elif char=='D':
		ascii = [' ____  ','|    \ ','|  |  |','|____/ ','       ']
	elif char=='E':
		ascii = [' _____ ','|   __|','|   __|','|_____|','       ']
	elif char=='F':
		ascii = [' _____ ','|   __|','|   __|','|__|   ','       ']
	elif char=='G':
		ascii = [' _____ ','|   __|','|  |  |','|_____|','       ']
	elif char=='H':
		ascii = [' _____ ','|  |  |','|     |','|__|__|','       ']
	elif char=='I':
		ascii = [' _____ ','|_   _|','__| |__','|_____|','       ']
	elif char=='J':
		ascii = ['    __ ',' __|  |','|  |  |','|_____|','       ']
	elif char=='K':
		ascii = [' _____ ','|  |  |','|    -|','|__|__|','       ']
	elif char=='L':
		ascii = [' __    ','|  |   ','|  |__ ','|_____|','       ']
	elif char=='M':
		ascii = [' _____ ','|     |','| | | |','|_|_|_|','       ']
	elif char=='N':
		ascii = [' _____ ','|   | |','| | | |','|_|___|','       ']
	elif char=='O':
		ascii = [' _____ ','|     |','|  |  |','|_____|','       ']
	elif char=='P':
		ascii = [' _____ ','|  _  |','|   __|','|__|   ','       ']
	elif char=='Q':
		ascii = [' _____ ','|     |','|  |  |','|__  _|','   |__|']
	elif char=='R':
		ascii = [' _____ ','| __  |','|    -|','|__|__|','       ']
	elif char=='S':
		ascii = [' _____ ','|   __|','|__   |','|_____|','       ']
	elif char=='T':
		ascii = [' _____ ','|_   _|','  | |  ','  |_|  ','       ']
	elif char=='U':
		ascii = [' _____ ','|  |  |','|  |  |','|_____|','       ']
	elif char=='U':
		ascii = [' _____ ','|  |  |','|  |  |',' \___/ ','       ']
	elif char=='W':
		ascii = [' _ _ _ ','| | | |','| | | |','|_____|','       ']
	elif char=='X':
		ascii = [' __ __ ','|  |  |','|-   -|','|__|__|','       ']
	elif char=='Y':
		ascii = [' __ __ ','|  |  |','|_   _|','  |_|  ','       ']
	elif char=='Z':
		ascii = [' _____ ','|__   |','|   __|','|_____|','       ']
	elif char=='-':
		ascii = ['     ',' ___ ','|___|','     ','     ']
	elif char==' ':
		ascii = ['  ','  ','  ','  ','  ']
	elif char=="'":
		ascii = [' _ ','|_|','   ','   ','   ']
	elif char=='"':
		ascii = [' _ _ ','|_|_|','     ','     ','     ']
	elif char=='.':
		ascii = ['   ','   ',' _ ','|_|','   ']
	elif char=='?':
		ascii = [' _____ ','|___  |','  |  _|','  |_|  ','  |_|  ']
	elif char==',':
		ascii = ['   ','   ','   ',' _ ','/_/']
	elif char=='(':
		ascii = ['  __ ',' / / ','| |  ','| |  ',' \\_\\ ']
	elif char==')':
		ascii = [' __  ',' \\ \\ ','  | |','  | |',' /_/ ']
	elif char=='!':
		ascii = [' __ ','|  |','|  |','|__|','|__|']
	return ascii

def getLogo():
	return('######################################################################\n######################################################################\n######################################################################\n######################################################################\n######################################################################\n######################################################################\n#####         #   ###   ##         ##         ##    #####   #         \n####    ###  ###   #   ##   ########   ########     ####   #####   ###\n###    ###  #####     ##   ########   ########   #  ###   #####   ####\n##         #######   ##         ##        ###   ##  ##   #####   #####\n#    ############   ########   ##   ########   ###  #   #####   ######\n    ############   ########   ##   ########   ####     #####   #######\n   ############   ##         ##          #   #####    #####   ########\n######################################################################\n######################################################################\n######################################################################\n###################   A command-line presentation   ##################\n###################     tool written in Python.     ##################\n######################################################################\n######################################################################\n######################################################################\n######################################################################')
if __name__ == "__main__":
	main(sys.argv[1:])