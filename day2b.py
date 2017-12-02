f = open("day2input.txt", 'r')
spread = []
for line in f:
	l = line.strip().split()
	for x in range(len(l)):
		l[x] = int(l[x])
	spread.append(l)

sum = 0
for l in spread:
	for i in range(len(l)):
		for j in range(i+1, len(l)):
			if l[i] % l[j] == 0:
				sum += l[i]/l[j]
			if l[j] % l[i] == 0:
				sum += l[j]/l[i]

print(sum)