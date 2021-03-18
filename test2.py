import math

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
		return i,j,d

def all_posi(m,i,j):
	#print("{} {}".format(i,j))
	answer = []
	for x in range(4):
		posi_n = next_position(m,i,j,x+1)
		if not posi_n == -1:
			answer.append(posi_n)
	return answer

def find_distance(u,v):
	x = u[0] - v[0]
	y = u[1] - v[1]
	dis = math.pow(x,2) + math.pow(y,2)
	return math.sqrt(dis)
	
#m = [[0,0,0,0,0,0,0,0,1,1],
#	 [0,0,0,0,0,1,0,0,0,0],
#	 [1,0,1,0,0,0,1,0,0,0],
#	 [1,0,0,1,0,0,0,0,0,1],
#	 [0,1,1,1,1,0,0,0,0,1],
#	 [0,1,0,0,0,0,0,0,0,1],
#	 [0,0,0,0,0,0,0,1,0,0],
#	 [1,0,0,0,0,0,0,0,1,0],
#	 [1,0,0,1,0,0,0,1,0,1],
#	 [1,1,0,0,0,0,0,0,0,0]]

m = [[0,0,0,0,0,0,0,0,1,1],
	 [0,0,0,0,0,1,0,0,0,0],
	 [1,0,1,0,0,0,1,0,0,0],
	 [1,0,0,1,0,0,0,0,0,1],
	 [0,1,1,1,1,0,0,0,0,1],
	 [0,1,0,0,0,0,1,0,0,1],
	 [0,0,0,0,0,0,0,0,0,0],
	 [1,0,0,0,0,0,0,1,1,0],
	 [1,0,0,1,0,0,0,1,0,1],
	 [1,1,0,0,0,0,0,0,0,0]]

#answer = all_posi(m,3,10)
#for row in m:
#	print(row)
	
#print(answer)

#for posi in answer:
#	print(find_distance([3,4],posi))
#print(find_distance([1,1],[3,3]))
#print(find_distance([1,1],[1,3]))
path = []
current_post = [3,10,3]
target_post = [3,4]
path.append(current_post)

for _ in range(6):
	closets_dis = float('inf')
	answer = all_posi(m,current_post[0],current_post[1])
	print(answer)
	for posi in answer:
		current_dis = find_distance(target_post,posi)
		if current_dis<closets_dis:
			current_post = posi
			closets_dis = current_dis
	path.append(current_post)
	for row in m:
		print(row)
print(path)