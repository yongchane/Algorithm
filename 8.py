a,b=map(int,input().split())

content =list(map(int,input().split()))

prefix =[0 for _ in range(a+1)]

for c in range(a):
    prefix[c+1] = prefix[c] + content[c] # 초기 값 + 입력한 content 값 -> prefix 배열을 만듬

answer=[] # 간격이 2인 배열 만들기 여기서 최대 값을 찾아야함
for d in range(b,a+1):
    answer.append(prefix[d]-prefix[d-b])
  
maxi=max(answer)
print(maxi)