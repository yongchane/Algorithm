n = int(input())

hint = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for a in range(1, 10):  # 100의 자리수
    for b in range(1, 10):  # 10의 자리수
        for c in range(1, 10):  # 1의 자리수
            if a == b or b == c or c == a:  # 서로 다른 숫자로 이루어진 세 자리 수만 고려
                continue

            # 후보 숫자를 문자열로 변환
            candidate = str(a) + str(b) + str(c)

            valid = True
            for arr in hint:
                number, strike, ball = arr[0], arr[1], arr[2]

                # 주어진 숫자를 문자열로 변환
                number_str = str(number)

                # strike와 ball 카운트 계산
                strike_count = 0
                ball_count = 0
                for i in range(3):  # 각 자릿수 비교
                    if candidate[i] == number_str[i]:  # 자릿수가 같고 숫자가 같으면 strike
                        strike_count += 1
                    elif candidate[i] in number_str:  # 숫자가 포함되어 있지만 자릿수가 다르면 ball
                        ball_count += 1

                # 주어진 strike와 ball 조건을 만족하지 않으면 후보 탈락
                if strike_count != strike or ball_count != ball:
                    valid = False
                    break

            if valid:  # 모든 조건을 만족하면 정답 후보로 추가
                answer += 1

print(answer)