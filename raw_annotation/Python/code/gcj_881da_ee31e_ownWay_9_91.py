import random
def main():
	T=eval(input())
	for i in range (T):
		N=eval(input())
		s=input()
		print("Case #"+str(i+1)+":", end=' ')
		ownWay(s,N)
def ownWay(s,n):
	maze=[]
	for i in range (n):
		maze.append([])
		for j in range (n):
			maze[i].append([])
			for k in range (2):
				if k==0:
					maze[i][j].append(i)
				else:
					maze[i][j].append(j)
	l=list(s)
	c_l=[]    
	for i in range (1):
		c_l.append([])
		for j in range(2*n-1):
			c_l[i].append([])
			for k in range (2):
				c_l[i][j].append(0)
	x=0
	y=0
	c_l[0][0][0]=maze[x][y][0]
	c_l[0][0][1]=maze[x][y][1]
	for i in range(2*n-2):
		if l[i]=='S':
			y=y+1
			c_l[0][i+1][1]=maze[x][y][1]
			c_l[0][i+1][0]=maze[x][y][0]
		if l[i]=='E':
			x=x+1
			c_l[0][i+1][0]=maze[x][y][0]
			c_l[0][i+1][1]=maze[x][y][1]       
	check=True
	random.shuffle(l)
	c_l1=[]
	for i in range (1):
		c_l1.append([])
		for j in range(2*n-1):
			c_l1[i].append([])
			for k in range (2):
				c_l1[i][j].append(0)
	x1=0
	y1=0
	c_l1[0][0][0]=maze[x1][y1][0]
	c_l1[0][0][1]=maze[x1][y1][1]
	for i in range(2*n-2):
		if l[i]=='S':
			y1=y1+1
			c_l1[0][i+1][1]=maze[x1][y1][1]
			c_l1[0][i+1][0]=maze[x1][y1][0]
		if l[i]=='E':
			x1=x1+1
			c_l1[0][i+1][0]=maze[x1][y1][0]
			c_l1[0][i+1][1]=maze[x1][y1][1]
	while check:
		check=False
		for i in range(2*n-2):
			if (c_l[0][i][0]==c_l1[0][i][0]) and (c_l[0][i][1]==c_l1[0][i][1]) and (c_l[0][i+1][0]==c_l1[0][i+1][0]) \
				and (c_l[0][i+1][1]==c_l1[0][i+1][1]):
				check=True
		if check:
			random.shuffle(l)
			c_l1=[]
			for i in range (1):
				c_l1.append([])
				for j in range(2*n-1):
					c_l1[i].append([])
					for k in range (2):
						c_l1[i][j].append(0)
			x1=0
			y1=0
			c_l1[0][0][0]=maze[x1][y1][0]
			c_l1[0][0][1]=maze[x1][y1][1]
			for i in range(2*n-2):
				if l[i]=='S':
					y1=y1+1
					c_l1[0][i+1][1]=maze[x1][y1][1]
					c_l1[0][i+1][0]=maze[x1][y1][0]
				if l[i]=='E':
					x1=x1+1
					c_l1[0][i+1][0]=maze[x1][y1][0]
					c_l1[0][i+1][1]=maze[x1][y1][1]
	print(''.join(l))
main()