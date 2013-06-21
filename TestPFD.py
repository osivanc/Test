

# -------------------------------
# Sogol Moshtaghi
# Oscar chavarria
# -------------------------------

"""
To test the program:
% python TestPFD.py >& TestPFD.py.out
% chmod ugo+x TestPFD.py
% TestPFD.py >& TestPFD.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest
import sys
import Queue

from PFD import PFD_read, PFD_eval, PFD_print, PFD_solve, PFD_removal

# -----------
# TestPFD
# -----------

class TestPFD (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read1 (self) :
        r = StringIO.StringIO("2 1 1\n1 1 2")
        a = [[0]*(3) for _ in range(3)]
        successors = [[0]*(1) for _ in range(3)]
        b = PFD_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0][0] == 0)
        self.assert_(a[0][1] == 0)
        self.assert_(a[0][2] == 0)
        b = PFD_read(r, a)
        self.assert_(a[1][0] == 1)
        self.assert_(a[1][1] == 2)
        self.assert_(a[1][2] == 0)  
        b = PFD_read(r, a)      
        self.assert_(a[2][0] == 1)
        self.assert_(a[2][1] == 1)
        self.assert_(a[2][2] == 0)
        
        
    def test_read2 (self) :
        r = StringIO.StringIO("3 2 1 5")
        a = [[0]*(5) for _ in range(5)]
        b = PFD_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0][0] == 0)
        self.assert_(a[0][1] == 0)
        self.assert_(a[0][2] == 0)
        self.assert_(a[3][0] == 2)
        self.assert_(a[3][1] == 1)
        self.assert_(a[3][2] == 5)
        
    def test_read3 (self) :
        r = StringIO.StringIO("1 7 3 4 5 6 7 8 9")
        a = [[0]*(9) for _ in range(9)]
        b = PFD_read(r, a)
        self.assert_(b == True)
        self.assert_(a[1][0] == 7)
        self.assert_(a[1][1] == 3)
        self.assert_(a[1][2] == 4)
        self.assert_(a[1][3] == 5)
        self.assert_(a[1][4] == 6)
        self.assert_(a[1][5] == 7)    
        self.assert_(a[1][6] == 8)
        self.assert_(a[1][7] == 9)        
        
	# ----
    # eval
    # ----
    def test_eval1 (self):
		a = [[0,0,0],[1,2,0],[1,1,0]]
		successors = [[0]*(1) for _ in range(3)]
		w = sys.stdout
		b = PFD_eval(a,successors,w)
		self.assert_(successors[1][1] == 2)        #Testing the list of successors
		self.assert_(successors[2][1] == 1)
		self.assert_(successors[0][0] == 0)
		self.assert_(successors[1][0] == 0)

    def test_eval2 (self):
		a = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [2, 5, 3, 0, 0, 0], [2, 1, 5, 0, 0, 0], [1, 3, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0]]
		successors = [[0]*(1) for _ in range(6)]
		w = sys.stdout
		b = PFD_eval(a,successors,w)
		self.assert_(successors == [[0], [0,3,5], [0], [0, 2,4], [0], [0,2,3]])        #Testing the list of successors    
   
    def test_eval3 (self):
		a = [[0,0,0,0],[0,0,0,0],[2,1,3,0],[1,1,0,0]]
		successors = [[0]*(1) for _ in range(4)]
		w = sys.stdout
		b = PFD_eval(a,successors,w)
		self.assert_(successors == [[0],[0,2,3],[0],[0,2]])        #Testing the list of successors

	# -----------
    # PFD_removal
    # -----------
    def test_removal1 (self):
		a = [[0,0,0],[1,2,0],[1,1,0]]
		successors = [[0],[0,2],[0,1]]
		pq = Queue.PriorityQueue()
		w = sys.stdout
		b = PFD_removal(a,pq,successors,w)
		self.assert_(b == "")	     
        
# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
