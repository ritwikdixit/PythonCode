class Heap:
	def __init__(self):
		self.arr=[]

	def leftChild(self, index):
		if 2*index+1>=len(self.arr):
			return None
		return self.arr[2*index+1]

	def rightChild(self, index):
		if 2*index+2>=len(self.arr):
			return None
		return self.arr[2*index+2]

	def swap(self, i1, i2):
		temp = self.arr[i1]
		self.arr[i1]=self.arr[i2]
		self.arr[i2]=temp

	def getMin(self):
		if self.arr:
			return self.arr[0]

	def add(self, value):
		self.arr.append(value)
		ind=len(self.arr)-1
		while ind>0 and self.arr[ind] < self.arr[(ind-1)//2]:
			self.swap(ind, (ind-1)//2 )
			ind=(ind-1)//2

	def removeMin(self):
		if not self.arr:
			return None
		minval=self.arr[0]
		self.arr[0]=self.arr[len(self.arr)-1]
		self.arr.pop()
		#swim
		ind=0
		while self.leftChild(ind):
			if self.arr[ind] < self.leftChild(ind) and \
				(not self.rightChild(ind) or self.arr[ind] < self.rightChild(ind)):
				break
			if self.rightChild(ind) and self.leftChild(ind) > self.rightChild(ind):
				self.swap(ind,2*ind+2)
				ind=2*ind+2
			else:
				self.swap(ind,2*ind+1)
				ind=2*ind+1

		return minval

heap = Heap()
heap.add(4)
heap.add(6)
heap.add(2)
heap.add(1)
heap.add(14)
heap.add(10)
heap.add(3)
heap.add(8)
l=[]
while heap.getMin():
	l.append(heap.removeMin())
print(l)
