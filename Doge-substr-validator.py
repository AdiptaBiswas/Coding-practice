''' 

         || Problem set: Geeksforgeeks ||
         
* Given a string 'str' of lowercase letters.
* Require to find the number of times the word 'doge' appears
in a string
* Also, the 'g' in doge can be replaced by any letter from 'a-z'
so 'dope' is also 'valid'

Example 1: str = 'dogedopedose'
Output 1: 3

Example 2: str = 'dog'
Output 2: 0

'''

for i in range(len(string)-3):
    for j in range(i, i+len("doge")):
        temp += string[j]
        print(temp)
    print(" ")
    if temp[0:2] == "do" and temp[3] == "e":
        count += 1
    temp = ""
print(count)

#{ 
#Driver Code Starts.

def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        print(doge_count(str))
        testcases -= 1

if __name__=='__main__':
    main()
