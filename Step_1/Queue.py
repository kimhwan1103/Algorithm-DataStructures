#큐(Queue) - FIFO(First In First Out) 구조
#한쪽 끝(rear)에서 삽입하고 반대쪽 끝(front)에서 꺼내는 선형 자료구조
#단일 연결 리스트의 append/popleft와 구조가 매우 유사

#노드 클래스 - 데이터와 다음 노드 참조를 저장
class Node:
    def __init__(self, data):
        self.data = data #노드가 저장할 데이터
        self.next = None #다음 노드를 가리키는 참조

#큐 클래스 - front와 rear를 관리
class Queue:
    def __init__(self):
        self.front = None #큐의 앞쪽 (꺼내는 쪽)
        self.rear = None  #큐의 뒤쪽 (넣는 쪽)

    #enqueue() - rear에 데이터 추가
    #1. 새 노드를 만든다
    #2. 큐가 비어있으면 front와 rear 모두 새 노드를 가리킴
    #3. 비어있지 않으면 현재 rear의 next를 새 노드로 연결하고 rear를 새 노드로 업데이트
    def enqueue(self, data):
        node = Node(data)
        if self.rear is None: #큐가 비어있는 경우
            self.front = node
            self.rear = node
        else:
            self.rear.next = node #현재 rear의 next에 새 노드 연결
            self.rear = node      #rear를 새 노드로 업데이트

    #dequeue() - front에서 데이터 꺼내기
    #1. front가 None이면 꺼낼 데이터가 없으므로 None 반환
    #2. 현재 front를 임시 변수에 저장
    #3. front를 다음 노드로 이동
    #4. front가 None이 되면 큐가 비었으므로 rear도 None으로
    #5. 임시 변수의 데이터를 반환
    def dequeue(self):
        if self.front is None: #큐가 비어있으면 None 반환
            return None
        node = self.front          #현재 front를 임시 저장
        self.front = self.front.next #front를 다음 노드로 이동
        if self.front is None:     #큐가 비었으면 rear도 None으로
            self.rear = None
        return node.data           #꺼낸 데이터 반환

    #peek() - front 데이터 확인 (제거하지 않음)
    def peek(self):
        if self.front is None: #큐가 비어있으면 None 반환
            return None
        return self.front.data #front의 데이터만 반환

    #is_empty() - 큐가 비어있는지 확인
    def is_empty(self):
        return self.front is None

    #큐 상태 출력
    def __str__(self):
        if self.front is None:
            return "Queue is empty!"
        res = "Front"
        node = self.front
        while node is not None:
            res += " -> " + str(node.data)
            node = node.next
        res += " <- Rear"
        return res


#큐 실행해보기
my_queue = Queue()

#enqueue 테스트
for i in range(1, 6):
    my_queue.enqueue(i)
    print(f"{i}을 enqueue. 큐 상태: {my_queue}")

#peek 테스트
print(f"\npeek: {my_queue.peek()}")

#dequeue 테스트
print()
for _ in range(3):
    val = my_queue.dequeue()
    print(f"{val}을 dequeue. 큐 상태: {my_queue}")

print(f"\nis_empty: {my_queue.is_empty()}")


#코딩 테스트에서는 deque로 큐를 간단하게 구현할 수 있다
#list의 pop(0)은 O(n)이므로 큐가 필요하면 collections.deque를 사용한다

from collections import deque

queue = deque()        #큐 초기화
queue.append(1)        #enqueue [1]
queue.append(2)        #enqueue [1, 2]
queue.append(3)        #enqueue [1, 2, 3]
val = queue.popleft()  #dequeue -> 1, queue = [2, 3]
front = queue[0]       #peek -> 2
is_empty = not queue   #is_empty -> False


#덱(Deque) - 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조
#스택과 큐의 기능을 모두 포함한다

dq = deque()
dq.append(1)        #오른쪽 끝에 추가 [1]
dq.appendleft(0)    #왼쪽 끝에 추가 [0, 1]
dq.append(2)        #오른쪽 끝에 추가 [0, 1, 2]
dq.pop()             #오른쪽 끝에서 꺼내기 -> 2, dq = [0, 1]
dq.popleft()         #왼쪽 끝에서 꺼내기 -> 0, dq = [1]

#rotate - 원하는 만큼 좌, 우로 회전
#양수면 오른쪽, 음수면 왼쪽으로 회전
dq_rotate = deque([1, 2, 3, 4, 5])
dq_rotate.rotate(2)   #[4, 5, 1, 2, 3] - 오른쪽으로 2칸
dq_rotate.rotate(-1)  #[5, 1, 2, 3, 4] - 왼쪽으로 1칸

#maxlen - 최대 길이 제한 (초과 시 반대쪽에서 자동 제거)
dq_max = deque(maxlen=3)
dq_max.append(1)  #deque([1])
dq_max.append(2)  #deque([1, 2])
dq_max.append(3)  #deque([1, 2, 3])
dq_max.append(4)  #deque([2, 3, 4]) - 1이 자동으로 제거됨


'''
활용 문제 (출처 : 프로그래머스)
프로세스

운영체제의 역할 중 하나는 컴퓨터 시스템의 자원을 효율적으로 관리하는 것입니다.
이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.

1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.

예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 대기 중이고 우선순위가 [2, 1, 3, 2]라면
C -> D -> A -> B 순서로 실행됩니다.

입출력예
priorities = [2, 1, 3, 2], location = 2 -> return 1
priorities = [1, 1, 9, 1, 1, 1], location = 0 -> return 5
'''

def solution(priorities: list[int], location: int) -> int:
    #(인덱스, 우선순위) 쌍으로 큐를 만든다
    queue = deque(enumerate(priorities))
    order = 0 #실행 순서 카운터

    while queue:
        current = queue.popleft() #큐에서 프로세스 하나 꺼냄
        #큐에 현재보다 우선순위가 높은 프로세스가 있는지 확인
        if any(current[1] < item[1] for item in queue):
            queue.append(current) #더 높은 우선순위가 있으면 다시 큐에 넣음
        else:
            order += 1 #실행 순서 증가
            if current[0] == location: #찾는 프로세스이면 순서 반환
                return order

print(solution([2, 1, 3, 2], 2))       #1
print(solution([1, 1, 9, 1, 1, 1], 0)) #5
