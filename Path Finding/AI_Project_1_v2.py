#################################
#  AI Search Algorithm project  #
# 								#
#  Created By Aaron Waruszewski #
#								#
#################################                             

import time
#import sys ******************** DELETE ME! ***********************

# This Heap class is using a Minimum Heap structure, constructed in an array/list.
class Heap:
	"""docstring for Heap"""

	# The constructor for the Heap class.
	def __init__(self, board = None): 
		self.boards = []				# Setup board with an empty list/array.

		if board is not None: 			# Adds a board if there's one to add.
			self.boards.append(board)

	# Adds a new node/board to the the bottom of the Heap tree, then moves it up to the proper position.
	def insert(self, newBoard):
		self.boards.append(newBoard) 							# Insert a new board to the bottom of the heap tree.
		num = len(self.boards) - 1
		#while self.boards[num].estimatedCost < self.boards[int((num-1)*0.5)].estimatedCost:  # Checks to see which has a smaller cost.
		#	temp = self.boards[int((num-1)*0.5)]               	# Save the parent
		#	self.boards[int((num-1)*0.5)] = self.boards[num]   	# Move the child to the parents spot
		#	self.boards[num] = temp 					     	# Move the old parent to be the new child
		#	num = int((num-1)*0.5)							 	# Chnges num to continue the search
		self.sortNewBoard(num)											# Since the code for sorting decreasekey and insert are the same, send it the new nodes location for sorting.


	# Returns the root node, which is also the holder the lowest value, and deletes it from the Heap.
	def deleteMin(self):
		returnBoard = self.boards[0]			# Takes the root node/top of the heap tree, and saves it to return it.

		if len(self.boards) > 1:
			self.boards[0] = self.boards.pop() 	# What was this for? To make the bottom leaf the new root.
			num = 0

			while ((2*num)+1) < len(self.boards):		# Checks to see if ((2*num)+1) isn't longer than the list/array so not to go outside of the list/array.
				if ((2*num)+2) < len(self.boards):		# If this isn't longer too, start comparing each leaf.
					if self.boards[num].estimatedCost > self.boards[(2*num)+1].estimatedCost or self.boards[num].estimatedCost > self.boards[(2*num)+2].estimatedCost:	# Check to see if the added board needs to be moved at all.
						if self.boards[(2*num)+1].estimatedCost > self.boards[(2*num)+2].estimatedCost: #Check which is bigger
							temp = self.boards[int((2*num)+2)]					# Saves Child node
							self.boards[int((2*num)+2)] = self.boards[num]		# Drops parent node to child node
							self.boards[num] = temp 							# Puts old child node in new parent spot
							num = int((2*num)+2)								# Chnges num to continue the search
						else:
							temp = self.boards[int((2*num)+1)]					# Saves Child node
							self.boards[int((2*num)+1)] = self.boards[num]		# Drops parent node to child node
							self.boards[num] = temp 							# Puts old child node in new parent spot
							num = int((2*num)+1)								# Chnges num to continue the search
					else:
						break													# Breaks out if the added node is no longer smaller than the parents.
				elif self.boards[num].estimatedCost > self.boards[(2*num)+1].estimatedCost: # The tree has only has one leaf left, check it then break.
					temp = self.boards[int((2*num)+1)]					# Saves Child node
					self.boards[int((2*num)+1)] = self.boards[num]		# Drops parent node to child node
					self.boards[num] = temp 							# Puts old child node in new parent spot
					break 												# Breaks out now that it's finished.
				else:													# The heap is good, so we leave the heap alone.
					break

		else:															# There is only one node left, so pop it off and trash it.
			trash = self.boards.pop()									# Removes the lone node (the root node).

		return returnBoard												# Returns the saved root node for further processing.


	# For a Four branch tree. ************ Needs to be finished. *****************
	def deleteMin2(self): 
		returnBoard = self.boards[0]			# Takes the root node/top of the heap tree, and saves it to return it.

		if len(self.boards) > 1:
			self.boards[0] = self.boards.pop() 	# What was this for? To make the bottom leaf the new root.
			num = 0

			while ((4*num)+1) < len(self.boards):		# Checks to see if ((2*num)+1) isn't longer than the list/array so not to go outside of the list/array.
				if ((4*num)+4) < len(self.boards):		# If this isn't longer too, start comparing each leaf.
					if self.boards[num].estimatedCost > self.boards[(4*num)+1].estimatedCost or self.boards[num].estimatedCost > self.boards[(4*num)+2].estimatedCost or self.boards[num].estimatedCost > self.boards[(4*num)+3].estimatedCost or self.boards[num].estimatedCost > self.boards[(4*num)+4].estimatedCost:	# Check to see if the added board needs to be moved at all.
						if self.boards[(4*num)+3].estimatedCost > self.boards[(4*num)+4].estimatedCost and self.boards[(4*num)+2].estimatedCost > self.boards[(4*num)+4].estimatedCost and self.boards[(4*num)+1].estimatedCost > self.boards[(4*num)+4].estimatedCost: #Check which is bigger
							temp = self.boards[int((4*num)+4)]					# Saves Child node
							self.boards[int((4*num)+4)] = self.boards[num]		# Drops parent node to child node
							self.boards[num] = temp 							# Puts old child node in new parent spot
							num = int((4*num)+4)								# Chnges num to continue the search
						elif self.boards[(4*num)+2].estimatedCost > self.boards[(4*num)+3].estimatedCost and self.boards[(4*num)+1].estimatedCost > self.boards[(4*num)+3].estimatedCost: #Check which is bigger
							temp = self.boards[int((4*num)+3)]					# Saves Child node
							self.boards[int((4*num)+3)] = self.boards[num]		# Drops parent node to child node
							self.boards[num] = temp 							# Puts old child node in new parent spot
							num = int((4*num)+3)								# Chnges num to continue the search
						elif self.boards[(4*num)+1].estimatedCost > self.boards[(4*num)+2].estimatedCost: #Check which is bigger
							temp = self.boards[int((4*num)+2)]					# Saves Child node
							self.boards[int((4*num)+2)] = self.boards[num]		# Drops parent node to child node
							self.boards[num] = temp 							# Puts old child node in new parent spot
							num = int((4*num)+2)								# Chnges num to continue the search
						else:
							temp = self.boards[int((4*num)+1)]					# Saves Child node
							self.boards[int((4*num)+1)] = self.boards[num]		# Drops parent node to child node
							self.boards[num] = temp 							# Puts old child node in new parent spot
							num = int((4*num)+1)								# Chnges num to continue the search
					else:
						break													# Breaks out if the added node is no longer smaller than the parents.
				elif ((4*num)+3) < len(self.boards):
					if self.boards[num].estimatedCost > self.boards[(4*num)+1].estimatedCost or self.boards[num].estimatedCost > self.boards[(4*num)+2].estimatedCost or self.boards[num].estimatedCost > self.boards[(4*num)+3].estimatedCost:	# Check to see if the added board needs to be moved at all.
						if self.boards[(4*num)+2].estimatedCost > self.boards[(4*num)+3].estimatedCost and self.boards[(4*num)+1].estimatedCost > self.boards[(4*num)+3].estimatedCost: #Check which is bigger
							temp = self.boards[int((4*num)+3)]					# Saves Child node
							self.boards[int((4*num)+3)] = self.boards[num]		# Drops parent node to child node
							self.boards[num] = temp 							# Puts old child node in new parent spot
							num = int((4*num)+3)								# Chnges num to continue the search
						elif self.boards[(4*num)+1].estimatedCost > self.boards[(4*num)+2].estimatedCost: #Check which is bigger
							temp = self.boards[int((4*num)+2)]					# Saves Child node
							self.boards[int((4*num)+2)] = self.boards[num]		# Drops parent node to child node
							self.boards[num] = temp 							# Puts old child node in new parent spot
							num = int((4*num)+2)								# Chnges num to continue the search
						else:
							temp = self.boards[int((4*num)+1)]					# Saves Child node
							self.boards[int((4*num)+1)] = self.boards[num]		# Drops parent node to child node
							self.boards[num] = temp 							# Puts old child node in new parent spot
							num = int((4*num)+1)								# Chnges num to continue the search
					else:
						break													# Breaks out if the added node is no longer smaller than the parents.
				elif ((4*num)+2) < len(self.boards):
					if self.boards[num].estimatedCost > self.boards[(4*num)+1].estimatedCost or self.boards[num].estimatedCost > self.boards[(4*num)+2].estimatedCost:	# Check to see if the added board needs to be moved at all.
						if self.boards[(4*num)+1].estimatedCost > self.boards[(4*num)+2].estimatedCost: #Check which is bigger
							temp = self.boards[int((4*num)+2)]					# Saves Child node
							self.boards[int((4*num)+2)] = self.boards[num]		# Drops parent node to child node
							self.boards[num] = temp 							# Puts old child node in new parent spot
							num = int((4*num)+2)								# Chnges num to continue the search
						else:
							temp = self.boards[int((4*num)+1)]					# Saves Child node
							self.boards[int((4*num)+1)] = self.boards[num]		# Drops parent node to child node
							self.boards[num] = temp 							# Puts old child node in new parent spot
							num = int((4*num)+1)								# Chnges num to continue the search
					else:
						break
				elif self.boards[num].estimatedCost > self.boards[(4*num)+1].estimatedCost: # The tree has only has one leaf left, check it then break.
					temp = self.boards[int((4*num)+1)]					# Saves Child node
					self.boards[int((4*num)+1)] = self.boards[num]		# Drops parent node to child node
					self.boards[num] = temp 							# Puts old child node in new parent spot
					break 												# Breaks out now that it's finished.
				else:													# The heap is good, so we leave the heap alone.
					break

		else:															# There is only one node left, so pop it off and trash it.
			trash = self.boards.pop()									# Removes the lone node (the root node).

		return returnBoard												# Returns the saved root node for further processing.


	# Decreases the value of one similar nodes by replacing it with another similar node that has a lower value.
	def decreaseKey(self, otherBoard): 
		# Search the list/array and replace a similar one if its f(n) value is smaller
		count = 0
		for keyFinder in self.boards:							# Rotates through the boards.
			if otherBoard.__hash__() == keyFinder.__hash__():	# Is this faster than the compare method? Checks to see if the boards are the same.
				if otherBoard.estimatedCost < keyFinder.estimatedCost:	# Checks to see if the new board is has a lower cost to get to.
					self.boards[count] = otherBoard						# If it has reached this point, switch the higher cost board with the lower cost one. (Checked this works on simple tests)
					break 												# New add-on! Break out of search since we found the board and have replaced it.
				else:													# Since matching boards have been found but the new cost isn't lower, stop looking.
					break
			count = count + 1

		self.sortNewBoard(count)											# Since the code for sorting decreasekey and insert are the same, send it the new nodes location for sorting.

	# This method sorts the new or altered boards into the proper place in the heap tree.
	def sortNewBoard(self, num):
		while self.boards[num].estimatedCost < self.boards[int((num-1)/2)].estimatedCost:  # Checks to see which has a smaller cost, and if smaller continue working through the tree.
			temp = self.boards[int((num-1)/2)]               	# Save the parent
			self.boards[int((num-1)/2)] = self.boards[num]   	# Move the child to the parents spot
			self.boards[num] = temp 					     	# Move the old parent to be the new child
			num = int((num-1)/2)							 	# Chnges num to continue the search

	# This method sorts the new or altered boards into the proper place in a 4 branch heap tree.
	def sortNewBoard2(self, num):
		while self.boards[num].estimatedCost < self.boards[int((num-1)/4)].estimatedCost:  # Checks to see which has a smaller cost, and if smaller continue working through the tree.
			temp = self.boards[int((num-1)/4)]               	# Save the parent
			self.boards[int((num-1)/4)] = self.boards[num]   	# Move the child to the parents spot
			self.boards[num] = temp 					     	# Move the old parent to be the new child
			num = int((num-1)/4)							 	# Chnges num to continue the search

	# Checks to see if the Heap is empty, and returns the answer.
	def isEmpty(self):
		return self.boards == []	# Returns true if the heap is empty.


