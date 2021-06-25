print("Please type the message you want to encrypt. Please, no spaces.")
a = input()
b = []
count = 0
print("Lousy encryption is in progress please wait.")
for letters in a:
	if a[count] == "a" or a[count] == "A":
		b.append("b")
		count += 1
	elif a[count] == "b" or a[count]== "B":
		b.append("c")
		count += 1
	elif a[count] == "c" or a[count]== "C":
		b.append("d")
		count += 1
	elif a[count] == "d" or a[count] == "D":
		b.append("e")
		count += 1
	elif a[count] == "e" or a[count] == "E":
		b.append("f")
		count += 1
	elif a[count] == "f" or a[count] == "F":
		b.append("g")
		count += 1
	elif a[count] == "g" or a[count] == "G":
		b.append("h")
		count += 1
	elif a[count] == "h" or a[count] == "H":
		b.append("i")
		count += 1
	elif a[count] == "i"or a[count] == "I":
		b.append("j")
		count += 1
	elif a[count] == "j"or a[count] == "J":
		b.append("k")
		count += 1
	elif a[count] == "k"or a[count] == "K":
		b.append("l")
		count += 1
	elif a[count] == "l"or a[count] == "L":
		b.append("m")
		count += 1
	elif a[count] == "m"or a[count] == "M":
		b.append("n")
		count += 1
	elif a[count] == "n"or a[count] == "N":
		b.append("o")
		count += 1
	elif a[count] == "o"or a[count] == "O":
		b.append("p")
		count += 1
	elif a[count] == "p"or a[count] == "P":
		b.append("q")
		count += 1
	elif a[count] == "q"or a[count] == "Q":
		b.append("r")
		count += 1
	elif a[count] == "r"or a[count] == "R":
		b.append("s")
		count += 1
	elif a[count] == "s"or a[count] == "S":
		b.append("t")
		count += 1
	elif a[count] == "t"or a[count] == "T":
		b.append("u")
		count += 1
	elif a[count] == "u"or a[count] == "U":
		b.append("v")
		count += 1
	elif a[count] == "v"or a[count] == "V":
		b.append("w")
		count += 1
	elif a[count] == "w"or a[count] == "W":
		b.append("x")
		count += 1
	elif a[count] == "x"or a[count] == "X":
		b.append("y")
		count += 1
	elif a[count] == "y"or a[count] == "Y":
		b.append("z")
		count += 1
	elif a[count] == "z"or a[count] == "Z":
		b.append("a")
		count += 1
print(b)