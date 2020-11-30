cash=5000
while True: 
	print "You may bid up to five valuable paintings."
	print "Start with $5000."
	print "Then, try to sell your collection for as much as possible."

	paintings = 0

	import random
	store = []

	#buying phase
	for x in range(5):
		print "Your balance:" , cash
		print "painting" ,(x+1) , "is up for sale"
		s = int(raw_input("what is your bid?"))
		if s > cash:
			continue
		opponent = random.randint(150,1150)
		print "another collector has bid " , opponent
		if s >= opponent:
			print "you bought it!"
			paintings += 1
			cash -= s
			store.append(s)
		else:
			print "sorry, you lost it"
	#selling phrase	
	for y in range(paintings):
		print "you may now sell your painting", paintings
		offers = random.randint(1,6)
		for z in range(offers):
			bid = random.randint(500,2500)
			print "you've been offered $", bid, "for this painting. You paid $", store[y], "for it. Do you accept? (y/n)"
			a = raw_input("y/n")
			if a == "y":
				cash += bid
				break
			else:
				print "Sorry, that was your last chance. You have to keep that painting!"

		print "Sorry, that was your last chance. You have to keep that painting!"
			
	#play again	
	print "you started with $5000. You finish with $" ,cash
	p = raw_input("Play again? (y/n)")

	if p == "n":
		break
		

	