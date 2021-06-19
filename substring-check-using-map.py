# Find whether an array is subset of another array using Map

Arr1 = [11, 1, 13, 21, 3, 7]
Arr2 = [11, 3, 7, 1]
Map = {}
counter = 0

for i in range(len(Arr2)):
    if (Arr2[i] in Arr1 and Arr2[i] not in Map):
        Map[Arr2[i]] = counter + 1
        
counter = 0
for k,v in Map.items():
    counter += v
    
if (counter != len(Arr2)):
    print("Arr2 is not a substring of Arr1")
else:
    print("Arr2 is a substring of Arr1")
    
''' Output:

    Arr2 is a substring of Arr1
    
'''