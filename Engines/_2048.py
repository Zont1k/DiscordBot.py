# 2048 engine (made by ilesik)
import random

class Field():
	def __init__(self,field_size = 4):
		self.size = field_size
		self.map= [[None for i in range(field_size)] for i in range(field_size)]
		self.map[random.randint(0,len(self.map)-1)][random.randint(0,len(self.map[0])-1)] =  (2 if random.randint(0,100) < 90 else 4)
		self.need = 2 ** ((field_size+1)*2+1)
		
	def get_map(self):
		return self.map
	
	def move(self,way = ''):#left,right,up,down
		check = True
		
		if way == "up":			
			while check:
				check = False
				for row_n in range(1,len(self.map)):
					for i in range(len(self.map[row_n])):
						if self.map[row_n][i] and self.map[row_n-1][i] and self.map[row_n][i] == self.map[row_n-1][i] :
							self.map[row_n-1][i] *= 2
							self.map[row_n][i] = None
							check = True
							continue
							
						elif self.map[row_n][i] and not self.map[row_n-1][i]:
							self.map[row_n-1][i],self.map[row_n][i] = self.map[row_n][i],self.map[row_n-1][i]
							check = True
							continue
							
		if way == "down":
			while check:
				check = False
				for row_n in range(len(self.map)-2,-1,-1):
					for i in range(len(self.map[row_n])):
						if self.map[row_n][i] and self.map[row_n+1][i] and self.map[row_n][i] == self.map[row_n+1][i] :
							self.map[row_n+1][i] *= 2
							self.map[row_n][i] = None
							check = True
							continue
							
						elif self.map[row_n][i] and not self.map[row_n+1][i]:
							self.map[row_n+1][i],self.map[row_n][i] = self.map[row_n][i],self.map[row_n+1][i]
							check = True
							continue
							
							
		if way == "left":			
			while check:
				check = False
				for row_n in range(len(self.map)):
					for i in range(1,len(self.map[row_n])):
						if self.map[row_n][i] and self.map[row_n][i-1] and self.map[row_n][i] == self.map[row_n][i-1] :
							self.map[row_n][i-1] *= 2
							self.map[row_n][i] = None
							check = True
							continue
							
						elif self.map[row_n][i] and not self.map[row_n][i-1]:
							self.map[row_n][i-1],self.map[row_n][i] = self.map[row_n][i],self.map[row_n][i-1]
							check = True
							continue
							
		if way == "right":
			while check:
				check = False
				for row_n in range(len(self.map)):
					for i in range(len(self.map[row_n])-2,-1,-1):
						if self.map[row_n][i] and self.map[row_n][i+1] and self.map[row_n][i] == self.map[row_n][i+1] :
							self.map[row_n][i+1] *= 2
							self.map[row_n][i] = None
							check = True
							continue
							
						elif self.map[row_n][i] and not self.map[row_n][i+1]:
							self.map[row_n][i+1],self.map[row_n][i] = self.map[row_n][i],self.map[row_n][i+1]
							check = True
							continue
		#check for win/lose
		free_places = []
		not_free = []
		for i in range(len(self.map)) :
			for b in range(len(self.map[i])) :
				if not self.map[i][b]:
					free_places.append([i,b])
				else:
					not_free.append(self.map[i][b])
		if max(not_free) >= self.need:
			return "win"
		if len(free_places) == 0:
			return "lose"
		pos = random.choice(free_places)
		self.map[pos[0]][pos[1]] = (2 if random.randint(0,100) < 90 else 4)
			
		
		
		
	

if __name__ == '__main__':
	a =Field(4)
	while True:
		print(a.get_map())
		print(a.move(input('way: ')))
	