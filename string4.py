test_case = int(input())
repeat_num = [0 for i in range(test_case)]
repeat_str = [0 for i in range(test_case)]

for i in range(test_case) :
    rep_num , rep_str = input().split()
    repeat_num[i] = int(rep_num)
    repeat_str[i] = rep_str


for i in range(test_case):
    list_str = list(repeat_str[i])
   
    for j in list_str :
        for k in range(repeat_num[i]) :
            print(j, end ='')
    print()

