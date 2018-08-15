from collections import deque

class Node:
	def __init__(self):
		self.endofWord=False
		self.links={}

class Trie:
	def __init__(self):
		self.root=Node()

	#insert a string
	def insert(self, s):
		node = self.root
		for char in s:
			if char not in node.links:
				node.links[char]=Node()
			node=node.links[char]
		node.endofWord=True

	def contains(self, s):
		node = self.root
		for char in s:
			if char not in node.links:
				return False
			node=node.links[char]
		return node.endofWord

	def printWords(self):
		def recurse(node, progress):
			if not node.links:
				print(progress)
			for charkey in node.links:
				recurse(node.links[charkey], progress+charkey)
		recurse(self.root, '')


#Tests
trie = Trie()
trie.insert('alpha')
trie.insert('alphapotomus')
trie.insert('colloquial')
trie.insert('bamf')

print(trie.contains('bamf'))
print(trie.contains('alph'))
print(trie.contains('sdi'))

trie.printWords()
