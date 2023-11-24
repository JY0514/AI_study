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

# 알고리즘 예제: 김치찌개 만들기 (실행은 안됨)
def create_food(kimchi):
    clean_pot()         # 1.냄비 닦기
    prepare_pot(kimchi) # 2. 냄비에 김치와 김칫국물 넣기
    heat_pot()          # 3. 냄비 끓이기
    add_pot(seasoning)  # 4. 양념 넣기

kimchi_stew = create_food(kimchi)
eat(kimchi_stew)

# 알고리즘 성능 표기법
# 대문자 O 표기법
