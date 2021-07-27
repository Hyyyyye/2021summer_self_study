import sys

alpa_max = 0
word = input()
word_list = list(word)
alpa_num = [0 for i in range(26)]

for i in word_list :
    if i == 'a' or i == 'A' :
        alpa_num[0] = alpa_num[0]+1
    elif i == 'b' or i == 'B':
        alpa_num[1] = alpa_num[1]+1
    elif i == 'c' or i == 'C':
         alpa_num[2] = alpa_num[2]+1
    elif i == 'd' or i == 'D':
         alpa_num[3] = alpa_num[3]+1
    elif i == 'e' or i == 'E':
         alpa_num[4] = alpa_num[4]+1
    elif i == 'f' or i == 'F':
        alpa_num[5] = alpa_num[5]+1
    elif i == 'g' or i == 'G':
         alpa_num[6] = alpa_num[6]+1
    elif i == 'h' or i == 'H':
         alpa_num[7] = alpa_num[7]+1
    elif i == 'i' or i == 'I':
         alpa_num[8] = alpa_num[8]+1
    elif i == 'j' or i == 'J':
         alpa_num[9] = alpa_num[9]+1
    elif i == 'k' or i == 'K':
         alpa_num[10] = alpa_num[10]+1
    elif i == 'l' or i == 'L':
         alpa_num[11] = alpa_num[11]+1
    elif i == 'm' or i == 'M':
         alpa_num[12] = alpa_num[12]+1
    elif i == 'n' or i == 'N':
         alpa_num[13] = alpa_num[13]+1
    elif i == 'o' or i == 'O':
         alpa_num[14] = alpa_num[14]+1
    elif i == 'p' or i == 'P':
         alpa_num[15] = alpa_num[15]+1
    elif i == 'q' or i == 'Q':
         alpa_num[16] = alpa_num[16]+1
    elif i == 'r' or i == 'R':
         alpa_num[17] = alpa_num[17]+1
    elif i == 's' or i == 'S':
         alpa_num[18] = alpa_num[18]+1
    elif i == 't' or i == 'T':
         alpa_num[19] = alpa_num[19]+1
    elif i == 'u' or i == 'U' :
         alpa_num[20] = alpa_num[20]+1
    elif i == 'v' or i == 'V':
         alpa_num[21] = alpa_num[21]+1
    elif i == 'w' or i == 'W':
         alpa_num[22] = alpa_num[22]+1
    elif i == 'x' or i == 'X':
         alpa_num[23] = alpa_num[23]+1 
    elif i == 'y' or i == 'Y':
         alpa_num[24] = alpa_num[24]+1
    elif i == 'z' or i == 'Z':
         alpa_num[25] = alpa_num[25]+1

max_tmp = alpa_num[0]

for i in range(26) :
     if max_tmp < alpa_num[i] :
          max_tmp = alpa_num[i] # 제일 많은 알파벳의 갯수
          alpa_max = i # 가장 많은 알파벳의 숫자번호

del alpa_num[alpa_max]      

for i in alpa_num :
    if i == max_tmp :
         print("?")
         exit()
         
result = ord('A')+int(alpa_max)
print(chr(result))