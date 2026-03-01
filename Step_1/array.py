'''
본 코드는 공부및 복습용으로 작성되어있음
'''

# 1 차원 배열 
list1 = [1,2,3,4,5]
print(list1)

#2 차원 배열
list2 = [[1,2], [3,4], [5,6]]
print(list2)

#빈 리스트 생성 총 2가지 방법 존재
list3 = []
list4 = list()

#리스트에 요소를 추가하거나 삭제 하는 방법
#요소 추가
list3.append(1)

#요소 삭제
list3.pop(1) #데이터를 빼오면서 list에서 데이터를 삭제한다. 즉 데이터를 추출한다고 하면 생각하기 쉽다.
list3.remove(1) #단순히 list에서 데이터를 삭제하는 것이다.
list3.clear() #전체 데이터 삭제

#인덱스 접근
#아까전에 생성했던 2차원 배열에서 1차원을 접근해 보자
print(list2[0]) #예시 출력 결과 : [1,2]

#만약에 2차원 차원인 list2를 다 출력할려면 아래와 같은 방식으로 하거나 아니면 그냥 for문으로 간단하게 한바퀴 돌리는게 좋다.
print(list2[0][0])
print(list2[0][1])
print(list2[1][0])
print(list2[1][1])
print(list2[2][0])
print(list2[2][1])

#for문으로 순회 할 경우 
for row in list2: #첫번째 차원에서 들어가서 차례대로 읽음 
    for val in row: #두번째 차원에서 들어가서 차례대로 읽음
        print(val) 

#배열의 길이
print(f"len of a: {len(list1)}") #len()함수를 사용하여 측정 가능

#특정 위치에서 삽입
list1.insert(1, 6) #[1,6,2,3,4,5]

#리스트끼리 합치기
list_a = [1,2,3]
list_b = [4,5,6]

list_a.extend(list_b) #list_a랑 list_b를 합침 #[1,2,3,4,5,6]

#배열에서 인덱스값 찾기
print(list1.index(3)) # 값 3이 위치한 인덱스 출력: 3 (insert 이후 list1 = [1,6,2,3,4,5])

#배열 정렬하기 sort, sroted 함수 사용 가능 
sort_list = [3, 1, 4, 5, 2]

#sort함수를 사용하여 정렬하기
sort_list.sort() #배열을 오름차순으로 정렬 [1,2,3,4,5]

sort_list2 = ['a', 'y', 'd', 'c', 'e']
sort_list2.sort() #문자열도 똑같이 오름차순으로 정렬 ['a', 'c', 'd' 'e', 'y']

#역순으로 정렬 옵션값 reverse=True으로 해주면 됨
sort_list.sort(reverse=True) #[5,4,3,2,1]

#원하는 순서로 정렬하기 key 옵션을 사용하면 가능

#문자열 길이순으로 정렬 
sort_list3 = ['apple', 'banana', 'kiwi', 'orange']
sort_list3.sort(key=len)#문자열 길이순으로 정렬 #['kiwi', 'apple', 'banana', 'orange']

#절대값으로 정렬 똑같이 key옵션으로 하되 abs으로 해주면 됨
sort_list4 = [3, -2, 1, -4, 5]
sort_list4.sort(key=abs) #[1,2,3,4,5]

#iterable을 원소로 가지는 배열에서 정렬
sort_list5 = [('apple',3), ('banana', 2), ('kiwi', 1), ('orange', 4)]
sort_list5.sort(key=lambda x:x[1]) #2번째 원소를 기준으로 오름차순 정렬 #[('kiwi', 1), ('banana', 2), ('apple', 3), ('orange', 4)]

#배열 슬라이싱~
#start, end, step 모두 양/음수가 가능함
#start는 시작하는 인덱스/end는 끝내는 인덱스/ step는 증가폭,감소폭
#end번째 값은 가져오는 범위에 포함되지 않음
#step은 선택사항임/첫번째 인덱스는 당연히 0/마지막 인덱스는 -1로 사용가능
#슬라이싱 예시를 위해 list1을 다시 선언
list1 = [1,2,3,4,5]
#만약에 list1을 슬라이싱 하여 출력하게 되면
print(list1[0:2]) # [1, 2]
print(list1[0:3]) # [1, 2, 3]
print(list1[0:len(list1)]) #슬라이싱을 할때 len 함수를 사용하여 전체 길이를 구하여 전체를 출력할 수 있음

#step을 추가하여 슬라이싱을 해보자
print(list1[0:3:1]) #[1, 2, 3]
print(list1[0:3:2]) #[1, 3]

#역순으로 슬라이싱이 가능하다
print(list1[-1:0:-1]) #[5, 4, 3, 2] (인덱스 0은 포함되지 않으므로 완전한 역순이 아님)
print(list1[-3]) #3

#인덱스 생략하기
#시작 인덱스를 생략하면 첫 인덱스부터 가져온다는 뜻임
print(list1[:3]) #[1,2,3]
print(list1[:3:-1]) #[5] (끝에서부터 인덱스 3 직전까지, 즉 인덱스 4만 해당)

#끝 인덱스를 생략하면 마지막요소까지 가져온다는 뜻임
print(list1[3:]) #[4, 5]
print(list1[3: :-1]) #[4, 3, 2, 1]
print(list1[: :1]) #전체 순서대로 출력
print(list1[: :-1]) #역순으로 전체 출력

#전체 슬라이싱
print(list1[:])
print(list1[::])

#이제부터 2차원 배열을 슬라이싱을 해보자 numpy을 사용하면 쉽게 되지만 코딩테스트를 하거나 numpy을 사용하지 못하는 환경이면 기본 문법을 사용하여 슬라이싱 가능

#행(row) 슬라이싱 - 바깥 리스트를 슬라이싱하면 행 단위로 잘린다
print(list2[0:2]) #[[1,2], [3,4]] -> 0~1번째 행
print(list2[1:]) #[[3,4], [5,6]] -> 1번째 행부터 끝까지
print(list2[:2]) #[[1,2], [3,4]] -> 처음부터 1번째 행까지

#열(column) 슬라이싱 - 리스트 컴프리헨션을 사용해야 한다
print([row[1] for row in list2]) #[2, 4, 6] -> 모든 행의 1번째 열
print([row[0] for row in list2]) #[1, 3, 5] -> 모든 행의 0번째 열

#행 + 열 동시 슬라이싱 - 바깥은 행 슬라이싱, 안쪽은 리스트 컴프리헨션으로 열 슬라이싱
print([row[1] for row in list2[0:2]]) #[2, 4] -> 0~1번째 행의 1번째 열
print([row[0] for row in list2[1:3]]) #[3, 5] -> 1~2번째 행의 0번째 열
