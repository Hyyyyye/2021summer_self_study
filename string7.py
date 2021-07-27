n1 , n2 = input().split()

list_n1 = reversed(list(n1))
list_n2 = reversed(list(n2))

n1_int = list(map(int,list_n1))
n2_int = list(map(int,list_n2)) 

for i in range(len(n1)) :

    if n1_int[i] > n2_int[i] :
        for j in range(len(n1)) :
            print(n1_int[j], end ='')
        break
    elif n1_int[i] < n2_int[i] :
        for j in range(len(n2)) :
            print(n2_int[j], end ='')
        break
    else :
        continue
    