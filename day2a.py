f = open("day2input.txt", 'r')
spread = []
for line in f:
	l = line.strip().split()
	for x in range(len(l)):
		l[x] = int(l[x])
	spread.append(l)

sum = 0
for l in spread:
	min = l[0]
	max = l[0]
	minloc = 0
	maxloc = 0
	for i in range(len(l)):
		if l[i] < min:
			minloc = i
			min = l[i]
		if l[i] > max:
			maxloc = i
			max = l[i]
	sum+=max-min		

print(sum)