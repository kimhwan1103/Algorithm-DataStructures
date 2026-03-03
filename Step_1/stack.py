#스택(Stack) - LIFO(Last In First Out) 구조
#한쪽 끝(top)에서만 삽입과 삭제가 가능한 선형 자료구조
#단일 연결 리스트의 appendleft/popleft와 구조가 매우 유사

#노드 클래스 - 데이터와 다음 노드 참조를 저장
class Node:
    def __init__(self, data):
        self.data = data #노드가 저장할 데이터
        self.next = None #다음 노드를 가리키는 참조

#스택 클래스 - top만 관리하면 됨
class Stack:
    def __init__(self):
        self.top = None #스택의 최상단 노드

    #push() - top에 데이터 추가
    #1. 새 노드를 만든다
    #2. 새 노드의 next를 현재 top으로 지정
    #3. top을 새 노드로 업데이트
    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top #새 노드가 기존 top을 가리킴
            self.top = node #top을 새 노드로 변경

    #pop() - top에서 데이터 꺼내기
    #1. top이 비어있으면 None 반환
    #2. 현재 top을 임시 변수에 저장
    #3. top을 다음 노드로 이동
    #4. 임시 변수의 데이터를 반환
    def pop(self):
        if self.top is None: #스택이 비어있으면 None 반환
            return None
        node = self.top #현재 top을 임시 저장
        self.top = self.top.next #top을 다음 노드로 이동
        return node.data #꺼낸 데이터 반환

    #peek() - top 데이터 확인 (제거하지 않음)
    def peek(self):
        if self.top is None: #스택이 비어있으면 None 반환
            return None
        return self.top.data #top의 데이터만 반환

    #is_empty() - 스택이 비어있는지 확인
    def is_empty(self):
        return self.top is None

#코딩 테스트에서는 리스트로 스택을 간단하게 구현할 수 있다

stack = [] #스택 초기화
stack = [1,2,3]
stack.append(4) #push - 원소 추가 [1,2,3,4]
top = stack.pop() #pop - 마지막 원소를 반환하며 제거. top = 4, stack = [1,2,3]
top = stack[-1] #peek - 스택에서 원소를 제거하지 않고 가져오기만 할 때에는 -1을 주면 된다

'''
활용 문제 (출처 : 프로그래머스)
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다.

예를 들어, 문자열 S = baabaa라면, **b aa baa → bb aa → aa → ** 의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다. 제거할 수 없으면 0을 반환합니다.

입출력예
s = baabaa, result = 1
s = cdcd, result = 0
'''

s = 'baabaa'

#알고리즘 문제 함수
def solution(s: str) -> int:
    stack: list[str] = [] #스택 정의
    for ch in s: #문자열 한바퀴 돌리기
        if stack and (ch == stack[-1]): #스택의 top을 확인(peek)하여 현재 문자와 같으면 pop하여 제거
            stack.pop()
        else:
            stack.append(ch) #그렇지않으면 문자를 다시 집어넣음
    return 0 if stack else 1