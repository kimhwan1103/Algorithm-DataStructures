#파이썬은 모든 것이 객체이므로 변수는 객체를 참조한다.
#파이썬에서는 객체 지향방식으로 연결리스트를 비교적 쉽게 구현할 수 있음
#구현 방법

class Node:
    def __init__(self, data):
        self.data = data #data는 값을 가리키는 변수
        self.next = None #next는 다음 노드를 가리키는 변수

#간단한 연결 리스트 만들기
#1. 첫번째 노드를 만들고 hea에 할당
#2. 두번째 노드를 만들고 head.next가 두 번째 노드를 가리키도록 함
#3. 세번째 노드를 만들고 head.next.next가 세번째 노드를 가리키도록 함

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

#연결 리스트의 값 출력
#1. head부터 마지막 노득까지 이동하면서 data 출력
#2. head는 연결 리스트의 시작이므로 head가 이동하면서 연결리스트를 잃게 된다
#3. 변수를 만들고 head부터 마지막 노드까지 이동하면서 data를 출력
#4. 마지막 노드의 next는 None이므로 노드가 None이 아닐 동안 계속 이동하면서 data 출력

node = head
while node:
    print(node.data)
    node = node.next

#반복문 결과 : 1, 2, 3

#연결리스트의 끝에 새 노드를 추가하기
#1. 변수를 만들고 head부터 마지막 노드까지 이동
#2. 마지막 노드의 next가 새 노드를 가리키도록 한다

node = head
while node:
    if node.next is None:
        node.next = Node(4)
        break
    node = node.next

#좀더 축약버전으로 작성하면 아래와 같다
node = head
while node.next:
    node = node.next
node.next = Node(4)

#연결 리스트의 처음에 새 노드를 추가
#1. 추가할 노드를 생성
#2. 추가할 노드의 next가 head를 가리키게 한다
#3. head를 추가한 노드로 이동시킨다

node = Node(0)
node.next = head
head = node

