''' 
* This is a Hackerrank problem.
* Usage of "string" modul.
'''

import string

def print_rangoli(size):
    alpha = string.ascii_uppercase
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(L[:0:-1]+L))

if __name__ == '__main__':
    n = int(input("Enter range: "))
    print_rangoli(n)
    
''' Output:

Enter range: 15

----------------------------O----------------------------
--------------------------O-N-O--------------------------
------------------------O-N-M-N-O------------------------
----------------------O-N-M-L-M-N-O----------------------
--------------------O-N-M-L-K-L-M-N-O--------------------
------------------O-N-M-L-K-J-K-L-M-N-O------------------
----------------O-N-M-L-K-J-I-J-K-L-M-N-O----------------
--------------O-N-M-L-K-J-I-H-I-J-K-L-M-N-O--------------
------------O-N-M-L-K-J-I-H-G-H-I-J-K-L-M-N-O------------
----------O-N-M-L-K-J-I-H-G-F-G-H-I-J-K-L-M-N-O----------
--------O-N-M-L-K-J-I-H-G-F-E-F-G-H-I-J-K-L-M-N-O--------
------O-N-M-L-K-J-I-H-G-F-E-D-E-F-G-H-I-J-K-L-M-N-O------
----O-N-M-L-K-J-I-H-G-F-E-D-C-D-E-F-G-H-I-J-K-L-M-N-O----
--O-N-M-L-K-J-I-H-G-F-E-D-C-B-C-D-E-F-G-H-I-J-K-L-M-N-O--
O-N-M-L-K-J-I-H-G-F-E-D-C-B-A-B-C-D-E-F-G-H-I-J-K-L-M-N-O
--O-N-M-L-K-J-I-H-G-F-E-D-C-B-C-D-E-F-G-H-I-J-K-L-M-N-O--
----O-N-M-L-K-J-I-H-G-F-E-D-C-D-E-F-G-H-I-J-K-L-M-N-O----
------O-N-M-L-K-J-I-H-G-F-E-D-E-F-G-H-I-J-K-L-M-N-O------
--------O-N-M-L-K-J-I-H-G-F-E-F-G-H-I-J-K-L-M-N-O--------
----------O-N-M-L-K-J-I-H-G-F-G-H-I-J-K-L-M-N-O----------
------------O-N-M-L-K-J-I-H-G-H-I-J-K-L-M-N-O------------
--------------O-N-M-L-K-J-I-H-I-J-K-L-M-N-O--------------
----------------O-N-M-L-K-J-I-J-K-L-M-N-O----------------
------------------O-N-M-L-K-J-K-L-M-N-O------------------
--------------------O-N-M-L-K-L-M-N-O--------------------
----------------------O-N-M-L-M-N-O----------------------
------------------------O-N-M-N-O------------------------
--------------------------O-N-O--------------------------
----------------------------O----------------------------

'''
