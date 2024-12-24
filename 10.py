graph= [list(map(int,input().split()))for _ in range(4)]

x1,y1,x2,y2=map(int,input().split())

prefix=[[0 for _ in range(5)]for _ in range(5)] # 2차원 배열을 만든다 x,y 그래프를 만들었다고 생각하면 편함

for y in range(4):
    for x in range(4):
        prefix[y+1][x+1] = prefix[y][x+1] + prefix[y+1][x] -prefix[y][x] +graph[y][x] 

anw=prefix[x2][y2]-prefix[x2][y1-1]-prefix[x1-1][y2] +prefix[x1-1][y1-1]

print(anw)