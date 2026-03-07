# 기초 자료 구조

## 배열 / 리스트

배열은 하나의 변수에 하나 이상의 Value을 가질 수 있는 것이다. 또한 데이터를 나열하고 배열 속 각 데이터들에 인덱스로 접근 할 수 있다.

### 배열이 필요한 이유

1. 같은 종류의 데이터를 효율적으로 관리하기 위해
2. 같은 종류의 데이터를 순차적으로 저장
3. 인덱스 번호를 사용한 데이터 접근 가능

파이썬의 경우 위에서 말하고 있는 1, 2번의 경우가 해당하지 않는다. 그 이유는 파이썬의 list는 각기 다른 종류의 데이터도 저장이 가능하기 때문이다.

즉 파이썬에서는 배열은 다량의 데이터를 순차적, 효율적으로 저장 관리, 인덱스를 사용하여 직접 접근하기 위해 사용한다.

### 배열 생성

```python
# 1차원 배열
list1 = [1, 2, 3, 4, 5]

# 2차원 배열
list2 = [[1, 2], [3, 4], [5, 6]]

# 빈 리스트 생성 (2가지 방법)
list3 = []
list4 = list()
```

### 요소 추가 / 삭제

| 메서드 | 설명 |
|--------|------|
| `append(x)` | 리스트 끝에 요소 추가 |
| `insert(i, x)` | 인덱스 i 위치에 요소 삽입 |
| `extend(list)` | 다른 리스트의 모든 요소를 뒤에 합침 |
| `pop(i)` | 인덱스 i의 요소를 꺼내면서 삭제 (반환값 있음) |
| `remove(x)` | 값 x와 일치하는 첫 번째 요소를 삭제 (반환값 없음) |
| `clear()` | 전체 요소 삭제 |

### 인덱스 접근

```python
list2[0]       # [1, 2] — 1차원 접근
list2[0][1]    # 2 — 2차원 접근
list1.index(3) # 값 3이 위치한 인덱스를 반환
```

### 순회

```python
# for문으로 2차원 배열 순회
for row in list2:
    for val in row:
        print(val)
```

### 정렬

```python
# 기본 오름차순 정렬
sort_list.sort()

# 역순 정렬
sort_list.sort(reverse=True)

# key 옵션으로 정렬 기준 지정
sort_list3.sort(key=len)            # 문자열 길이순
sort_list4.sort(key=abs)            # 절대값 기준
sort_list5.sort(key=lambda x: x[1]) # 튜플의 두 번째 원소 기준
```

### 슬라이싱

`list[start:end:step]` 형태로 사용하며, **end 인덱스는 포함되지 않는다.**

```python
list1 = [1, 2, 3, 4, 5]

# 기본 슬라이싱
list1[0:2]   # [1, 2]
list1[0:3]   # [1, 2, 3]

# step 사용
list1[0:3:2] # [1, 3]

# 역순 슬라이싱
list1[::-1]  # [5, 4, 3, 2, 1] — 전체 역순

# 인덱스 생략
list1[:3]    # [1, 2, 3] — 처음부터
list1[3:]    # [4, 5] — 끝까지
```

#### 2차원 배열 슬라이싱

```python
list2 = [[1, 2], [3, 4], [5, 6]]

# 행(row) 슬라이싱
list2[0:2]  # [[1, 2], [3, 4]]

# 열(column) 슬라이싱 — 리스트 컴프리헨션 사용
[row[1] for row in list2]       # [2, 4, 6]

# 행 + 열 동시 슬라이싱
[row[1] for row in list2[0:2]]  # [2, 4]
```

### 시간복잡도

| 연산 | 시간복잡도 | 이유 |
|------|-----------|------|
| `list[i]` 접근 | O(1) | 인덱스로 바로 접근 |
| `append()` | O(1) | 끝에 추가 |
| `pop()` 마지막 | O(1) | 끝에서 제거 |
| `pop(i)` / `insert(i)` | O(n) | 중간 요소들을 밀어야 함 |
| `remove()` / `in` 검색 | O(n) | 처음부터 순차 탐색 |
| `sort()` | O(n log n) | Timsort 알고리즘 |

## 연결 리스트

연결 리스트는 데이터를 연속된 메모리 공간에 저장하지 않고 각 데이터가 다음 위치를 가리키는 방식으로 구성된 선형적인 자료구조이다.

각 데이터 단위를 노드라고 하고 노드는 데이터를 저장하는 공간과 다음 노드를 가리키는 참조를 포함시킨다.