# A Queue. It has a first in first out structure.
class Queue:
	"""docstring for Queue"""

	# Constructor for the Queue class.
	def __init__(self, board):
		self.boards = []

		if board is not None: # Adds a board if there's one to add.
			self.boards.append(board)

	# Adds a new node/board to the back of the Queue.
	def enqueue(self, board):
		self.boards.insert(0,board)

	# Returns a node/board and deletes it from the front of the Queue.
	def dequeue(self):
		return self.boards.pop()

	# Checks to see if the Queue is empty, and returns the answer.
	def isEmpty(self):
		return self.boards == []


# A Stack. It has a first in last out structure.
class Stack(object):
	"""docstring for Stack"""

	# The constructor for the Stack class.
	def __init__(self, board):
		self.boards = []

		if board is not None: # Adds a board if there's one to add.
			self.boards.append(board)
		
	# Adds a node/board to the top of the Stack.
	def push(self, board):
		self.boards.append(board)

	# Removes and returns a node/board from the top of the Stack.
	def pop(self):
		return self.boards.pop()

	#Checks to see if the Stack is empty, and returns the answer.
	def isEmpty(self):
		return self.boards == []

# The Board_nxn class takes a list/array of consecutive numbers that are long enough to create a N x N list. 
class GameBoard(object):
	"""docstring for Board_nXn"""

	# Global class variables
	boardSize = 0			# This holds size of the n x n board.
	nodeCount = 0			# This holds the amount of total nodes created.
	branchLimit = 0			# This holds the maximum length the nodes can grow.
	startTime = 0 			# This holds the start time when this search has started.


	# This is the constructor for the GameBoard class.
	def __init__(self, initialBoard = None):
		super(GameBoard, self).__init__() # Is this needed? *******************************

		if GameBoard.startTime is 0:
			GameBoard.startTime = time.clock()

		# Set up the class global class variables.
		if initialBoard is not None and GameBoard.boardSize is 0:	# This will initialize the boardSize variable with the
			GameBoard.boardSize = int(len(initialBoard) ** 0.5)		# square root of the length of the initialBoard.

		# Sets up the maximum branch limit that can be moved through.
		if GameBoard.branchLimit is 0:
			GameBoard.branchLimit = ((( GameBoard.boardSize - 1 ) * 2) * (GameBoard.boardSize * GameBoard.boardSize))  # 500
			# x*2 where x is the length of one side -1, then multiplied by 2 to get the amount of moves for one piece 
			# to across the board. Then by multiplying that by the amount of pieces on the board we get the depth of 
			# the tree that has at least one solveable set of moves it can take to solve the board. 

		GameBoard.nodeCount = GameBoard.nodeCount + 1 # Counts the amount of nodes that have been created in total.

		# GameBoard variables
		self.board = [[0 for x in xrange(0, GameBoard.boardSize)]for y in xrange(0, GameBoard.boardSize)] #Creates a 2D list/array.
		self.blankSpaceX = 0   # This holds the x coordinate to the zero/blank space of the GameBoard.
		self.blankSpaceY = 0   # This holds the y coordinate to the zero/blank space of the GameBoard.
		self.branchLength = 0  # This holds the branch length of this node. Though I could use len(self.moves) as well.
		self.moves = []        # This holds the set of moves that got this node to where it is now.

		# Fill the 2D list/array with usable data.
		if initialBoard is not None:						# Checks to see if there is anything in initialBoard.
			count = 0										# Creates and sets count to 0.
			for y in xrange(0, GameBoard.boardSize):		# This for loop runs through the y coordinates.
				for x in xrange(0, GameBoard.boardSize):	# This for loop runs through the x coordinates.
					self.board[x][y] = initialBoard[count]	# Adds the data from initialBoard to the 2D list/array.
					if initialBoard[count] == 0:			# Checks to see if the current input from initialBoard is 0.
						self.blankSpaceX = x 				# Saves the the x coordinate of the zero/blank space.
						self.blankSpaceY = y 				# Saves the the y coordinate of the zero/blank space.
					count = count + 1						# Adds 1 to count to iterate through initialBoard.
			self.board = self.convert2DListTo2DTuple(self.board)


	def convert2DListTo2DTuple(self, tempList): # Transforms the list into a tuple for hashing later.
		temp = []								# Creates a temporary list

		for t in tempList:						# Goes through the main list to acquire the other lists.
			temp.append(tuple(t))				# Transforms the other lists into a tuple and saves them to the temp one.

		return tuple(temp)						# Converts the main list into a tuple, as the last step and returns an entire 2D tuple.


	def compare(self, otherBoard):
		return self.__hash__() == otherBoard.__hash__()	# Checks if both boards are the same by comparing their hash.


	def success(self):
		endTime = time.clock()
		

		print 'path_to_goal: ', self.moves
		print 'cost_of_path: ', self.branchLength #len(self.moves)
		print 'nodes_expanded: ', GameBoard.nodeCount
		print 'fringe_size:'
		print 'max_fringe_size: '
		print 'search_depth:'
		print 'max_search_depth: '
		print 'running_time:', endTime - GameBoard.startTime
		print 'max_ram_usage:'

		# For mass Testing ********************** DELETE ME! *************************
		GameBoard.startTime = 0

	def failure(self):
		endTime = time.clock()
		

		print 'Failed to find answer...'
		print 'path_to_goal: ', self.moves
		print 'cost_of_path: ', len(self.moves)
		print 'nodes_expanded: ', GameBoard.nodeCount
		print 'fringe_size:'
		print 'max_fringe_size: '
		print 'search_depth:'
		print 'max_search_depth: '
		print 'running_time:', endTime - GameBoard.startTime
		print 'max_ram_usage:'

		# For mass Testing ********************** DELETE ME! *************************
		GameBoard.startTime = 0
	
	def __eq__(self, otherBoard):
		return self.compare(otherBoard)

	def __ne__(self, otherBoard):
		return not self.compare(otherBoard)
        

	def __hash__(self):
		return hash(self.board)

	def __cmp__(self, otherBoard):			# A comparison method.
		return self.compare(otherBoard) 

	def forTesting(self):
		GameBoard.nodeCount = 2
		

