def isAnagram(string1, string2):
	if(len(string1) != len(string2)):
		return False
	for x in string1:
		found = False
		for i in range(len(string2)):
			if x == string2[i]:
				found = True
				break;
		string2 = string2[:i] + string2[i+1:]
		if found == False:
			return False
	return True

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
			if isAnagram(password[i],password[j]):
				valid = False
				break;
		if valid == False:
			break;
	if valid:
		count+= 1

print(count)