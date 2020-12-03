
# defining the Node class
class Node:
	def __init__ (self, child = None, parent = None, sibling = None, identifier = None, cargo = None):
		self.__child = child;
		self.__parent = parent;
		self.__sibling = sibling;
		self.__identifier = identifier;
		self.__cargo = cargo;
	def setChild (self, child = None):
		self.__child = child;
	def setParent (self, parent = None):
		self.__parent = parent;
	def setSibling (self, sibling = None):
		self.__sibling = sibling
	def setCargo (self, cargo = None):
		self.__cargo = cargo;
	def setId (self, identifier = None):
		self.__identifier = identifier
	def getChild (self):
		return self.__child;
	def getParent (self):
		return self.__parent;
	def getSibling (self):
		return self.__sibling;
	def getId (self):
		return self.__identifier;
	def getCargo (self):
		return self.__cargo;
	def getDetails (self):
		return {
			'child':self.__child,
			'parent':self.__parent,
			'current':self,
			'sibling':self.__sibling,
			'identifier':self.__identifier,
			'cargo':self.__cargo,
		}
	def __del__ (self):
		pass;

# defining the Tree class
class Tree:
	def __init__ (self):
		self.__rootnode = None;
		self.__identifier = 0;
	def insertChild (self, root = None, cargo = None):
		node = Node (None, root, None, self.__identifier, cargo)
		if not root:
			root = node
		else:
			firstChild = root.getChild ()
			if not firstChild:
				root.setChild (node)
			else:
				while firstChild.getSibling ():
					firstChild = firstChild.getSibling ()
				firstChild.setSibling (node)
		self.__identifier = self.__identifier + 1;
		return root;
	def insertSibling (self, root = None, cargo = None):
		node = Node (None, root, None, self.__identifier, cargo)
		if not root:
			return None
		else:
			firstChild = root;
			while firstChild.getSibling ():
				firstChild = firstChild.getSibling ();
			firstChild.setSibling (node)
		self.__identifier = self.__identifier + 1
		return root;
	def displayChild (self, root = None):
		if not root or not root.getChild ():
			return None
		firstChild = root.getChild ()
		while firstChild:
			print (firstChild.getDetails ())
			firstChild = firstChild.getSibling ()
		return root;
	def displaySibling (self, root = None):
		if not root:
			return None
		firstChild = root;
		while firstChild:
			print (firstChild.getDetails ())
			firstChild = firstChild.getSibling ()
		return root;
	def displayTree (self, root = None):
		if not root:
			return None
		else:
			print (root.getDetails ())
			firstChild = root.getChild ()
			while firstChild:
				self.displayTree (firstChild)
				firstChild = firstChild.getSibling ()
		return root;
	def findNode (self, root = None, identifier = 0):
		if not root:
			return None;
		elif identifier == 0:
			return self.__rootnode
		else:
			firstChild = root.getChild ()
			while firstChild:
				if firstChild.getId () == identifier:
					return firstChild
				firstChild = self.findNode (firstChild, identifier)
				if firstChild and firstChild.getId () == identifier:
					return firstChild
				if firstChild:
					firstChild = firstChild.getSibling ()
		return root;
	def setRoot (self, root = None):
		self.__rootnode = root;
		return self.__rootnode;
	def getRoot (self):
		return self.__rootnode;
	def __del__ (self):
		pass;

def main ():
	tree = Tree ()
	tree.setRoot (tree.insertChild (tree.getRoot (), 123));
	tree.setRoot (tree.insertChild (tree.getRoot (), 4223));
	tree.setRoot (tree.insertChild (tree.getRoot (), 345));
	tree.setRoot (tree.insertChild (tree.getRoot (), 213));

	# finding the node with an id of 3
	node = tree.findNode (tree.getRoot (), 2);
	node = tree.insertChild (node, 890);
	node = tree.insertChild (node, 908);
	node = tree.insertSibling (node, 789);

	# finding the node with an id of 5
	node = tree.findNode (tree.getRoot (), 5);
	node = tree.insertChild (node, 908);
	node = tree.insertChild (node, 809);
	node = tree.insertSibling (node, 777);

	# finding the node with an id of 7
	node = tree.findNode (tree.getRoot (), 7);
	node = tree.insertChild (node, 987);

	# displaying the tree
	tree.setRoot (tree.displayTree (tree.getRoot ()))
if __name__ == '__main__':
	main ()