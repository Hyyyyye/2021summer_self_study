
num1 = input()
result = 0
num2 = input()

list_str = list(num2) # 문자열을 배열(list)로 하나씩 넣어줌
print(list_str)

list_int = list(map(int,list_str)) #배열의 문자를 정수형으로 바꿔줌
print(list_int)
print(sum(list_int))