word = input()
list_str = list(word)
num = 0
none = -1
alpa_num = [-1 for i in range(26)]
  
# baekjoon
for i in list_str :
    if i == 'a' :
        if alpa_num[0] == -1 :
             alpa_num[0] = num
    elif i == 'b' :
       if alpa_num[1] == -1 :
             alpa_num[1] = num
    elif i == 'c' :
        if alpa_num[2] == -1 :
             alpa_num[2] = num
    elif i == 'd' :
        if alpa_num[3] == -1 :
             alpa_num[3] = num
    elif i == 'e' :
        if alpa_num[4] == -1 :
             alpa_num[4] = num
    elif i == 'f' :
        if alpa_num[5] == -1 :
             alpa_num[5] = num
    elif i == 'g' :
        if alpa_num[6] == -1 :
             alpa_num[6] = num
    elif i == 'h' :
        if alpa_num[7] == -1 :
             alpa_num[7] = num
    elif i == 'i' :
        if alpa_num[8] == -1 :
             alpa_num[8] = num
    elif i == 'j' :
        if alpa_num[9] == -1 :
             alpa_num[9] = num
    elif i == 'k' :
        if alpa_num[10] == -1 :
             alpa_num[10] = num
    elif i == 'l' :
        if alpa_num[11] == -1 :
             alpa_num[11] = num
    elif i == 'm' :
        if alpa_num[12] == -1 :
             alpa_num[12] = num
    elif i == 'n' :
        if alpa_num[13] == -1 :
             alpa_num[13] = num
    elif i == 'o' :
        if alpa_num[14] == -1 :
             alpa_num[14] = num
    elif i == 'p' :
        if alpa_num[15] == -1 :
             alpa_num[15] = num
    elif i == 'q' :
        if alpa_num[16] == -1 :
             alpa_num[16] = num
    elif i == 'r' :
        if alpa_num[17] == -1 :
             alpa_num[17] = num
    elif i == 's' :
        if alpa_num[18] == -1 :
             alpa_num[18] = num
    elif i == 't' :
        if alpa_num[19] == -1 :
             alpa_num[19] = num
    elif i == 'u' :
        if alpa_num[20] == -1 :
             alpa_num[20] = num
    elif i == 'v' :
        if alpa_num[21] == -1 :
             alpa_num[21] = num
    elif i == 'w' :
        if alpa_num[22] == -1 :
             alpa_num[22] = num
    elif i == 'x' :
        if alpa_num[23] == -1 :
             alpa_num[23] = num
    elif i == 'y' :
        if alpa_num[24] == -1 :
             alpa_num[24] = num
    elif i == 'z' :
        if alpa_num[25] == -1 :
             alpa_num[25] = num
    num = num+1

for i in alpa_num :
    print(i , end =' ')