class GameBoard_for_BFS(GameBoard):
	"""docstring for GameBoard_for_BFS"""

	def __init__(self, initialBoard = None):
		super(GameBoard_for_BFS, self).__init__(initialBoard)	# Why doesn't this work?
		#GameBoard.__init__(self, initialBoard)

	# Makes and returns a copy of itself.
	def copy(self):
		tempBoard = GameBoard_for_BFS()

		for y in xrange(0, GameBoard.boardSize):
			for x in xrange(0, GameBoard.boardSize):
				tempBoard.board[x][y] = self.board[x][y]
				if self.board[x][y] == 0:
					tempBoard.blankSpaceX = x
					tempBoard.blankSpaceY = y
		for c in xrange(0, len(self.moves)):
			tempBoard.moves.append(self.moves[c])		# Is this the python way of doing it? What about tempBoard.moves = self.moves[:]
		#tempBoard.moves = self.moves[:]
		tempBoard.branchLength = self.branchLength + 1

		return tempBoard

	# Creates more boards based on the neighbors where the blank space is located.
	def neighbors(self):
		tempList = []

		#Add if statement here to control branch Length
		if self.branchLength < self.branchLimit:
			if self.blankSpaceY > 0:
				tempCopy = self.copy()

				tempCopy.moves.append('Up')

				tempCopy.board[self.blankSpaceX][self.blankSpaceY] = self.board[self.blankSpaceX][self.blankSpaceY - 1]
				tempCopy.board[self.blankSpaceX][self.blankSpaceY - 1] = 0

				tempCopy.blankSpaceY = tempCopy.blankSpaceY - 1

				tempCopy.board = tempCopy.convert2DListTo2DTuple(tempCopy.board) # This changes the 2d list/array the board uses into a tuple for hash comparing later.

				tempList.append(tempCopy)

			if self.blankSpaceY < (self.boardSize-1):
				tempCopy = self.copy()

				tempCopy.moves.append('Down')

				tempCopy.board[self.blankSpaceX][self.blankSpaceY] = self.board[self.blankSpaceX][self.blankSpaceY + 1]
				tempCopy.board[self.blankSpaceX][self.blankSpaceY + 1] = 0
            
				tempCopy.blankSpaceY = tempCopy.blankSpaceY + 1

				tempCopy.board = tempCopy.convert2DListTo2DTuple(tempCopy.board) # This changes the 2d list/array the board uses into a tuple for hash comparing later.

				tempList.append(tempCopy)

			if self.blankSpaceX > 0:
				tempCopy = self.copy()

				tempCopy.moves.append('Left')

				tempCopy.board[self.blankSpaceX][self.blankSpaceY] = self.board[self.blankSpaceX - 1][self.blankSpaceY]
				tempCopy.board[self.blankSpaceX - 1][self.blankSpaceY] = 0

				tempCopy.blankSpaceX = tempCopy.blankSpaceX - 1

				tempCopy.board = tempCopy.convert2DListTo2DTuple(tempCopy.board) # This changes the 2d list/array the board uses into a tuple for hash comparing later.

				tempList.append(tempCopy)


			if self.blankSpaceX < (self.boardSize-1):
				tempCopy = self.copy()

				tempCopy.moves.append('Right')

				tempCopy.board[self.blankSpaceX][self.blankSpaceY] = self.board[self.blankSpaceX + 1][self.blankSpaceY]
				tempCopy.board[self.blankSpaceX + 1][self.blankSpaceY] = 0
            
				tempCopy.blankSpaceX = tempCopy.blankSpaceX + 1

				tempCopy.board = tempCopy.convert2DListTo2DTuple(tempCopy.board) # This changes the 2d list/array the board uses into a tuple for hash comparing later.

				tempList.append(tempCopy)
		

		return tempList

