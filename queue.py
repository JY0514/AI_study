import queue

# 데이터의 입력과 출력이 이루어지는 창구가 하나 제일 먼저 들어간 데이터가 제일 나중에 나옴

queue_list = list()


def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data


for index in range(10):
    enqueue(index)

    print(queue_list)