배열은 인덱스를 활용하여 원소에 쉽게 접근할 수 있지만 원소를 추가하거나 삭제할 때 연속된 메모리 공간에서 이동해야 하므로 시간이 걸린다. 하지만 연결 리스트 같은 경우 자료의 크기가 정해져 있지 않거나 추가와 삭제가 자주 발생하는 경우에는 연결리스트가 더 적합하다.

### 단일 연결 리스트 구조

- 각 노드는 값과 다음 노드의 참조를 저장한다
- head는 연결 리스트의 첫번째 노드를 가리키며 연결 리스트에 접근하기 위한 시작점 역할을 한다.

### 연결 리스트의 주요 특징

- 동적 크기 조절 : 배열과 달리 크기가 정의되어 있지 않아 필요에 따라 노드를 추가하거나 삭제가 가능하다
- 삽입과 삭제가 쉬움 : 배열은 삽입/삭제 시 이후 모든 원소를 이동시켜야 한다. 연결 리스트는 참조만 바꾸면 되므로 효율적이다.
- 메모리 효율성 : 배열은 미리 메모리 공간을 할당해야한다. 연결리스트는 필요한 만큼만 메모리를 사용하므로 메모리 낭비를 줄일수 있다.

### 노드 구현

파이썬은 모든 것이 객체이므로 객체 지향 방식으로 연결 리스트를 비교적 쉽게 구현할 수 있다.

```python
class Node:
    def __init__(self, data):
        self.data = data  # 값을 저장
        self.next = None  # 다음 노드를 가리킴
```

### 간단한 연결 리스트 만들기

```python
# 노드 생성 및 연결
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# 순회하며 출력 (head를 직접 이동하면 리스트를 잃으므로 임시 변수 사용)
node = head
while node:
    print(node.data)
    node = node.next

# 끝에 새 노드 추가
node = head
while node.next:
    node = node.next
node.next = Node(4)

# 처음에 새 노드 추가
node = Node(0)
node.next = head
head = node
```

### LinkedList 클래스 구현

| 메서드 | 설명 |
|--------|------|
| `appendleft(data)` | 리스트 앞에 노드 추가 |
| `append(data)` | 리스트 끝에 노드 추가 |
| `popleft()` | 첫 번째 노드를 꺼내서 반환 |
| `pop()` | 마지막 노드를 꺼내서 반환 |
| `remove(target)` | 특정 값을 가진 노드 삭제 |
| `insert(i, data)` | 특정 인덱스에 노드 삽입 |
| `reverse()` | 연결 리스트 뒤집기 |

#### appendleft — 앞에 추가

```python
def appendleft(self, data):
    if self.head is None:
        self.head = Node(data)
    else:
        node = Node(data)
        node.next = self.head
        self.head = node
    self.length += 1
```

#### append — 끝에 추가

```python
def append(self, data):
    if self.head is None:
        self.head = Node(data)
    else:
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(data)
    self.length += 1
```

#### popleft — 앞에서 꺼내기

값을 반환해야 하므로 head를 옮기기 전에 임시 변수에 저장해야 한다.

```python
def popleft(self):
    if self.head is None:
        return None
    node = self.head
    self.head = self.head.next
    self.length -= 1
    return node.data
```

#### pop — 끝에서 꺼내기

마지막 노드를 제거하려면 이전 노드(prev)의 next를 None으로 바꿔야 하므로 임시 노드 2개가 필요하다.

```python
def pop(self):
    if self.head is None:
        return None
    node = self.head
    while node.next is not None:
        prev = node
        node = node.next
    if node == self.head:
        self.head = None
    else:
        prev.next = None
    self.length -= 1
    return node.data
```

#### remove — 특정 값 삭제

popleft와 pop의 아이디어를 조합. node는 삭제할 값을 찾을 때까지 이동하고 prev는 그 뒤를 따라간다.

```python
def remove(self, target):
    if self.head is None:
        return False
    node = self.head
    while node is not None and node.data != target:
        prev = node
        node = node.next
    if node is None:
        return False
    if node == self.head:
        self.head = self.head.next
    else:
        prev.next = node.next
    self.length -= 1
    return True
```

#### insert — 특정 위치에 삽입

인덱스가 범위를 벗어나면 appendleft 또는 append로 처리한다.

```python
def insert(self, i, data):
    if i <= 0:
        self.appendleft(data)
    elif i >= self.length:
        self.append(data)
    else:
        node = self.head
        for _ in range(i - 1):
            node = node.next
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        self.length += 1
```