class GameBoard_for_DFS(GameBoard):
	"""docstring for GameBoard_for_DFS"""

	def __init__(self, initialBoard = None):
		super(GameBoard_for_DFS, self).__init__(initialBoard)
		#GameBoard.__init__(self, initialBoard)

	def copy(self):
		tempBoard = GameBoard_for_DFS()

		for y in xrange(0, GameBoard.boardSize):
			for x in xrange(0, GameBoard.boardSize):
				tempBoard.board[x][y] = self.board[x][y]
				if self.board[x][y] == 0:
					tempBoard.blankSpaceX = x
					tempBoard.blankSpaceY = y
		for c in xrange(0, len(self.moves)):
			tempBoard.moves.append(self.moves[c])
		tempBoard.branchLength = self.branchLength + 1

		return tempBoard


	#Creates more boards based on the neighbors where the blank space is located (Backwards)
	def neighbors(self):
		tempList = []

		#Add if statement here to control branch Length
		if self.branchLength < self.branchLimit:
			if self.blankSpaceX < (self.boardSize-1):																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																		
				tempCopy = self.copy()

				tempCopy.moves.append('Right')

				tempCopy.board[self.blankSpaceX][self.blankSpaceY] = self.board[self.blankSpaceX + 1][self.blankSpaceY]
				tempCopy.board[self.blankSpaceX + 1][self.blankSpaceY] = 0
            
				tempCopy.blankSpaceX = tempCopy.blankSpaceX + 1

				tempCopy.board = tempCopy.convert2DListTo2DTuple(tempCopy.board) # This changes the 2d list/array the board uses into a tuple for hash comparing later.

				tempList.append(tempCopy)


			if self.blankSpaceX > 0:
				tempCopy = self.copy()

				tempCopy.moves.append('Left')

				tempCopy.board[self.blankSpaceX][self.blankSpaceY] = self.board[self.blankSpaceX - 1][self.blankSpaceY]
				tempCopy.board[self.blankSpaceX - 1][self.blankSpaceY] = 0

				tempCopy.blankSpaceX = tempCopy.blankSpaceX - 1

				tempCopy.board = tempCopy.convert2DListTo2DTuple(tempCopy.board) # This changes the 2d list/array the board uses into a tuple for hash comparing later.
            
				tempList.append(tempCopy)


			if self.blankSpaceY < (self.boardSize-1):
				tempCopy = self.copy()

				tempCopy.moves.append('Down')

				tempCopy.board[self.blankSpaceX][self.blankSpaceY] = self.board[self.blankSpaceX][self.blankSpaceY + 1]
				tempCopy.board[self.blankSpaceX][self.blankSpaceY + 1] = 0
            
				tempCopy.blankSpaceY = tempCopy.blankSpaceY + 1

				tempCopy.board = tempCopy.convert2DListTo2DTuple(tempCopy.board) # This changes the 2d list/array the board uses into a tuple for hash comparing later.

				tempList.append(tempCopy)


			if self.blankSpaceY > 0:
				tempCopy = self.copy()

				tempCopy.moves.append('Up')

				tempCopy.board[self.blankSpaceX][self.blankSpaceY] = self.board[self.blankSpaceX][self.blankSpaceY - 1]
				tempCopy.board[self.blankSpaceX][self.blankSpaceY - 1] = 0

				tempCopy.blankSpaceY = tempCopy.blankSpaceY - 1

				tempCopy.board = tempCopy.convert2DListTo2DTuple(tempCopy.board) # This changes the 2d list/array the board uses into a tuple for hash comparing later.
            
				tempList.append(tempCopy)


		return tempList

