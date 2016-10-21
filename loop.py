#! /usr/bin/python

number = 23
loop = True

while loop:
	guess = int(raw_input("Enter a number:")
	if guess == number:
   		print "Contralations,you guessed it."
		loop = False
	elif guess < number:
		print "No,it's bigger than that."
	else:
		print "no,it's lower than that."
else:
	print "The loop is over."
print "Done."
