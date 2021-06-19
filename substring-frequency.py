# Frequency of a substring in a string

string = input("Enter string: ")
pat = input("Enter pattern: ")
s = ""
i, count = 0, 0

while i <= len(string):
    try:
        for j in range(i, i+len(pat)):
            s += string[j]
        if (s == pat):
            count += 1
        s = ""
        i += 1
    except:
        break
    
print("String: {}".format(string))
print("Pattern: {}".format(pat))
print("Pattern frequency: {}".format(count))

''' Output:

String: aaaaaaaaaa
Pattern: aa
Pattern frequency: 9
'''