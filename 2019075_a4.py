import random
import time
import os
import copy
megagrid=[]
def clean():
	if os.name=="nt":
		_=os.system('cls')
	return
class grid():
	def __init__(self,n,start,goal,myObstacles,myRewards):
		'''class grid has the given parameters'''
		'''the constructor has been overwritten after seeing the attributes the goal,staryt, reward and obstacle
		position are printed'''
		self.n=n
		self.start=start
		self.goal=goal
		self.myObstacles=myObstacles
		self.myRewards=myRewards
		global megagrid
		#obstacle repalce
		for k in self.myObstacles:
			i=k.x
			j=k.y
			megagrid[i][j]="#"
		#reward replace
		for k in self.myRewards:
			i=k.x
			j=k.y
			megagrid[i][j]=k.value
		#previous path replace
		for i in range(self.n):
			for j in range(self.n):
				if(megagrid[i][j]=="X"):
					megagrid[i][j]="."
		#start and endpoint
		i=self.start.x
		j=self.start.y
		megagrid[i][j]="O"
		i=self.goal.x
		j=self.goal.y
		megagrid[i][j]="D"
		for i in range(self.n):
			for j in range(self.n):
				print(megagrid[i][j],end=" ")
			print()
	def showGrid(self):
			'''The show grid method is used by make move to print the corresponding move'''
			'''Energy is reduced and returned'''
			global megagrid
			global player1
			player1.energy-=1
			clean()
			megagrid[player1.x][player1.y]="O"
			for i in self.myObstacles:
				if(i.x==player1.x and i.y==player1.y):
					player1.energy-=4*self.n
					self.myObstacles.remove(i)
			for i in self.myRewards:
				if(i.x==player1.x and i.y==player1.y):
					player1.energy+=i.value*self.n
					self.myRewards.remove(i)
			print("ENERGY: ",player1.energy)
			for i in range(self.n):
				for j in range(self.n):
					print(megagrid[i][j],end=" ")
				print()
			time.sleep(0.5)
			return player1.energy
	def rotateAnticlockwise(self,no):
		global megagrid
		global player1
		'''rotation in anticlockwise direction'''
		energy1=player1.energy
		megagrid1=copy.deepcopy(megagrid)
		myob=copy.deepcopy(self.myObstacles)
		myrew=copy.deepcopy(self.myRewards)
		k=self.n
		for r in range(no):
			temp=0
			energy1=energy1-(k//3)
			'''energy is reduced and swapping takes place first'''
			newe=[]
			for i in range (len(megagrid1)):
				col=[]
				for j in range (len(megagrid1)):
					col.append(megagrid1[j][len(megagrid1)-1-i])
					if(col[j]=="#"):
						myob.remove(point(j,len(megagrid1)-1-i))
					if(type(col[j])==int):
						myrew.remove(Reward(j,len(megagrid1)-1-i,int(megagrid1[j][len(megagrid1)-1-i])))
				newe.append(col)
				''' the destination and position are initialised and it next checks for any discrepancies'''
			for i in range (len(newe)):
				for j in range (len(newe)):
					if(newe[i][j]=="D"):
						newe[i][j]="."
					elif(newe[i][j]=="O"):
						newe[i][j]="."
			if(not((newe[self.start.x][self.start.y]==".") and ( newe[self.goal.x][self.goal.y]=="."))):
						temp+=1
						'''The goal/initial position clashing is noted and loop proceeds for the next iteration'''
			for i in range (len(newe)):
				for j in range (len(newe)):
					if(newe[i][j]=="#"):
						newe[i][j]="."
						myob.append(point(i,j))
					elif(type(newe[i][j])==int):
						myrew.append(Reward(i,j,int(newe[i][j])))
						newe[i][j]="."
			megagrid1=copy.deepcopy(newe)
			'''If goal/original coincides with obstacle reward'''
		if(temp>0):
			print("CANNOT ROTATE GRID")
			time.sleep(5)
			return megagrid,player1.energy
		else:					
			self.myRewards=myrew
			self.myObstacles=myob
			player1.energy=energy1
			return newe,player1.energy
	def rotateClockwise(self,no):
		'''Exact similar function as anticlockwise the swapping is just a bit different'''
		global megagrid
		global player1
		energy1=player1.energy
		megagrid1=copy.deepcopy(megagrid)
		myob=copy.deepcopy(self.myObstacles)
		myrew=copy.deepcopy(self.myRewards)
		k=self.n
		for r in range(no):
			temp=0
			energy1=energy1-(k//3)
			newe=[]
			for i in range (len(megagrid1)):
				col=[]
				for j in range (len(megagrid1)):
					col.append(megagrid1[len(megagrid1)-1-j][i])
					if(col[j]=="#"):
						myob.remove(point(len(megagrid1)-1-j,i))
					if(type(col[j])==int):
						myrew.remove(Reward(len(megagrid1)-1-j,i,int(megagrid1[len(megagrid1)-1-j][i])))
				newe.append(col)
			for i in range (len(newe)):
				for j in range (len(newe)):
					if(newe[i][j]=="D"):
						newe[i][j]="."
					elif(newe[i][j]=="O"):
						newe[i][j]="."
			if(not((newe[self.start.x][self.start.y]==".") and ( newe[self.goal.x][self.goal.y]=="."))):
						temp+=1
			for i in range (len(newe)):
				for j in range (len(newe)):
					if(newe[i][j]=="#"):
						newe[i][j]="."
						myob.append(point(i,j))
					elif(type(newe[i][j])==int):
						myrew.append(Reward(i,j,int(newe[i][j])))
						newe[i][j]="."
			megagrid1=copy.deepcopy(newe)
		if(temp>0):
			print("CANNOT ROTATE GRID")
			time.sleep(4)
			return megagrid,player1.energy
		else:					
			self.myRewards=myrew
			self.myObstacles=myob
			player1.energy=energy1
			return newe,player1.energy

class Obstacle():
	'''class obstacle'''
	def __init__(self,n):
		x=random.randint(0,n-1)
		y=random.randint(0,n-1)
		self.x=x
		self.y=y
	def __eq__(self,other):
		return self.x==other.x and self.y==other.y
class Reward():
	'''reward class if x and y are not passed it ranomly generates them and the value '''
	def __init__(self,x,y,r=random.randint(1,9)):		
		self.x=x
		self.y=y
		self.value=r
	def __eq__(self,other):
		return self.x==other.x and self.y==other.y
class player():
	'''in addition to coordinates it has energy'''
	def __init__(self,x,y,energy):
		self.x=x
		self.y=y
		self.energy=energy
	def makeMove(self,s):
		'''it handles the case of right-left-up- and down'''
		'''along with them it also handles clockwise and anticlockwise'''
		global megagrid
		global grid1
		i=0
		while(i<len(s)-1):
			'''corresponding move is made one by one in every iteration replacing the current position by "X" and new 
			position is indicated by "O"'''
			if(s[i].lower()=="u"):
				no=0
				while(i+1<len(s) and s[i+1] in ["0","1","2","3","4","5","6","7","8","9"] ):
					no=no*10+int(s[i+1])
					i+=1
				for j in range(no):
					self.x-=1
					megagrid[self.x+1][self.y]="X"
					if(self.x<0):
						self.x=n-1					
					self.energy=grid1.showGrid()
					if(self.energy<=0):
						break
					if(self.x==grid1.goal.x and self.y==grid1.goal.y):
						break
						'''in between the move in case a player runs out of energy
						then this case is also handled
						In a case if player wins while making a move such a case is also handled'''											
			elif(s[i].lower()=="l"):
				no=0
				while(i+1<len(s) and s[i+1] in ["0","1","2","3","4","5","6","7","8","9"] ):
					no=no*10+int(s[i+1])
					i+=1
				for j in range(no):
					self.y-=1
					megagrid[self.x][self.y+1]="X"
					if(self.y<0):
						self.y=n-1					
					self.energy=grid1.showGrid()
					if(self.energy<=0):
						break
					if(self.x==grid1.goal.x and self.y==grid1.goal.y):
						break			
			elif(s[i].lower()=="r"):
				no=0
				while(i+1<len(s) and s[i+1] in ["0","1","2","3","4","5","6","7","8","9"] ):
					no=no*10+int(s[i+1])
					i+=1
				for j in range(no):
					self.y+=1
					megagrid[self.x][self.y-1]="X"					
					if(self.y>n-1):
						self.y=0
					self.energy=grid1.showGrid()
					if(self.energy<=0):
						break
					if(self.x==grid1.goal.x and self.y==grid1.goal.y):
						break
			elif(s[i].lower()=="d"):
				no=0
				while(i+1<len(s) and s[i+1] in ["0","1","2","3","4","5","6","7","8","9"] ):
					no=no*10+int(s[i+1])
					i+=1
				for j in range(no):
					self.x+=1
					megagrid[self.x-1][self.y]="X"
					if(self.x>n-1):
						self.x=0
					self.energy=grid1.showGrid()
					if(self.energy<=0):
						break
					if(self.x==grid1.goal.x and self.y==grid1.goal.y):
						break
			elif(s[i].upper()=="A"):
				'''the no loop handles the case of multidigit input'''
				no=0
				while(i+1<len(s) and s[i+1] in ["0","1","2","3","4","5","6","7","8","9"] ):
					no=no*10+int(s[i+1])
					i+=1
				megagrid,self.energy=grid1.rotateAnticlockwise(no)
				if(self.energy<=0):
						break
			elif(s[i].upper()=="C"):	
				no=0
				while(i+1<len(s) and s[i+1] in ["0","1","2","3","4","5","6","7","8","9"] ):
					no=no*10+int(s[i+1])
					i+=1
				megagrid,self.energy=grid1.rotateClockwise(no)
				if(self.energy<=0):
						break
			else:
				print("ENTER A VALID MOVE")	
				time.sleep(4)
			i+=1

class point():
		def __init__(self,x,y):
			self.x=x
			self.y=y
		def __eq__(self,other):
			return self.x==other.x and self.y==other.y
"""equality checker used in main function to check clashes"""
def generate(n):
			'''This is a random point generator function
			for choosing the starting and ending point we have four options of the boundary one such is chosen and starting and 
			goal point is indicated'''
			choice1=(0,random.randint(0,n-1))
			choice2=(random.randint(0,n-1),0)
			choice3=(n-1,random.randint(0,n-1))
			choice4=(random.randint(0,n-1),n-1)
			starting=random.choice([choice1,choice2,choice3,choice4])
			pointposition=point(starting[0],starting[1])
			return pointposition
'''main part of the body'''
n=int(input())	
'''taking the input from the user'''		
clean()
megagrid=[]
for i in range(n):
	col=[]
	for j in range(n):
		col.append(".")
	megagrid.append(col)
'''megagrid is initialised to a gid of all ". " so that it can be overwritten by the showGrid() method'''
startpoint=generate(n)
endpoint=generate(n)
while(startpoint==endpoint):
	endpoint=generate(n)
'''Generation of the startpoint and the endpoint if startpoint becomes qual to the endpoint it is generated again '''
no_obstacle=random.randint(n//2,n)
no_reward=random.randint(n//2,n)
'''choosing gof the no of obstacles and rewards it is between n//2 and n'''
obstaclelist=[]
rewardlist=[]
'''empty lists which will be passed to grid defination'''
for i in range(no_obstacle):
	o=Obstacle(n)
	while((o.x==startpoint.x and o.y==startpoint.y) or (o.x==endpoint.x and o.y==endpoint.y)):
		o=Obstacle(n)
	obstaclelist.append(o)
'''obstacle list is created in a case object coincides with staart or end point it is generated again '''
for i in range(no_reward):
	r=Reward(x=random.randint(0,n-1),y=random.randint(0,n-1))
	while((r.x==startpoint.x and r.y==startpoint.y) or (r.x==endpoint.x and r.y==endpoint.y)):
		r=Reward(x=random.randint(0,n-1),y=random.randint(0,n-1))
	rewardlist.append(r)
'''Reward list is created in a case object coincides with staart or end point it is generated again '''
for i in range(len(rewardlist)):
	for j in obstaclelist:
		if(rewardlist[i]==j):
			rewardlist[i]=Reward(x=random.randint(0,n-1),y=random.randint(0,n-1))
			while((r.x==startpoint.x and r.y==startpoint.y) or (r.x==endpoint.x and r.y==endpoint.y)):
				r=Reward(x=random.randint(0,n-1),y=random.randint(0,n-1))
"""explicit checking occurs to check if any obsatcle object collides with reward oblect as it will interfere i  future
in such a case reward is generated again"""

#object player 1 is a global object used throuout to keep track of players coordinates and energy
player1=player(startpoint.x,startpoint.y,2*n)

#--INITIALISATION
print("ENERGY: ",player1.energy)
grid1=grid(n,startpoint,endpoint,obstaclelist,rewardlist)
#----------

flag=0
#this loop is responsible for taking inputs until energy exhausts or goal is reached
while(not(player1.x==grid1.goal.x and player1.y==grid1.goal.y) and player1.energy>0):
	s=input()
	player1.makeMove(s)
	clean()
	# initilisation after every move to clear the trail

	print("ENERGY: ",player1.energy)
	grid1=grid(n,point(player1.x,player1.y),grid1.goal,grid1.myObstacles,grid1.myRewards)
	#---
	time.sleep(0.5)
	if player1.x==grid1.goal.x and player1.y==grid1.goal.y and player1.energy>=0:
		print("YAAAY! YOU WIN!! ;)")
		flag=1
		break
if(flag==0):
		print("OOPS! YOU LOOSE!! :(")
