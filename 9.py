# 완전 탐색

# 누적합

# 투포인터

N = int(input())

lst=[]
result=0
for i in range(N):
    x,y= map(int,input().split())
    lst.append([x,y])
    # 기둥을 x 축으로 나열
    lst.sort()
print(result)

i=0
# lst -> l이 lst에 들어있는 배열값이 됨
for l in  lst:
    if l[1] > result: # l[0]-> [2,3] 일때 2 임 
        result=l[1] # 전보다 높이가 높을때(값이 클때) 업데이트됌  이때 result는 가장 큰 높이가 더해짐
        idx=i # i값을 통해 가장 높은 위치를 알 수 있음
    i +=1 # i는 가장 높은 높이 위치를 찾게됨 ex) n 번쨰가 제일 높음
print(idx)
print("1번",result)
# 첫번째[0]의 기둥의 높이를[1] 나타냄
height=lst[0][1]

# 최대 높이 전까지 높이를 더해주는 작
for i in range(idx):
    if height < lst[i+1][1]: # 첫번째 높이가 다음 높이보다 작으면 
        result += height*(lst[i+1][0]-lst[i][0]) # lst의 x축을 뺴서 더해야할 높이를 곱해줌(높이가 7인게 3개)
        height = lst[i+1][1] # 더한후 높이는 첫번쨰 값보다 높은 값으로 갱신됌
    else: # 아니면 계속 값을 더해 나감
        result += height*(lst[i+1][0]-lst[i][0])
print("2번",result)
height=lst[-1][1]

for i in range(N-1,idx,-1):
    if height < lst[i-1][1]: # 첫번째 높이가 다음 높이보다 작으면 
        result += height*(lst[i][0]-lst[i-1][0]) # lst의 x축을 뺴서 더해야할 높이를 곱해줌(높이가 7인게 3개)
        height =lst[i-1][1] # 더한후 높이는 첫번쨰 값보다 높은 값으로 갱신됌
    else: # 아니면 계속 값을 더해 나감
        result += height*(lst[i][0]-lst[i-1][0])

print(result)