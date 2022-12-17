global gnummern
gnummern = { "¬": 1, "∧": 2, "∨": 3, "→": 4, "↔": 5, "∀": 6, "∃": 7, "=": 8, "(": 9, ")": 10, "0": 11, "s": 12, "+": 13, "*": 14, ",": 15, " ": 16 }

def primegen(numprim):
	c = 1
	current = 3 
	primelist = [2]
	while c != int(numprim):
		divisor = int(round((current + 1)**(1/2), 0))
		divcount = 0	
		for i in range(2, divisor+1):
			if (current % int(i)) == 0:
				divcount = divcount + 1
		if divcount == 0:
			primelist.append(current)
			c = c+1
		current = current + 1		
	return(primelist)


def getg(statement):
	c = 1
	iteration = 0

	listprimes = primegen(len(statement))
	for symbol in statement:
		iteration = iteration + 1
		c = c * (listprimes[iteration-1] ** gnummern.get(symbol))
	print(c)

def getstat(gnumber):
	c = 0
	explist = []
	divind = 1
	div = (primegen(divind + 1))[divind]
	final = []
	while (int(gnumber)%2) == 0:
		gnumber = int(gnumber) // 2
		c=c+1
	explist.append(c)
	while (gnumber) > 1:
		d = 0
		while (int(gnumber)%div) == 0:
			gnumber = gnumber // div
			d=d+1
		explist.append(d)
		divind = divind + 1	
		div = (primegen(divind + 1))[divind]
	for exp in explist:
		final.append(list(gnummern)[exp-1])
	print(''.join(final))

def main():
	choice = input('Wollen Sie a) Aussage -> Gödelnummer oder b) Gödelnummer -> Aussage? a/b ')
	if choice == 'a':
		try:
			getg(input('statement: '))
		except Exception as e:
				print(e)
	elif choice == 'b':
		try:
			getstat(int(input('Gödelnummer ')))
		except Exception as e:
				print(e)

if __name__ == '__main__':
	c = 0
	while c == 0:
		main()
		stop = input('stop? y/n ')
		if stop == 'y':
			c = 1	
				