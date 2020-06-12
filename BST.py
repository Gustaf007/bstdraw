from Queue import Queue

class BST:
	class Node:
		def __init__(self, key, value):
			self.key = key
			self.value = value
			self.left = None
			self.right = None
	
	def __init__(self):
		self.root = None
		
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
		return x
		
	def get(self, key):
		x = self.root
		while x != None:
			if   key < x.key: x = x.left
			elif x.key < key: x = x.right
			else: return x.value
		return None


	def keys(self):
		q = Queue()
		self.__inorder(self.root, q)
		return q

	def __inorder(self, x, q):
		if x == None: return
		self.__inorder(x.left, q)
		q.enqueue(x.key)
		self.__inorder(x.right, q)
				
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
		
		
	def deleteMin(self):
		self.root = self.__deleteMin(self.root)

	def __deleteMin(self, x):
		if x.left == None: return x.right
		x.left = self.__deleteMin(x.left)
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
		return x		
