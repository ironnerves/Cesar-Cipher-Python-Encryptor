#Hey! Stop looking at my code!
#Well, this is a lousy piece of shit code,
#So do whatever you want to this crap.
print("Please type the message you want to encrypt. Please, no spaces.")
a = input()
avaliable_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
print("Please Type Amount Of letter Displacement (Less Or Equal To 25, Preferably)")
AOLC = int(input())
b = []
count = 0
print("Lousy encryption is in progress please wait.")
for letters in a:
	if a[count] == "a" or a[count] == "A":
		b.append(avaliable_letters[AOLC])
		count += 1
	elif a[count] == "b" or a[count]== "B":
		b.append(avaliable_letters[1 + AOLC])
		count += 1
	elif a[count] == "c" or a[count]== "C":
		b.append(avaliable_letters[2 + AOLC])
		count += 1
	elif a[count] == "d" or a[count] == "D":
		b.append(avaliable_letters[3 + AOLC])
		count += 1
	elif a[count] == "e" or a[count] == "E":
		b.append(avaliable_letters[4 + AOLC])
		count += 1
	elif a[count] == "f" or a[count] == "F":
		b.append(avaliable_letters[5 + AOLC])
		count += 1
	elif a[count] == "g" or a[count] == "G":
		b.append(avaliable_letters[6 + AOLC])
		count += 1
	elif a[count] == "h" or a[count] == "H":
		b.append(avaliable_letters[7 + AOLC])
		count += 1
	elif a[count] == "i"or a[count] == "I":
		b.append(avaliable_letters[8 + AOLC])
		count += 1
	elif a[count] == "j"or a[count] == "J":
		b.append(avaliable_letters[9 + AOLC])
		count += 1
	elif a[count] == "k"or a[count] == "K":
		b.append(avaliable_letters[10 + AOLC])
		count += 1
	elif a[count] == "l"or a[count] == "L":
		b.append(avaliable_letters[11 + AOLC])
		count += 1
	elif a[count] == "m"or a[count] == "M":
		b.append(avaliable_letters[12 + AOLC])
		count += 1
	elif a[count] == "n"or a[count] == "N":
		b.append(avaliable_letters[13 + AOLC])
		count += 1
	elif a[count] == "o"or a[count] == "O":
		b.append(avaliable_letters[14 + AOLC])
		count += 1
	elif a[count] == "p"or a[count] == "P":
		b.append(avaliable_letters[15 + AOLC])
		count += 1
	elif a[count] == "q"or a[count] == "Q":
		b.append(avaliable_letters[16 + AOLC])
		count += 1
	elif a[count] == "r"or a[count] == "R":
		b.append(avaliable_letters[17 + AOLC])
		count += 1
	elif a[count] == "s"or a[count] == "S":
		b.append(avaliable_letters[18 + AOLC])
		count += 1
	elif a[count] == "t"or a[count] == "T":
		b.append(avaliable_letters[19 + AOLC])
		count += 1
	elif a[count] == "u"or a[count] == "U":
		b.append(avaliable_letters[20 + AOLC])
		count += 1
	elif a[count] == "v"or a[count] == "V":
		b.append(avaliable_letters[21 + AOLC])
		count += 1
	elif a[count] == "w"or a[count] == "W":
		b.append(avaliable_letters[22 + AOLC])
		count += 1
	elif a[count] == "x"or a[count] == "X":
		b.append(avaliable_letters[23 + AOLC])
		count += 1
	elif a[count] == "y"or a[count] == "Y":
		b.append(avaliable_letters[24 + AOLC])
		count += 1
	elif a[count] == "z"or a[count] == "Z":
		b.append(avaliable_letters[25 + AOLC])
		count += 1
print(b)
