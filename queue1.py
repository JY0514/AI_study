import queue

import queue
# 데이터의 입력과 출력이 이루어지는 창구가 하나 제일 먼저 들어간 데이터가 제일 나중에 나옴

# Queue(): 일반적인 큐 자료구조
data_queue = queue.Queue()
data_queue.put(1) # 1
data_queue.put(2) # 1 - 2
data_queue.put(3) # 1 - 2 - 3
data_queue.get() # 1 출력
data_queue.get() # 2 출력
print(data_queue)

# LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조
data_queue2 = queue.LifoQueue()
data_queue2.put(1) #1 
data_queue2.put(2)  #2 - 1
data_queue2.put(3) # 3 - 2 - 1
data_queue2.get() #3 출력
data_queue2.get() #2 출력
print(data_queue2)

# PriorityQueue(): 데이터마다 우선순위를 지정하여, 정렬된 큐로, 우선순위 높은 순으로 출력하는 구조
data_queue3 = queue.PriorityQueue()
data_queue3.put((10,1))
data_queue3.put((5,2))
data_queue3.put((15,3))
data_queue3.get()
data_queue3.get()

# 리스트로 queue구현
class ListQueue:
    def __init__(self):
        self.my_list = list()

    def put(self, element):
        self.my_list.append(element)

    def get(self):
        return self.my_list.pop(0)

    def qsize(self):
        return len(self.my_list)
#  Enqueue기능을 가지는 put 메서드 ,  Dequeue기능을 가진 get 메서드 , 큐의 길이를 반환하는 qsize 메서드를 구현한 코드

# 리스트로 PriorityQueue 구현
class ListPriorityQueue:
    def __init__(self):
        self.my_list = list()

    def put(self, element):
        self.my_list.append(element)
        self.my_list.sort(key=lambda x: x[0])

    def get(self):
        return self.my_list.pop(0)

    def qsize(self):
        return len(self.my_list)
# list의 메소드 중 하나인, sort를 이용하여 구현 작은 순서로 우선순위 정렬



queue_list = list()
#
# def enqueue(data):
#     queue_list.append(data)
#
# def dequeue():
#     data = queue_list[0]
#     del queue_list[0]
#     return data
#
#
# for index in range(10):
#     enqueue(index)
#
#     print(queue_list)