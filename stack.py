def recursive(data):
    if data <0:
        print("ended")
    else:
        print(data)
        recursive(data - 1)
        print("returned",data)
# recursive(4)

# 스택은 처음 들어간 것이 가장 마지막에 나오도록 되어있는 구조
# FILO,LIFO 요소의 삽입과 삭제가 자료구조의 한쪽 끝에서만 이루어지는 것
# 리스트 변수로 스택
stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)

pop()


# 배열을 사용하여 스택 구현

