''' 
* A naive GCD calculator of given 2 integers
* Complexity: O(n)
'''

def maxi(m,n):
    if m < n:
        return m
    else:
        return n

def divisor(m,n):
    smaller = maxi(m,n)
    for i in range(1, smaller+1):
        if n % i == 0 and m % i == 0:
            fac = i
    print(fac)
    
divisor(1947, 14748)

'''
Output: 3
'''
