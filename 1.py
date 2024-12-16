# 입력을 받고 (디테일 )

# Default input -> 스트링 타입, 문자열 타입으로 받아와 주도록 만들어짐

# 배열
# list =[0,0,0,0]
# list =["a","b","c"]

# case 1: 단순히 정수일때 int 를 붙임
# number=int(input())

# case 2: 수열 (숫자들의 모임)
list1 =list(map(int,input().split())) # map을 통해 여러개를 받고 split으로 쪼갠후 int 타입으로 나눠줌
print(list1)

#case 3: 단순히 문자일떄
# string =input()  

# case 4: 문자열 
list2 =list(map(str, input().split()))
print(list2) 

# 계산을 하고


# 출력을 한다

