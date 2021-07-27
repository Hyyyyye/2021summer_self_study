phone = input()
phone_list = list(phone)
phone_num = [0 for i in range(9)]
result = 2*len(phone)

for i in phone_list :
    if i == 'A' or i == 'B' or i == 'C' :
        phone_num[1] = phone_num[1]+1
    elif i == 'D' or i == 'E' or i == 'F' :
        phone_num[2] = phone_num[2]+2
    elif i == 'G' or i == 'H' or i == 'I' :
        phone_num[3] = phone_num[3]+3
    elif i == 'J' or i == 'K' or i == 'L' :
        phone_num[4] = phone_num[4]+4
    elif i == 'M' or i == 'N' or i == 'O' :
        phone_num[5] = phone_num[5]+5
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        phone_num[6] = phone_num[6]+6
    elif i == 'T' or i == 'U' or i == 'V' :
        phone_num[7] = phone_num[7]+7
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        phone_num[8] = phone_num[8]+8

for i in phone_num :
    result = i + result
print(result)
