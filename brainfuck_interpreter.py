cells=[]
numofcells=30000
index=0

#start of function
def brainfuck(source):
	printvalue = ""
	for i in xrange(numofcells):
		cells.append(chr(0))
	global index
	iterator=0
	while(iterator < len(source)):
		# + : Increments the value at the current cell by one.
		if source[iterator]=='+': 
			cells[index]=chr(ord(cells[index])+1)
			iterator+=1
		# - : Decrements the value at the current cell by one.
		elif source[iterator]=='-': 
			cells[index]=chr(ord(cells[index])-1)
			iterator+=1
		# < : Moves the data pointer to the next cell (cell on the left)
		elif source[iterator]=='<': 
			index-=1
			iterator+=1
		# > : Moves the data pointer to the previous cell (cell on the right).
		elif source[iterator]=='>': 
			index+=1;
			iterator+=1
		# . : Prints the ASCII value at the current cell (i.e. 65 = 'A')
		elif source[iterator]=='.':  
			printvalue+=cells[index]
			iterator+=1
		# , : Reads a single input character into the current cell.
		elif source[iterator]==',': 
			cells[index]=chr(int(raw_input()))
			iterator+=1
		#[ : If the value at the current cell is zero, skips to the corresponding ] .
	    #    Otherwise, move to the next source.'''
		elif source[iterator]=='[':
			#print iterator, ord(cells[index])
			if cells[index]==chr(0):
				iterator+=1
				count=0
				while(True):
					if(source[iterator]=='['):
						count+=1
					elif(source[iterator]==']'):
						count-=1
					if count == -1:
						break
					#print source[iterator],
					iterator+=1;
					if iterator>=len(source):
						print "Symbols are not paired!!!"
						return;
			else:
				iterator+=1
			# ] : If the value at the current cell is zero, move to the next source.
			#     Otherwise, move backwards in the sources to the corresponding [ .
		elif source[iterator]==']':
			#print iterator,ord(cells[index])
			if cells[index]==chr(0):
				iterator+=1
			else:
				count=0
				iterator-=1
				while(True):
					if(source[iterator]=='['):
						count-=1
					elif(source[iterator]==']'):
						count+=1
					if count == -1:
						break;
					iterator-=1
					if iterator<0:
						print "Symbol not paired"
						return;
		else:
			iterator+=1
	print printvalue
#end of function

def main():
	inputstring = raw_input(">").strip()
	brainfuck(inputstring),
if __name__ == '__main__':
	main()