f = open("day5input.txt", 'r')
instructions = []
for line in f:
	l = line.strip()
	instructions.append(int(l))

count = 0
i = 0
while i > -1 and i < len(instructions):
	newi = i+instructions[i]
	if instructions[i] > 2:
		instructions[i] -= 1
	else:
		instructions[i]+=1
	count+=1
	i = newi
print(count)