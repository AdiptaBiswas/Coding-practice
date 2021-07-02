''' 
* "Merge the Tools!" - String problem from Hackerrank.
* Sample Input:

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

* Sample Output:

AB
CA
AD
'''

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        strHold = ""
        for c in string[i : i+k]:
            if (c not in strHold):
                strHold+=c
        print(strHold)

if __name__ == '__main__':
    string, k = input(), int(input())
    print("\n")
    merge_the_tools(string, k)
    
'''
Output:

AABCRDAABSC
3


AB
CRD
AB
SC
'''