#### reverse — 뒤집기

node.next를 이전 노드로 바꾸면 다음 노드와의 연결이 끊어지므로, 다음 노드를 미리 저장할 변수(ahead)가 필요하다.

```python
def reverse(self):
    if self.length < 2:
        return
    prev = None
    ahead = self.head.next
    while ahead:
        self.head.next = prev
        prev = self.head
        self.head = ahead
        ahead = ahead.next
    self.head.next = prev
```

### 시간복잡도

| 연산 | 시간복잡도 | 이유 |
|------|-----------|------|
| `appendleft()` | O(1) | head만 변경 |
| `append()` | O(n) | 끝까지 순회 필요 |
| `popleft()` | O(1) | head만 변경 |
| `pop()` | O(n) | 끝까지 순회 필요 |
| `insert(i)` | O(n) | 삽입 지점까지 순회 |
| `remove()` | O(n) | 값을 찾을 때까지 순회 |
| `reverse()` | O(n) | 전체 노드 순회 |
| 인덱스 접근 | O(n) | 처음부터 순회해야 함 (배열은 O(1)) |

### 코딩 테스트에서는?

파이썬에서 연결 리스트를 직접 구현할 일은 거의 없다. 대부분 `list`나 `collections.deque`로 대체한다.

| 목적 | 사용할 것 |
|------|----------|
| 자료구조 수업/시험 | 직접 구현 |
| 코딩 테스트 | `list` 또는 `deque` |
| 실무 개발 | `list` 또는 `deque` |

### 이중 연결 리스트 (Doubly Linked List)

단일 연결 리스트는 `next`만 가지고 있어 한 방향으로만 이동 가능하다. 이중 연결 리스트는 각 노드가 `prev`와 `next`를 모두 가지고 있어 양쪽 방향으로 순회할 수 있다.

```
None ← [1] ⇄ [2] ⇄ [3] → None
        head              tail
```

#### 노드 구현

```python
class DualNode:
    def __init__(self, data):
        self.data = data  # 노드가 저장할 실제 데이터
        self.prev = None  # 이전 노드를 가리키는 참조
        self.next = None  # 다음 노드를 가리키는 참조
```

#### DoublyLinkedList 클래스 구현

head(시작점)와 tail(끝점)을 항상 알고 있어야 한다.

| 메서드 | 설명 |
|--------|------|
| `append(data)` | 리스트 끝에 노드 추가 |
| `appendleft(data)` | 리스트 앞에 노드 추가 |
| `remove(data)` | 특정 값을 가진 노드 삭제 |
| `print_forward()` | head → tail 순방향 출력 |
| `print_backward()` | tail → head 역방향 출력 |

#### append — 끝에 추가

```python
def append(self, data):
    new_node = DualNode(data)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node   # 현재 tail의 next를 새 노드로
        new_node.prev = self.tail   # 새 노드의 prev를 현재 tail로
        self.tail = new_node        # tail을 새 노드로 업데이트
    self.size += 1
```

#### appendleft — 앞에 추가

```python
def appendleft(self, data):
    new_node = DualNode(data)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head   # 새 노드의 next를 현재 head로
        self.head.prev = new_node   # 현재 head의 prev를 새 노드로
        self.head = new_node        # head를 새 노드로 업데이트
    self.size += 1
```

#### remove — 특정 값 삭제

이중 연결 리스트는 `prev`를 이미 알고 있으므로 삭제가 단일 리스트보다 직관적이다. head, tail, 중간 3가지 경우를 처리한다.

```python
def remove(self, data):
    current = self.head
    while current:
        if current.data == data:
            if current == self.head:        # head 삭제
                self.head = current.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None
            elif current == self.tail:      # tail 삭제
                self.tail = current.prev
                self.tail.next = None
            else:                           # 중간 노드 삭제
                current.prev.next = current.next
                current.next.prev = current.prev
            self.size -= 1
            return True
        current = current.next
    return False
```

#### 단일 vs 이중 연결 리스트 비교

| 연산 | 단일 | 이중 |
|------|------|------|
| `append()` | O(n) — 끝까지 순회 | **O(1)** — tail 사용 |
| `appendleft()` | O(1) | O(1) |
| `pop()` | O(n) — prev를 모름 | **O(1)** — tail.prev 사용 |
| `popleft()` | O(1) | O(1) |
| 메모리 | 적음 (next만) | 많음 (prev + next) |

### 원형 연결 리스트 (Circular Linked List)