#연결리스트 클래스 만들기

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length
    
    #appendleft() 만들기
    #head가 None이면 새로 만든 노드를 head에 바로 할당
    #만약에 head가 None이 아니면
    #1. 새 노드를 만든다
    #2. 새노드의 next에 현재 head를 연결
    #3. head를 새 노드로 ㅛ체
    #4. 마지막으로 리스트의 길이를 1 증가시킨다.
    def appendleft(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.length += 1

    #append() 만들기
    #head가 None이면 생성한 노드를 head에 할당
    #만약에 head가 None이 아니면
    #1. 임시 노드를 만들어 마지막 노드까지 이동
    #2. 새 노드를 만든다
    #3. 임시 노드의 next에 새 노드를 할당
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.length += 1

    #__str__구현하여 print()에 연결 리스트 상태를 직관적으로 출력
    def __str__(self):
        if self.head is None:
            return "Linked list is empty!"
        res = "Head"
        node = self.head
        while node is not None:
            res += " -> " + str(node.data)
            node = node.next
        return res
    
    #popleft() 만들기
    #연결 리스트에서 노드를 삭제하는 일은 추가하는 것보다 고려해야할것이 많다 
    #리스트에서 첫번째 노드를 꺼내려면 head는 그 다음 노드를 가리켜야 한다
    #하지만 값을 반환해야 하므로 head를 옮기기전에 현재 head를 임시 변수에 저장해야 한다.
    #head가 None이면 꺼낼 노드가 없으므로 None을 반환
    #그렇지 않으면
    #1. 현재 head를 임시 노드에 저장
    #2. head를 head.next로 이동
    #3. 리스트의 길이를 1 줄임
    #4. 임시 노드의 데이터를 반환
    def popleft(self):
        if self.head is None: #head가 None이면 None을 리턴
            return None
        node = self.head #현재 head를 임시 노드에 저장
        self.head = self.head.next #head.next을 head에 할당
        self.length -= 1 #연결 리스트 길이 -1하기
        return node.data #임시 노드에서 데이터 반환
    
    #pop() 만들기
    #마지막 노드를 제거하기 위해서 이전 노드의 next를 None으로 바꿔주는 작업이 추가로 필요
    #이를 위해서 현재 노드뿐만 아니라 그 이전 노드도 함께 기억해줘야 한다
    #head가 None이면 꺼낼 값이 없으므로 None을 반환
    #그렇지 않으면
    #1. node와 prev라는 두개의 임시 노드를 만든다
    #2. node는 head부터 시작하여 마지막 노드까지 이동한다
    #3. 이때 prev는 항상 node의 이전 노드를 따라간다
    #4. 마지막 노드의 이전 노드의 next를 None으로 바꾼다
    #5. 만약 노드가 하나뿐이라면 prev는 존재하지 않으면 head를 None으로 만듬
    #6. 리스트의 길이를 1줄이고 마지막 노드의 값을 반환
    def pop(self):
        if self.head is None: #head가 None이면 None을 리턴
            return None
        node = self.head #
        while node.next is not None:
            prev = node
            node = node.next
        if node == self.head:
            self.head = None
        else:
            prev.next = None
        self.length -= 1
        return node.data
    
    #remove() 만들기
    #popleft, pop 메서드에서 사용된 아이디어를 적절히 조합해서 만들수 있음
    #1. 임시 노드 2개를 만듬 node, prev
    #2. node는 삭제할 값을 찾을 때까지 이동하고 prev는 그 뒤를 따라감
    #3. 삭제할 값을 찾으면 perv.next를 node.next로 바꿔 연결을 끊음 그리고 True를 반환
    #4. 삭제할 값이 없거나 리스트를 비어 있으면 False를 반환
    #5. 삭제할 값이 head에 있는 경우 따로 처리
    def remove(self, target):
        if self.head is None: #head가 None이면 False로 반환
            return False
        node = self.head #헤드를 노드로 할당
        while node is not None and node.data != target: #노드가 None이 아니고 타겟값이 아닐때까지 반복문 돌림
            prev = node #노드를 prev값에 할당
            node = node.next #노드 데이터값을 노드에 할당
        if node is None: #노드가 None이 False로 반환
            return False
        if node == self.head: #노드가 헤드값이면 헤드값을 head.next으로 할당
            self.head = self.head.next
        else: 
            prev.next = node.next #그게 아니면 prev.next에 node.next을 할당
        self.length -= 1 #데이터를 삭제하기 때문에 길이 한개 지우기
        return True
    
    #insert() 만들기
    #특정 인덱스에 노드를 삽입할 때 처리할 단계가 더 많음 그리고 인덱스가 범위를 벗어났을 때 어떻게 처리할지 고려해야 함
    #1. 인덱스가 0보다 작으면 인덱스 0에 삽입
    #2. 인덱스가 연결 리스트의 길이보다 크면 맨 끝에 삽입
    #3. 그 외의 경우 다음과 같이 처리
    #3-1. 임시 노드를 만들어 삽입 지점 바로 앞까지 이동
    #3-2. 새 노드를 만듬
    #3-3. 새 노드의 next를 임시 노드의 다음 노드로 지정
    #3-4. 임시 노드의 next를 새 노드로 바꿈
    def insert(self, i, data):
        if i <= 0: #0보다 작으면 left으로 삽입
            self.appendleft(data)
        elif i >= self.length: #인덱스가 연결리스의 길이보다 크면 맨 끝에 삽입
            self.append(data)
        else: #그외 상황
            node = self.head #헤드를 노드에 할당
            for _ in range(i - 1):
                node = node.next
            new_node = Node(data) #새로운 노드 만듬
            new_node.next = node.next 
            node.next = new_node #다음 연결 리스트에 연결
            self.length += 1 #추가했으니 길이 증가

    #reverse() 만들기
    #reverse을 구현할려면 임시 노드가 최소 두개이상 필요
    #node.next를 바로 이전 노드로 바꾸면 다음 노드로 이동할 경로가 끊어지는 문제가 발생
    #예를 들어 prev가 값이 1인 노드 node가 값 2인 노드를 가리킬 때
    #node.next = prev로 연결을 바꾸면 원래 node.next였던 값 3인 노드와 연결이 끊어진다
    #즉 연결 리스트으 ㅣ뒷부분을 잃어버리게 된다
    #또한 head가 마지막 노드로 이동해야한다는 점도 잊지 말아야한다
    #이러한 방법을 해결하기 위해 연결이 끊어지지 않도록 하기 위해 다음 노드를 미리 저장할 변수 ahead를 추가
    #1. 임시 노드 prev와 ahead를 만듬
    #2. prev에는 None, ahead에는 head.next를 넣음
    #3. ahead가 None이 아닐 때까지 반복
    #3-1. head.next = prev
    #3-2. prev = ahead
    #3-3. head = ahead 
    #3-4. ahead = ahead.next
    #4. 마지막 남은 head.next = prev를 한 번 더 해줘야 완전히 뒤집힘
    def reverse(self):
        if self.length < 2: #길이가 2이상 일때 진행
            return
        prev = None #prev을 None으로 초기화
        ahead = self.head.next #ahead를 head.next으로 할당
        while ahead: #ahead가 None이 아닐때까지 반복
            self.head.next = prev 
            prev = self.head
            self.head = ahead
            ahead = ahead.next
        self.head.next = prev


#appendleft 실행해보기
my_list = LinkedList()
print(f"연결 리스트 생성. 연결 리스트의 길이 = {len(my_list)}")
for i in range(4):
    my_list.appendleft(i)
    print(f"{i}을 추가 연결리스트의 길이 = {len(my_list)}")

#append 실행
for i in range(4):
    my_list.append(i)
    print(f"{i}을 추가 연결리스트의 길이 = {len(my_list)}")

#이중 연결리스트 형태로도 만들어보자
#이중 연결리스트는 다음 노드를 가리키는 참조만 가지는것만 아니라 이전 노드를 가지는 참조까지 모두 가져야 함
#단일 연결 리스트와 달리 이중 연결 리스트는 양쪽 방향으로 모두 순회할 수 있다
#즉 특정 노드 앞이나 뒤에 데이터를 삽입/삭제하는 것이 매우 쉽다

#노드 클래스 설계
#여기에서는 데이터와 이전 노드정보, 다음 노드 정보를 담고 있어야함
class DualNode:
    def __init__(self, data):
        self.data = data #노드가 저장할 실제 데이터
        self.prev = None #이전 노드를 가리키는 참조
        self.next = None #다음 노드를 가리키는 참조

#이중 연결 리스트 클래스 설계
#노드들을 연결하고 관리할 리스트 클래스를 만듬
#가장 중요한 것은 리스트의 시작점인 head와 끝점인 tail을 항상 알고 있어야함
class DoublyLinkedList:
    def __init__(self):
        self.head = None #리스트의 첫번째 노드
        self.tail = None #리스트의 마지막 노드
        self.size = 0 #리스트에 들어있는 노드의 개수

    #append()구현
    #새로운 노드를 만들고 현재 tail과 연결해 주면 됨
    def append(self, data):
        new_node = DualNode(data)

        #리스트가 비어있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #리스트에 이미 노드가 있는 경우
        else:
            self.tail.next = new_node #현재 마지막 노드의 next를 새 노드로 지정
            new_node.prev = self.tail #새 노드의 prev를 현재 마지막 노드로 지정
            self.tail =new_node #tail을 새 노드로 업데이트
        self.size += 1

    #appendleft() 구현
    #새로운 노드를 리스트의 가장 앞에 위치시키는 기능
    def appendleft(self, data):
        new_node = DualNode(data)

        #리스트가 비어있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #리스트에 이미 노드가 있는 경우
        else:
            new_node.next = self.head #새 노드의 next를 현재 head로 지정
            self.head.prev = new_node #현재 head의 prev를 새 노드로 지정
            self.head = new_node #head를 새 노드로 업데이트
        
        self.size += 1

    #remove() 구현
    #원하는 데이터를 가진 노드를 찾아 삭제하는 기능 
    #이중 연결 리스트의 장점이 드러나느 부분
    #이전 노드의 정보를 알고 있기 때문에 삭제가 단일 리스트보다 직관적임
    def remove(self, data):
        current = self.head

        while current:
            #삭제할 데이터를 찾은 경우
            if current.data == data:
                #1. 삭제할 데이터가 head인 경우
                if current == self.head:
                    self.head = current.next
                    if self.head: #노드가 하나만 있었던 것이 아니면
                        self.head.prev = None
                    else: #노드가 하나뿐이었다면
                        self.tail = None
                #2. 삭제할 노드가 tail인 경우
                elif current ==self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                
                #3.삭제할 노드가 중간에 있는 경우
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                
                self.size -= 1
                return True #삭제 성공

            current = current.next #다음 노드로 이동
        
        return False #삭제할 데이터를 찾지 못할 경우
    
    #전체 리스트 출력
    def print_forward(self):
        #head부터 tail까지 순방향 출력
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(f"<-> {elements}")
    
    def print_backward(self):
        #tail부터 head까지 역방향 출력
        current = self.tail
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        print(f"<-> {elements}")


#원형 연결 리스트를 구현할때 일반적으로 단일 연결 리스트를 사용한다.
#하지만 원형 연결 리스트는 마지막 노드의 next를 참조를 다시 첫번째 노드 head를 가리키도록 한다

#원형 연결 리스트 클래스 구현
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None #삽임 최적화를 위해 tail 참조 유지

    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)

        #리스트가 비어있을 경우 새로운 노드가 head이자 tail가 됨
        if self.is_empty():
            #원형 구조의 핵심인 자기 자신을 가리키게 함
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            #기존 tail의 다음에 새 노드를 연결
            self.tail.next = new_node
            #tial 참조를 새 노드로 업데이트
            self.tail = new_node
            #새로운 tail이 다시 head를 가리키도록 하여 원형을 유지
            self.tail.next = self.head

    #리스트를 순회할 수 있도록 이터레이터를 제공
    def __iter__(self):
        if self.is_empty():
            return
        
        current = self.head
        while True:
            yield current.data
            current = current.next
            #순회하다가 다시 head로 돌아오면 루프를 종료
            if current == self.head:
                break
    
    #리스트의 구조를 직관적으로 출력
    def display(self):
        if self.is_empty():
            print("리스트가 비어 있습니다")
            return
        
        #__iter__가 구현되어 있으므로 리스트 컴프리헨션을 사용할 수 있음
        elements = [str(data) for data in self]
        print(f" -> {elements} -> (Back to Head : {str(self.head.data)})")



