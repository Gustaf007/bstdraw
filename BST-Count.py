from Queue import Queue

class BST:
	class Node:
		def __init__(self, key, value):
			self.key = key
			self.value = value
			self.left = None
			self.right = None
			self.count = 1
	
	def __init__(self):
		self.root = None
		
	def size(self):
		return self.__size(self.root)

	def __size(self, x):
		if x == None: return 0
		return x.count
		
	def put(self, key, value):
		self.root = self.__put(self.root, key, value)
		
	def __put(self, x, key, value):
		if x == None: return BST.Node(key, value)		
		if key < x.key:
			x.left = self.__put(x.left, key, value)
		elif x.key < key:
			x.right = self.__put(x.right, key, value)
		else:
			x.value = value
		x.count = 1 + self.__size(x.left) + self.__size(x.right)
		return x
		
	def get(self, key):
		x = self.root
		while x != None:
			if   key < x.key: x = x.left
			elif x.key < key: x = x.right
			else: return x.value
		return None
		
	def floor(self, key):
		x = self.__floor(self.root, key)
		if x == None: return None
		return x.key

	def __floor(self, x, key):
		if x == None: return None
		if key == x.key:
			return x
		if key < x.key:
			return self.__floor(x.left, key)

		t = self.__floor(x.right, key)
		if t == None: return x
		return t
		
	def rank(self, key):
		return self.__rank(key, self.root)
		
	def __rank(self, key, x):
		if x == None: return 0
		if   key < x.key: 
			return self.__rank(key, x.left)
		elif x.key < key: 
			return 1 + self.__size(x.left) + self.__rank(key, x.right)
		else: 
			return self.__size(x.left)
		
	def keys(self):
		q = Queue()
		self.__inorder(self.root, q)
		return q

	def __inorder(self, x, q):
		if x == None: return
		self.__inorder(x.left, q)
		q.enqueue(x.key)
		self.__inorder(x.right, q)
		
	def deleteMin(self):
		self.root = self.__deleteMin(self.root)

	def __deleteMin(self, x):
		if x.left == None: return x.right
		x.left = self.__deleteMin(x.left)
		x.count = 1 + self.__size(x.left) + self.__size(x.right)
		return x		

	def min(self):
		if self.root == None: return None
		return self.__min(self.root)
		
	def __min(self, x):
		if x.left == None:
			 return x
		else:
			return self.__min(x.left)

	def delete(self, key):
		self.root = self.__delete(self.root, key)
	
	def __delete(self, x, key):
		if x == None: return None
		if key < x.key: x.left = self.__delete(x.left,  key)
		elif x.key < key: x.right = self.__delete(x.right, key)
		else:
			if x.right == None: return x.left
			if x.left  == None: return x.right
			t = x
			x = self.__min(t.right)
			x.right = self.__deleteMin(t.right)
			x.left = t.left
		x.count = 1 + self.__size(x.left) + self.__size(x.right)
		return x
		
if __name__ == "__main__":		
	bst = BST()
	bst.put("AIS",1)
	bst.put("DSA",2)
	bst.put("Vis",3)

	print(bst.floor("GPT"))
	print(bst.size())
	print(bst.rank("DSA"))

	for e in bst.keys():
		print(e)

	bst.delete("Vis")

	for e in bst.keys():
		print(e)

	print(bst.size())