class GameBoard_for_A_Star(GameBoard):
	"""docstring for Board_for_A_Star_Search"""

	goal = None 		# Is a 2D List/Array where [x][y]. It is used to find the estimated cost to the goal. This only needs to be initialized once.
	goalX = None 		# goalX Holds the x coordnate to the taget number in the goal, where the index number is the target number.
	goalY = None 		# goalY Holds the Y coordnate to the taget number in the goal, where the index number is the target number.
	timeReset = True 	# This is for reseting the time, but ***************** DELETE ME! **************************** This variable and method that would go with it would most likely be not needed based on how this will need to be run.

	def __init__(self, initialBoard = None, goalBoard = None):
		super(GameBoard_for_A_Star, self).__init__(initialBoard)
		#GameBoard.__init__(self, initialBoard)

		# Sets up the local variables.
		self.costSoFar = 0 # g(n)
		self.estimatedCost = 0 # Sets up the variable to be used later based on f(n) = g(n) + h(n). #self.estimatedCostToGoal() # f(n) = g(n) + h(n) # Not needed here. It takes up proccessing time.

		# ****************************** Being worked on! ****************************************
		# ********************** Trying to see if this will work faster **************************
		# This will hopefully speed up checking by turning two check min = every creation to one check.
		if GameBoard_for_A_Star.goal is None:
			if goalBoard is None: # Sees if the goal has been set yet and creates it manually if one has not been given.
			# Create Goal GameBoard
				GameBoard_for_A_Star.goal = [[0 for x in xrange(0, GameBoard.boardSize)]for y in xrange(0, GameBoard.boardSize)]
			
				count = 0
				for y in xrange(0, GameBoard.boardSize):				# Sets up the goal with a 2D list/arrat with consectutive numbers. This controls the y coordinate.
					for x in xrange(0, GameBoard.boardSize):			# This controls the x coordinate.
						GameBoard_for_A_Star.goal[x][y] = count 	# As count goes up by one in each loop, it sets goal with it to the new number.
						count = count + 1								# Adds 1 to count.
				self.setUpGoalXY()				# Sets up the XY coordinates for the goalX and goalY.

				GameBoard_for_A_Star.goal = self.convert2DListTo2DTuple(GameBoard_for_A_Star.goal) # Converts goal to a tuple.

			elif goalBoard is not None: 	# Sets the goal with a recieved goalBoard if goal has not been set yet.
				GameBoard_for_A_Star.goal = goalBoard							# Adds the goalBoard to goal
				self.setUpGoalXY()								# Sets up the XY coordinates for the goalX and goalY.
				GameBoard_for_A_Star.goal = self.convert2DListTo2DTuple(GameBoard_for_A_Star.goal) # Converts goal to a tuple.

			self.estimatedCost = self.estimatedCostToGoal()


		# ***************************** The original for the above *******************************
		#if GameBoard_for_A_Star.goal is None and goalBoard is None: # Sees if the goal has been set yet and creates it manually if one has not been given.
			# Create Goal GameBoard
		#	GameBoard_for_A_Star.goal = [[0 for x in xrange(0, GameBoard.boardSize)]for y in xrange(0, GameBoard.boardSize)]
			
		#	count = 0
		#	for y in xrange(0, GameBoard.boardSize):				# Sets up the goal with a 2D list/arrat with consectutive numbers. This controls the y coordinate.
		#		for x in xrange(0, GameBoard.boardSize):			# This controls the x coordinate.
		#			GameBoard_for_A_Star.goal[x][y] = count 	# As count goes up by one in each loop, it sets goal with it to the new number.
		#			count = count + 1								# Adds 1 to count.
		#	self.setUpGoalXY()				# Sets up the XY coordinates for the goalX and goalY.

		#	GameBoard_for_A_Star.goal = self.convert2DListTo2DTuple(GameBoard_for_A_Star.goal) # Converts goal to a tuple.

		#elif GameBoard_for_A_Star.goal is None and goalBoard is not None: 	# Sets the goal with a recieved goalBoard if goal has not been set yet.
		#	GameBoard_for_A_Star.goal = goalBoard							# Adds the goalBoard to goal
		#	self.setUpGoalXY()								# Sets up the XY coordinates for the goalX and goalY.
		#	GameBoard_for_A_Star.goal = self.convert2DListTo2DTuple(GameBoard_for_A_Star.goal) # Converts goal to a tuple.

		
	def setUpGoalXY(self):
		#if GameBoard_for_A_Star.goal is not None:
		listSize = GameBoard.boardSize * GameBoard.boardSize
		GameBoard_for_A_Star.goalX = range(0, listSize)
		GameBoard_for_A_Star.goalY = range(0, listSize)
		for y in xrange(0, GameBoard.boardSize):
			for x in xrange(0, GameBoard.boardSize):
				GameBoard_for_A_Star.goalX[GameBoard_for_A_Star.goal[x][y]] = x
				GameBoard_for_A_Star.goalY[GameBoard_for_A_Star.goal[x][y]] = y
			# Make goalX and goalY a tuple?
		GameBoard_for_A_Star.goalX = tuple(GameBoard_for_A_Star.goalX)
		GameBoard_for_A_Star.goalY = tuple(GameBoard_for_A_Star.goalY)

	# Calculates the cost to finish the board. ************ Is this right? ************
	def estimatedCostToGoal(self): # Uses the structure: f(n) = g(n) + h(n). It give the estimated cost to reach the goal board.
		heuristicCost = 0 # h(n)
		#piece = 0 # DELETE ME
		#print '\n\nNew heuristic cost!'
		for y in xrange(0, GameBoard.boardSize):				# Runs through the y coordinates of the board.
				for x in xrange(0, GameBoard.boardSize):		# Runs through the x coordinates of the board.
					if self.board[x][y] != 0:					# We don't want to count the blank space, so we skip it.
						#piece = abs(GameBoard_for_A_Star.goalY[self.board[x][y]] - y) + abs(GameBoard_for_A_Star.goalX[self.board[x][y]] - x)
						#print 'Piece: ', piece
						#print 'X: ', x, ' Y: ', y
						#print self.board[x][y]
						#heuristicCost = piece + heuristicCost
						heuristicCost = abs(GameBoard_for_A_Star.goalY[self.board[x][y]] - y) + abs(GameBoard_for_A_Star.goalX[self.board[x][y]] - x) + heuristicCost	# Counts each piece and calculates the cost to move each one.
		#print 'Total h(n) Heuristics: ', heuristicCost
		#print 'g(n): ', self.costSoFar
		#print 'Returning: ',self.costSoFar + heuristicCost

		return self.costSoFar + heuristicCost	# g(n) + h(n) I hope this is the way it's supposed to be.

	def copy(self):
		tempBoard = GameBoard_for_A_Star()

		for y in xrange(0, GameBoard.boardSize):
			for x in xrange(0, GameBoard.boardSize):
				tempBoard.board[x][y] = self.board[x][y]
				if self.board[x][y] == 0:
					tempBoard.blankSpaceX = x
					tempBoard.blankSpaceY = y
		for c in xrange(0, len(self.moves)):
			tempBoard.moves.append(self.moves[c])	# Is this the python way of doing it? What about tempBoard.moves = self.moves[:]
		#tempBoard.moves = self.moves[:]
		tempBoard.branchLength = self.branchLength + 1

		return tempBoard

	
	def neighbors(self): # Creates more boards based on the neighbors where the blank space is located.
		tempList = []

		# Change the blankSpace check to cover any board size.
		if self.branchLength < self.branchLimit:
			if self.blankSpaceY > 0:
				tempCopy = self.copy()

				tempCopy.moves.append('Up')

				# Changes spots of the zero/blank space with another spot.
				tempCopy.board[self.blankSpaceX][self.blankSpaceY] = self.board[self.blankSpaceX][self.blankSpaceY - 1]
				tempCopy.board[self.blankSpaceX][self.blankSpaceY - 1] = 0

				tempCopy.blankSpaceY = tempCopy.blankSpaceY - 1						# Changes the position y coordinate of zero.

				tempCopy.costSoFar = self.costSoFar + 1 							# Adds +1 to how much the cost it takes to move here.

				tempCopy.board = tempCopy.convert2DListTo2DTuple(tempCopy.board) 	# This changes the 2d list/array the board uses into a tuple for hash comparing later.

				tempCopy.estimatedCost = tempCopy.estimatedCostToGoal() 			# Update the f(n) cost to reach goal

				tempList.append(tempCopy)

			if self.blankSpaceY < (self.boardSize-1):
				tempCopy = self.copy()

				tempCopy.moves.append('Down')

				# Changes spots of the zero/blank space with another spot.
				tempCopy.board[self.blankSpaceX][self.blankSpaceY] = self.board[self.blankSpaceX][self.blankSpaceY + 1]
				tempCopy.board[self.blankSpaceX][self.blankSpaceY + 1] = 0
            
				tempCopy.blankSpaceY = tempCopy.blankSpaceY + 1						# Changes the position y coordinate of zero.

				tempCopy.costSoFar = self.costSoFar + 1 							# Adds +1 to how much the cost it takes to move here. 

				tempCopy.board = tempCopy.convert2DListTo2DTuple(tempCopy.board)	# This changes the 2d list/array the board uses into a tuple for hash comparing later.

				tempCopy.estimatedCost = tempCopy.estimatedCostToGoal() 			# Update the f(n) cost to reach goal

				tempList.append(tempCopy)

			if self.blankSpaceX > 0:
				tempCopy = self.copy()

				tempCopy.moves.append('Left')

				# Changes spots of the zero/blank space with another spot.
				tempCopy.board[self.blankSpaceX][self.blankSpaceY] = self.board[self.blankSpaceX - 1][self.blankSpaceY]
				tempCopy.board[self.blankSpaceX - 1][self.blankSpaceY] = 0

				tempCopy.blankSpaceX = tempCopy.blankSpaceX - 1						# Changes the position x coordinate of zero.

				tempCopy.costSoFar = self.costSoFar + 1 							# Adds +1 to how much the cost it takes to move here. 

				tempCopy.board = tempCopy.convert2DListTo2DTuple(tempCopy.board) 	# This changes the 2d list/array the board uses into a tuple for hash comparing later.

				tempCopy.estimatedCost = tempCopy.estimatedCostToGoal() 			# Update the f(n) cost to reach goal

				tempList.append(tempCopy)


			if self.blankSpaceX < (self.boardSize-1):
				tempCopy = self.copy()

				tempCopy.moves.append('Right')

				# Changes spots of the zero/blank space with another spot.
				tempCopy.board[self.blankSpaceX][self.blankSpaceY] = self.board[self.blankSpaceX + 1][self.blankSpaceY]
				tempCopy.board[self.blankSpaceX + 1][self.blankSpaceY] = 0
            
				tempCopy.blankSpaceX = tempCopy.blankSpaceX + 1						# Changes the position x coordinate of zero.

				tempCopy.costSoFar = self.costSoFar + 1 							# Adds +1 to how much the cost it takes to move here.  

				tempCopy.board = tempCopy.convert2DListTo2DTuple(tempCopy.board) 	# This changes the 2d list/array the board uses into a tuple for hash comparing later.

				tempCopy.estimatedCost = tempCopy.estimatedCostToGoal() 			# Update the f(n) cost to reach goal

				tempList.append(tempCopy)
		

		return tempList # Returns the neighbor list.



