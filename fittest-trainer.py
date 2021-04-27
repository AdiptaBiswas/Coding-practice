oxygen_avg = {}
flag = 0

for i in ["A", "B", "C"]:
    s = 0
    for j in range(1, 4):
        oxy = int(input("Enter: "))
        if oxy >= 1 and oxy <= 100:
            s += oxy
            print("{}'s Round-{} oxygen: {}".format(i, str(j), str(oxy)))
        else:
            print("Invalid input..")
            flag = 1
            break
    if flag != 1:
        oxygen_avg[i] = round(s/j)
        print("\n")
    else:
        break
    
if flag == 0:    
    winners = list({k for k, v in oxygen_avg.items() if v == max(oxygen_avg.values())})
    for w in winners:
        print("Trainer: {}\n".format(w))
        
''' Output:

Enter: 98                                                                                                                                       
A's Round-1 oxygen: 98                                                                                                                          
Enter: 99                                                                                                                                       
A's Round-2 oxygen: 99                                                                                                                          
Enter: 96                                                                                                                                       
A's Round-3 oxygen: 96                                                                                                                          
                                                                                                                                                
                                                                                                                                                
Enter: 98                                                                                                                                       
B's Round-1 oxygen: 98                                                                                                                          
Enter: 99                                                                                                                                       
B's Round-2 oxygen: 99                                                                                                                          
Enter: 99                                                                                                                                       
B's Round-3 oxygen: 99                                                                                                                          
                                                                                                                                                
                                                                                                                                                
Enter: 99                                                                                                                                       
C's Round-1 oxygen: 99                                                                                                                          
Enter: 98                                                                                                                                       
C's Round-2 oxygen: 98                                                                                                                          
Enter: 96                                                                                                                                       
C's Round-3 oxygen: 96                                                                                                                          
                                                                                                                                                
                                                                                                                                                
Trainer: B                                                                                                                                      
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
...Program finished with exit code 0                                                                                                            
Press ENTER to exit console. 

'''