단일 연결 리스트 구조에서 마지막 노드의 `next`가 `None`이 아닌 다시 `head`를 가리키도록 한 구조이다.

```
[1] → [2] → [3] → (다시 [1]로)
 head         tail
```

#### 구현 핵심

```python
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```

#### append — 끝에 추가

```python
def append(self, data):
    new_node = Node(data)
    if self.is_empty():
        self.head = new_node
        self.tail = new_node
        new_node.next = self.head   # 자기 자신을 가리킴 (원형)
    else:
        self.tail.next = new_node   # 기존 tail의 next에 새 노드 연결
        self.tail = new_node        # tail을 새 노드로 업데이트
        self.tail.next = self.head  # 새 tail이 다시 head를 가리킴 (원형 유지)
```

#### 순회 — `__iter__`

원형이므로 다시 head로 돌아오면 종료해야 무한 루프를 방지할 수 있다.

```python
def __iter__(self):
    if self.is_empty():
        return
    current = self.head
    while True:
        yield current.data
        current = current.next
        if current == self.head:  # 다시 head로 돌아오면 종료
            break
```

### 연결 리스트 종류 총정리

| 종류 | 방향 | 특징 |
|------|------|------|
| 단일 연결 리스트 | → | `next`만 있음. 구현이 가장 단순 |
| 이중 연결 리스트 | ← → | `prev` + `next`. 양방향 순회 가능, `pop()` O(1) |
| 원형 연결 리스트 | → (순환) | 마지막 노드가 head를 가리킴. 순환 구조 |

## 스택

한쪽 끝(top)에서만 자료의 삽입과 삭제가 가능한 **LIFO(Last In First Out)** 형식의 선형 자료구조이다. 가장 나중에 삽입한 자료가 가장 먼저 반환된다.

단일 연결 리스트의 `appendleft`/`popleft`와 구조가 매우 유사하다.

### 스택 직접 구현

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
```

| 메서드 | 설명 |
|--------|------|
| `push(data)` | top에 데이터 추가 |
| `pop()` | top에서 데이터 꺼내기 |
| `peek()` | top 데이터 확인 (제거하지 않음) |
| `is_empty()` | 스택이 비어있는지 확인 |

#### push — top에 추가

```python
def push(self, data):
    node = Node(data)
    node.next = self.top  # top이 None이어도 상관없음
    self.top = node
```

#### pop — top에서 꺼내기

```python
def pop(self):
    if self.top is None:
        return None
    node = self.top
    self.top = self.top.next
    return node.data
```

#### peek — top 확인

```python
def peek(self):
    if self.top is None:
        return None
    return self.top.data
```

### 코딩 테스트에서는 list로 구현

```python
stack = []
stack.append(4)    # push
top = stack.pop()  # pop → 4
top = stack[-1]    # peek (제거하지 않고 확인)
not stack          # is_empty
```

| 직접 구현 | `list` |
|----------|--------|
| `stack.push(x)` | `stack.append(x)` |
| `stack.pop()` | `stack.pop()` |
| `stack.peek()` | `stack[-1]` |
| `stack.is_empty()` | `not stack` |

### 시간복잡도

| 연산 | 시간복잡도 |
|------|-----------|
| `push()` | O(1) |
| `pop()` | O(1) |
| `peek()` | O(1) |
| 탐색 | O(n) |

## 큐

한쪽 끝(rear)에서 삽입하고 반대쪽 끝(front)에서 꺼내는 **FIFO(First In First Out)** 형식의 선형 자료구조이다. 가장 먼저 삽입한 자료가 가장 먼저 반환된다.

- 스택과 동일하게 가장 최근에 저장된 값 다음에 새로운 값이 저장
- 가장 오래전에 저장된 값부터 나간다는 점에서 차이가 있음 즉 FIFO 원칙이 적용됨
- 스택과 마찬가지로 리스트가 큐의 모든 연산을 지원
- 리스트는 동적 배열로 구현되어 큐의 연산을 수행하기에 효율적이지 않음 (`pop(0)`이 O(n))
- 파이썬에서 큐를 구현할 때는 덱을 이용

### 큐 직접 구현

단일 연결 리스트의 `append`/`popleft`와 구조가 매우 유사하다.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
```

| 메서드 | 설명 |
|--------|------|
| `enqueue(data)` | rear에 데이터 추가 |
| `dequeue()` | front에서 데이터 꺼내기 |
| `peek()` | front 데이터 확인 (제거하지 않음) |
| `is_empty()` | 큐가 비어있는지 확인 |

