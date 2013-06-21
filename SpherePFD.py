
# ---------------------------
# Sogol Moshtaghi
# Oscar chavarria
# PFD
# ---------------------------
import Queue
import sys

# ------------
# PFD_read
# ------------
def PFD_read (r, a) :
    """
reads two ints into a[0] and a[1]
r is a reader
a is an array on int
return true if that succeeds, false otherwise
"""
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    size = len(l)
    l_idx = 1
    while l_idx < size :
		assert int(l[l_idx]) > 0 
		assert int(l[l_idx]) < 101
		assert int(l[0]) != 0 
		a[int(l[0])][l_idx-1] = int(l[l_idx])
		l_idx += 1
    return True
    


# ------------
# PFD_eval
# ------------
def PFD_eval(i,j,w):
	i_size = len(i[0])		#populating the list of successors created in PFD_solve
	idx = 1
	while i_size >  idx :	
		jdx = 1
		while i_size > jdx :
			if i[idx][jdx] != 0 :
				j[i[idx][jdx]].append(idx)
			jdx += 1
		idx += 1
	pq = Queue.PriorityQueue()
	i_size = len(i)
	idx = 1
	while i_size > idx :
		if i[idx][0] == 0:
			pq.put(idx)      #populating the PriorityQueue
		idx += 1
	return PFD_removal(i,pq,j,w)
	
	
# ------------
# PFD_removal
# ------------
def PFD_removal(i,pq,j,w):
	result = ""
	while not pq.empty():
		removal = pq.get()
		removal_list = []
		removal_list.append(removal)
		removal_size = len(removal_list)
		idx = 0
		while idx < removal_size :
			i[removal][0] = -1
			list_idx = [k for k, e in enumerate(j[removal]) if e != 0] #getting the list of indeces of non-zero elements in the successors list
			size_list_idx = len(list_idx)
			index = 0
			list_successors = []
			while index < size_list_idx:
				list_successors.append(j[removal][list_idx[index]])				#creating a list of actual successors using the index list 
				index += 1
			size_list_successors = len(list_successors)
			index = 0
			while index < size_list_successors:
				i[list_successors[index]][0] -= 1
				if i[list_successors[index]][0] == 0:
					pq.put(list_successors[index])
				index += 1
			idx += 1
		result += str(removal) + " "
	return PFD_print(w, result)	
					
		
# ------------
# PFD_print
# ------------
def PFD_print(w,v):
	w.write(v)
	

# ------------
# PFD_solve
# ------------
def PFD_solve (r, w) :
    """
read, eval, print loop
r is a reader
w is a writer
"""
	
    counter = 0
    s = r.readline()												
    if s == "" :													
		return false												
    l = s.split()													
    vertex_count = int(l[0])										
    rule_count = int(l[1])																														
    a = [[0]*(vertex_count+1) for _ in range(vertex_count+1)]	#Creates 2D list that has individual references to each cell
    successors = [[0]*(1) for _ in range(vertex_count+1)]
    while PFD_read(r, a) :	
		counter += 1
    v = PFD_eval(a, successors,w)													
        											


# ----
# main
# ----

PFD_solve(sys.stdin, sys.stdout)									
