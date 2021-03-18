def next_position(m,i,j,d):
	if not m[j-1][i-1] == 1:
		m[j-1][i-1]=5
	else:
		#print("Error: Position Error")
		return -1
	#print("{} {} {}".format(i,j,d))
	if d == 1:
		j += 1
	elif d == 2:
		i += 1
	elif d == 3:
		j -= 1 
	else:
		i -= 1
	if j>10 or i>10 or i<1 or j<1 or m[j-1][i-1] == 1:
		#print("Error: Out of Range or Obstacle")
		return -1
	else:
		m[j-1][i-1]=5
		#print("{} {} {}".format(i,j,d))
		return i,j

def all_posi(m,i,j):
	print("{} {}".format(i,j))
	answer = []
	for x in range(4):
		posi_n = next_position(m,i,j,x)
		if not posi_n == -1:
			answer.append(posi_n)
	print(answer)
	
m = [[0,0,0,0,0,0,0,0,1,1],
	 [0,0,0,0,0,1,0,0,0,0],
	 [1,0,1,0,0,0,1,0,0,0],
	 [1,0,0,1,0,0,0,0,0,1],
	 [0,1,1,1,1,0,0,0,0,1],
	 [0,1,0,0,0,0,0,0,0,1],
	 [0,0,0,0,0,0,0,1,0,0],
	 [1,0,0,0,0,0,0,0,1,0],
	 [1,0,0,1,0,0,0,1,0,1],
	 [1,1,0,0,0,0,0,0,0,0]]

all_posi(m,7,1)
for row in m:
	print(row)