def Breath_First_Search(initialState, goalTest):
 
 	frontier = Queue(initialState)
 	explored = set() 
 	goalTest.forTesting() # TODO Here for testing.  ************************ Delete Me ***********************

 	while not frontier.isEmpty():
  		state = frontier.dequeue()
  		explored.add(state)
  
  		if goalTest.compare(state):
   			return state.success() 
  
  		for neighbor in state.neighbors():
   			if neighbor not in frontier.boards and neighbor not in explored: 
				frontier.enqueue(neighbor) 
  
 	return state.failure() #This needs work #For holding# Failure


def Depth_First_Search(initialState, goalTest):
	frontier = Stack(initialState)
	explored = set()
 	goalTest.forTesting() # TODO Here for testing.  ************************ Delete Me ***********************

	while not frontier.isEmpty():
		state = frontier.pop()
		explored.add(state)

		if goalTest.compare(state):
			return state.success()
  
  		for neighbor in state.neighbors():
   			if neighbor not in frontier.boards and neighbor not in explored:
				frontier.push(neighbor)
  
	return state.failure()

#Cost f(n) = g(n) + h(n)  where g(n) is the goal and h(n) is the heristics 
def A_Star_Search(initialState, goalTest):
 
 	frontier = Heap(initialState)
 	explored = set()
 	goalTest.forTesting() # TODO Here for testing.  ************************ Delete Me ***********************
 	#count = 0

  	print '\n************* 2 branch tree (Division) **************\n'

 	while not frontier.isEmpty():
  		state = frontier.deleteMin() #This is where some control lies
  		explored.add(state)

  		
		#print '\nNext Board:'   #************************ Delete Me ***********************
		#print 'Moves:'  #************************ Delete Me ***********************
		#print state.moves  #************************ Delete Me ***********************
		#for y in xrange(0, state.boardSize):  #************************ Delete Me ***********************
		#	print state.board [0][y], state.board [1][y], state.board [2][y], state.board [3][y]  #************************ Delete Me ***********************
		#count = count + 1
  
  		if goalTest.compare(state):
   			return state.success()
  
  		for neighbor in state.neighbors():
  			#print neighbor.board # ************************ Delete Me ***********************
  			#count = 0 # ************************ Delete Me ***********************
  			#print '\n\nNeighbor Board:'  # ************************ Delete Me ***********************
			#for y in xrange(0, 3): # ************************ Delete Me ***********************
			#	print neighbor.board [count][y], neighbor.board [count+1][y], neighbor.board [count+2][y] # ************************ Delete Me ***********************
   			
   			if neighbor not in frontier.boards and neighbor not in explored:
   				#print 'Adding Neighbor' # ************************ Delete Me ***********************
   				frontier.insert(neighbor)
   			elif neighbor in frontier.boards:
				frontier.decreaseKey(neighbor) #This is where some control lies
  
  	#print frontier.isEmpty() # ************************ Delete Me ***********************
 	return state.failure()

