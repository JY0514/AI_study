#input()함수

print('문자열 입력')
val1 = input()

val2 = input('문자열 입력 : ')

print(val1)
print(val2)

first_data = int(input('첫 번째 정수를 입력하시오 : '))
second_data = int(input('두 번째 정수를 입력하시오 : '))
print(f'두 정수의 합은 {first_data + second_data} 입니다')

input_data = map(int, input().split(" "))
print(input_data)
# [2, 4, 5]

[a, b, c] = map(int, input().split(" "))
print(a, b, c)
# 2 4 5

# 아스키코드 변환
ord(str) => int
chr(int) => str