#연결리스트랑 제일 비슷한 deque로 빠르게 사용해보자
#한쪽 끝에서만 자료의 삽입 삭제가 가능한 queue와 달리 양방향이 가능한 자료 구조
#O(1)의 접근 속도 가짐

from collections import deque

mydeque = deque() #초기화

#데이터 삽입
mydeque =deque([1,2])
mydeque.append(3) #[1,2,3]
mydeque.appendleft(0) #[0,1,2,3]

#데이터 삭제및 반환
mydeque.pop() #3
mydeque.popleft() #0

#deque를 양 끝으로 확장
mydeque2 = deque('kr')

mydeque2.extend('ap') #['k','r','a','p']
mydeque2.extendleft('hi') #['i','h','k','r','a','p']

#원하는 위치에 데이터 삽입 insert
mydeque3 = deque([1,2])
mydeque3.insert(1,3) #[1,3,2]

#원하는 데이터 삭제 remove
mydeque3.remove(1) #[3,2]

#deque를 원하는 만큼 좌, 우로 회전시킨다
#양수면 오른쪽, 음수면 왼쪽으로 원하는 만큼 좌, 우로 회전이 가능
mydeque4 = deque([1,2,3,4])

mydeque4.rotate(2) #[3,4,1,2]
mydeque4.rotate(-1) #[4,1,2,3]