#### enqueue — rear에 추가

```python
def enqueue(self, data):
    node = Node(data)
    if self.rear is None:
        self.front = node
        self.rear = node
    else:
        self.rear.next = node
        self.rear = node
```

#### dequeue — front에서 꺼내기

```python
def dequeue(self):
    if self.front is None:
        return None
    node = self.front
    self.front = self.front.next
    if self.front is None:  # 큐가 비었으면 rear도 None으로
        self.rear = None
    return node.data
```

#### peek — front 확인

```python
def peek(self):
    if self.front is None:
        return None
    return self.front.data
```

### 코딩 테스트에서는 deque로 구현

`list`의 `pop(0)`은 O(n)이므로 큐가 필요하면 `collections.deque`를 사용한다.

```python
from collections import deque

queue = deque()
queue.append(1)     # enqueue
queue.append(2)
val = queue.popleft()  # dequeue → 1
front = queue[0]       # peek
not queue              # is_empty
```

| 직접 구현 | `deque` |
|----------|---------|
| `queue.enqueue(x)` | `queue.append(x)` |
| `queue.dequeue()` | `queue.popleft()` |
| `queue.peek()` | `queue[0]` |
| `queue.is_empty()` | `not queue` |

### 시간복잡도

| 연산 | 시간복잡도 (연결 리스트 / deque) | `list`의 경우 |
|------|-------------------------------|--------------|
| `enqueue()` | O(1) | O(1) — `append()` |
| `dequeue()` | O(1) | **O(n)** — `pop(0)` |
| `peek()` | O(1) | O(1) |
| 탐색 | O(n) | O(n) |

## 덱 (Deque)

**Double-Ended Queue**의 약자로, 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조이다. 스택과 큐의 기능을 모두 포함한다.

```
← popleft  [front ... rear]  pop →
← appendleft               append →
```

### collections.deque

파이썬에서는 `collections.deque`가 덱을 구현한 클래스이다. 내부적으로 이중 연결 리스트로 구현되어 양쪽 끝 연산이 모두 O(1)이다.

```python
from collections import deque

dq = deque()
dq.append(1)        # 오른쪽 끝에 추가
dq.appendleft(0)    # 왼쪽 끝에 추가
dq.pop()             # 오른쪽 끝에서 꺼내기 → 1
dq.popleft()         # 왼쪽 끝에서 꺼내기 → 0
```

### deque 주요 메서드

| 메서드 | 설명 |
|--------|------|
| `append(x)` | 오른쪽 끝에 추가 |
| `appendleft(x)` | 왼쪽 끝에 추가 |
| `pop()` | 오른쪽 끝에서 꺼내기 |
| `popleft()` | 왼쪽 끝에서 꺼내기 |
| `extend(iterable)` | 오른쪽에 여러 요소 추가 |
| `extendleft(iterable)` | 왼쪽에 여러 요소 추가 (역순으로 들어감) |
| `rotate(n)` | 오른쪽으로 n칸 회전 (음수면 왼쪽) |
| `deque(maxlen=n)` | 최대 길이 제한 (초과 시 반대쪽에서 자동 제거) |

### rotate 예시

```python
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)   # deque([4, 5, 1, 2, 3]) — 오른쪽으로 2칸
dq.rotate(-1)  # deque([5, 1, 2, 3, 4]) — 왼쪽으로 1칸
```

### maxlen 예시

```python
dq = deque(maxlen=3)
dq.append(1)  # deque([1])
dq.append(2)  # deque([1, 2])
dq.append(3)  # deque([1, 2, 3])
dq.append(4)  # deque([2, 3, 4]) — 1이 자동으로 제거됨
```

### 시간복잡도

| 연산 | `deque` | `list` |
|------|---------|--------|
| `append()` | O(1) | O(1) |
| `appendleft()` | O(1) | **O(n)** — `insert(0, x)` |
| `pop()` | O(1) | O(1) |
| `popleft()` | O(1) | **O(n)** — `pop(0)` |
| `rotate(n)` | O(n) | — |
| 인덱스 접근 `[i]` | **O(n)** | O(1) |

### 스택 / 큐 / 덱 비교

| 자료구조 | 삽입 위치 | 삭제 위치 | 원칙 | 파이썬 구현 |
|---------|----------|----------|------|-----------|
| 스택 | top | top | LIFO | `list` |
| 큐 | rear | front | FIFO | `deque` |
| 덱 | 양쪽 | 양쪽 | — | `deque` |