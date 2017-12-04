f = open("day4input.txt", 'r')
passwords = []
for line in f:
	l = line.strip().split()
	passwords.append(l)
count = 0
for password in passwords:
	valid = True
	for i in range(len(password)):
		for j in range(i+1, len(password)):
			if password[i] == password[j]:
				valid = False
				break;
		if valid == False:
			break;
	if valid:
		count+= 1

print(count)