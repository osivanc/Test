#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2011
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array on int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (n, p) :
    """
    n is the beginning of the range, inclusive
    p is the end       of the range, inclusive
    return the max cycle length in the range [n, p]
    """
    assert n > 0
    assert p > 0
#
    if (n > p):
        k = n
        n = p
        p = k
    length_list = [0]*p
    assert n > 0, p > 0
    count = 1
    for i in range (n,p+1):
        origin = i
        while i > 1 :
            if (i <= p):
                if (length_list[i-1] > 0):
                    count += length_list[i-1]
                    length_list[origin-1] = count-1
                    break
            if (i % 2) == 0 :
                i = (i >> 1)
            else :
                i = (3 * i) + 1
            count += 1                
        if (i == 1):
            length_list[origin-1] = count
        count = 1
    return max(length_list)
#
    assert v > 0
    return v

# --------------------
# collatz_cycle_length
# --------------------

def collatz_cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n / 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)
