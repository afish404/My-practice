def MultiplicationTable():
    for i in range(1,10,1):
        
        for j in range(1,i+1,1):
            print(f'{j}*{i}={j*i}',end=" ")
        print()
        
MultiplicationTable()