def main():
	#b = GameBoard([0,1,2,3,4,5,6,7,8])
	#c = GameBoard([0,9,2,3,4,5,6,1,8])
	#d = GameBoard([0,1,2,3,4,5,6,7,8])
	#e = GameBoard_for_BFS([0,9,2,3,4,5,6,1,8])

	#print b.compare(c)
	#print c.compare(d)
	#print d.compare(b)

	#print b.__hash__()
	#print c.__hash__()
	#print d.__hash__()

	#print b.board

	#print c.__hash__()
	#print e.__hash__()
	#print (e.copy()).__hash__() # This only works when the list coverter is in the copy() method.

	#print '\n'
	#print 'e board:'
	#print e.board
	#print '\n'
	#print 'neighbors'

	#for neighbor in e.neighbors():
	#	print 'Neighbor:'
	#	print neighbor.board
	#	print neighbor.moves
	#	print 'Hash:'
	#	print hash(neighbor.board)

	#l = [1,2,3,4,5]
	#print l
	#l2 = l[:] # Creates a copy, one that can be changed without affecting the original.
	#print l2
	#l2[2] = 6
	#print l2
	#print l
	#print l2

	#startTime = time.clock()
	#print 'Starting Timer'
	#print startTime

	#initialBoard = [1,2,5,3,8,4,6,0,7]
	#initialBoard = [2,4,5,1,0,8,3,6,7]
	#initialBoard = [0,8,7,6,5,4,3,2,1]
	initialBoard = [0,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
	#initialBoard = [1,2,5,3,4,0,6,7,8]
	#initialBoard = [1,2,3,7,4,5,6,0,8,9,10,11,12,13,14,15]
	#initialBoard = [1,2,5,3,4,8,6,7,0]
	#initialBoard = [1,2,3,7,4,5,6,11,8,9,10,15,12,13,14,0]
	goalBoard = range(0, len(initialBoard))
	
	# TODO be able to handle args
	# TODO IDA* Search

	print '\nStarting Board input:', initialBoard
	count = 0
	print '\nStarting Board:'
	for y in xrange(0, len(initialBoard)):
		if count == 0:
			print initialBoard[y],
			count = 1
		elif int(len(initialBoard)**0.5)-1 > count:
			print initialBoard[y],
			count = count + 1
		else:
			print initialBoard[y]
			count = 0
		#print initialBoard [count], initialBoard [count+1], initialBoard [count+2], initialBoard [count+3]
		#count = count + 4
	count = 0
	print '\nGoal Board:'
	for y in xrange(0, len(initialBoard)):
		if count == 0:
			print goalBoard[y],
			count = 1
		elif int(len(initialBoard)**0.5)-1 > count:
			print goalBoard[y],
			count = count + 1
		else:
			print goalBoard[y]
			count = 0


	print '\nDoing a A* Search'
	A_Star_Search(GameBoard_for_A_Star(initialBoard), GameBoard(goalBoard))

	#print '\nDoing a Breath First Search'
	#Breath_First_Search(GameBoard_for_BFS(initialBoard), GameBoard(goalBoard))

	#print '\nDoing a Depth First Search'
	#Depth_First_Search(GameBoard_for_DFS(initialBoard), GameBoard(goalBoard))

	#endTime = time.clock()
	#print 'Stopped timer'
	#print endTime

	#print 'Total Time elapsed:', (endTime - startTime)


if __name__ == '__main__': # Starts the main function.
	main()